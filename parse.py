from util import *
from fmt import *

from collections import namedtuple
from bs4 import BeautifulSoup
from pathlib import Path
import re

specdir = Path("spec")


# Match a list of one-or-more keywords such as the string `"foo"; "bar";`
# Each keyword is alpha-numeric and may (rarely) contain a hyphen.
KEYWORDS_PATTERN = re.compile(r'"[a-zA-Z0-9-]+"(; "[a-zA-Z0-9-]+")*')

# Match a element exceptions such as the string "element (if ...)'
EXCEPTION_PATTERN = re.compile(r'([a-zA-Z0-9-]+) \(if [a-zA-Z0-9\' -]+\)')


# Global attributes common to all elements
# source: https://html.spec.whatwg.org/multipage/dom.html#global-attributes
global_attributes = \
[
    "accesskey",
    "autocapitalize",
    "contenteditable",
    "dir",
    "draggable",
    "enterkeyhint",
    "hidden",
    "inputmode",
    "is",
    "itemid",
    "itemprop",
    "itemref",
    "itemscope",
    "itemtype",
    "lang",
    "nonce",
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
        attr = attribute.strip()

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
    "Type of form control", "e.g. \"text\"", parse_input_type_keywords(g_soup)))

g_elements = dictify_namedtuples(g_elements)
g_categories = dictify_namedtuples(g_categories)
for i in g_attributes:
    if i[0] == "autocomplete":
        print(i)
g_attributes = dictify_namedtuples(g_attributes)
g_event_handlers = dictify_namedtuples(g_event_handlers)


with open("bin/elements.json", "wb") as fp:
    fp.write("".join(pformat(g_elements)).encode("utf-8"))

with open("bin/categories.json", "wb") as fp:
    fp.write("".join(pformat(g_categories)).encode("utf-8"))

with open("bin/attributes.json", "wb") as fp:
    fp.write("".join(pformat(g_attributes)).encode("utf-8"))

with open("bin/event_handlers.json", "wb") as fp:
    fp.write("".join(pformat(g_event_handlers)).encode("utf-8"))

