from util import *
from fmt import *

from collections import namedtuple
from bs4 import BeautifulSoup
from pathlib import Path
from slugify import slugify
import re

specdir = Path("contrib")
output_json = Path("spec-json")


# Match a list of one-or-more keywords such as the string `"foo"; "bar";`
# Each keyword is alpha-numeric and may (rarely) contain a hyphen.
KEYWORDS_PATTERN = re.compile(r'"[a-zA-Z0-9/-]+"(; "[a-zA-Z0-9/-]+")*')

# Match a element exceptions such as the string "element (if ...)'
EXCEPTION_PATTERN = re.compile(r'([a-zA-Z0-9-]+) \(if [a-zA-Z0-9\' -]+\)')


with Path("COPYING.txt").open("r") as fp:
    COPYING = fp.read().split("\n\n")

with (specdir / "timestamp").open("r") as fp:
    COPYING.append("Based on current published specifications accessed " + fp.read().strip())

COPYING = [x.replace("\n", " ").strip() for x in COPYING]


# Global attributes common to all HTML elements
# source: https://html.spec.whatwg.org/multipage/dom.html#global-attributes
# plus class, id, slot, role (ARIA)
global_attributes = \
[
    "accesskey",
    "autocapitalize",
    "class",
    "contenteditable",
    "dir",
    "draggable",
    "enterkeyhint",
    "hidden",
    "id",
    "inputmode",
    "is",
    "itemid",
    "itemprop",
    "itemref",
    "itemscope",
    "itemtype",
    "lang",
    "nonce",
    "role", # ARIA
    "slot",
    "spellcheck",
    "style",
    "tabindex",
    "title",
    "translate",
]


t_element       = namedtuple("Element",       ["name", "desc", "categories", "attributes", "children"])
t_category      = namedtuple("Category",      ["name", "elements", "elements_maybe", "exceptions"])
t_attribute     = namedtuple("Attributes",    ["name", "elements", "desc", "value_type", "value_keywords"])
t_event_handler = namedtuple("EventHandlers", ["name", "applies_to"])


def gen_elements(element):
    if element == "autonomous custom elements":
        pass
    elif ", " in element:
        # e.g. h1, h2, h3, h4, h5, h6
        for e in element.split(", "):
            yield from gen_elements(e)
    elif ";" in element:
        for e in element.split(";"):
            yield from gen_elements(e.strip())
    elif " " in element:
        # e.g. MathML math, SVG svg, ElementSpec element
        yield element.split(" ")[1]
    else:
        yield element


def gen_attributes(attributes):
    for attribute in attributes.split(";"):
        attr = attribute.strip("*").strip()

        if attr == "type\nsrcset":
            # Fix a bug in the spec formatting
            # https://github.com/whatwg/html/pull/4543
            yield "type"
            yield "srcset"

        elif attr == "globals":
            yield from global_attributes
        else:
            yield attr


def gen_categories(categories):
    for category in categories.split(";"):
        category = category.strip().strip("*")
        if category == "empty":
            continue
        yield category


def gen_keywords(keywords):
    """Given a `keywords` string such as `"foo"; "bar"`, yield each keyword.
    Otherwise, yield nothing."""
    if KEYWORDS_PATTERN.fullmatch(keywords):
        yield from map(lambda x: x.strip().strip("\""), keywords.split(";"))


def parse_index_elements(soup):

    rows = soup.find("h3", {"id": "elements-3"}).findNext("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all(["th", "td"])
        cells = [x.get_text() for x in cells]
        assert len(cells) == 7

        element, desc, categories, _, children, attributes, _ = cells

        elements = gen_elements(element)
        categories = set(gen_categories(categories))
        attributes = set(gen_attributes(attributes))
        children = set(gen_categories(children))

        for i in sorted(elements):
            yield t_element(i, desc.strip(), categories, attributes, children)


def parse_index_categories(soup):

    rows = soup.find("h3", {"id": "element-content-categories"}).findNext("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all(["th", "td"])
        cells = [x.get_text() for x in cells]
        assert len(cells) == 3

        category, elements, exceptions = cells

        exceptions = "; ".join(map(lambda x: x.strip(), exceptions.split(";")))
        if category.strip().endswith("*"):
            exceptions += "; The tabindex attribute can also make any element into interactive content."
        category = category.strip().strip("*")

        elements = set(gen_elements(elements))

        if exceptions == "—":
            exceptions = ""

        elements_maybe = parse_element_exceptions_string(exceptions)

        yield t_category(category, elements, elements_maybe, exceptions)


def parse_index_attributes(soup):
    rows = soup.find("h3", {"id": "attributes-3"}).findNext("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all(["th", "td"])
        cells = [x.get_text() for x in cells]
        assert len(cells) == 4

        attribute, elements, desc, value = cells
        value_desc = " ".join([x.strip().strip("*") for x in value.split("\n")])
        value_desc = value_desc.strip()
        if value.strip().endswith("*"):
            value_desc += ". The actual rules are more complicated than indicated"
        value_keywords = set(gen_keywords(value_desc))
        if value_keywords:
            value_desc = "Keywords"

        elements = set(map(lambda x: x.strip(";\n "), gen_elements(elements)))
        yield t_attribute(attribute.strip(), elements, desc.strip(), value_desc, value_keywords)


def parse_index_event_handlers(soup):
    rows = soup.find("table", {"id": "ix-event-handlers"}).findNext("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all(["th", "td"])
        cells = [x.get_text() for x in cells]
        assert len(cells) == 4

        attribute, elements, _, _ = cells

        yield t_event_handler(attribute.strip(), elements.strip())


def parse_input_type_keywords(soup):
    rows = soup.find("table", {"id": "attr-input-type-keywords"}).findNext("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all(["th", "td"])
        cells = [x.get_text() for x in cells]
        keyword, *_ = cells

        yield keyword.strip()


def parse_aria_roles(soup):
    concrete_roles = {
        "widget",
        "document_structure_roles",
        "landmark_roles",
        "live_region_roles",
        "window_roles",
    }

    for role in concrete_roles:
        rows = soup.find("section", {"id": role}).findNext("ul").find_all("li")

        for row in rows:
            keyword = row.find("code").get_text()
            yield keyword.strip()


def parse_element_exceptions_string(xs):
    # e.g. "element (if ...); ...' -> [element, ...]
    if not xs: return

    if ";" in xs:
        xs = xs.split(";")
    else:
        xs = [xs]

    for x in xs:
        x = x.strip()
        matches = EXCEPTION_PATTERN.fullmatch(x)
        if matches:
            yield matches.group(1)


def parse_element_types(soup):
    rows = soup.find("h4", {"id": "elements-2"}).findNext("dl")
    result = {}

    for dt, dd in grouper(rows, 2):
        elements = dd.find_all("code")
        if not elements: continue

        dfn = dt.find("dfn").get_text()
        dfn = slugify(dfn)
        if dfn not in result:
            result[dfn] = []

        for element in elements:
            name = element.get_text()
            result[dfn].append(name)

    return result


def element_wrapper(element_name):
    """NOTE: Not injection safe"""
    def f(content):
        return "<%s>%s</%s>" % (element_name, content, element_name)
    return f


with (specdir / "indices.html").open("r") as fp:
    g_soup = BeautifulSoup(fp, "lxml")


g_elements = parse_index_elements(g_soup)
g_categories = parse_index_categories(g_soup)
g_attributes = list(parse_index_attributes(g_soup)) # excl. event handlers
g_event_handlers = list(parse_index_event_handlers(g_soup))

with (specdir / "input.html").open("r") as fp:
    g_soup = BeautifulSoup(fp, "lxml")

g_attributes.append(t_attribute("type", set(["input"]),
    "Type of form control", "An input type e.g. \"text\"", set(parse_input_type_keywords(g_soup))))


with (specdir / "aria.html").open("r") as fp:
    g_soup = BeautifulSoup(fp, "lxml")

g_attributes.append(t_attribute("role", set(["HTML"]),
    "ARIA semantic role", "A concrete ARIA role", set(parse_aria_roles(g_soup))))


with (specdir / "syntax.html").open("r") as fp:
    g_soup = BeautifulSoup(fp, "lxml")

g_element_types = parse_element_types(g_soup)


META={
    "copyright": COPYING
}

g_elements = dictify_namedtuples(g_elements, meta=META)
g_categories = dictify_namedtuples(g_categories, meta=META)
g_attributes = dictify_namedtuples(g_attributes, merge=False, meta=META)
g_event_handlers = dictify_namedtuples(g_event_handlers, meta=META)


outputs = [
    ("elements", g_elements),
    ("categories", g_categories),
    ("attributes", g_attributes),
    ("event-handlers", g_event_handlers),
    ("element-types", g_element_types),
]

for k, v in outputs:
    with (output_json / (k + ".json")).open("wb") as fp:
        fp.write("".join(pformat(v)).encode("utf-8"))

