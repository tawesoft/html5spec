from bs4 import BeautifulSoup
import itertools
import re
import types


pattern_keywords = re.compile(r'"[a-zA-Z0-9-]+"(; "[a-zA-Z0-9-]+")*')

# https://html.spec.whatwg.org/multipage/dom.html#global-attributes
global_attributes = [
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


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..., (sLast, None)"
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.zip_longest(a, b, fillvalue=None)

def dict_lastitems(xs):
    "xs -> (k0, v0, False), (k1, v1, False), ..., (kLast, vLast, True)"
    keys = pairwise(xs.keys())
    for key, key2 in keys:
        yield key, xs[key], key2 is None

def list_lastitems(xs):
    "xs -> (x0, False), (x1, False), ..., (xLast, True)"
    for x, y in pairwise(xs):
        yield x, y is None


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
        yield category


def gen_keywords(keywords):
    # "foo"; "bar"
    # KEYWORD: alphanumeric
    # "KEYWORD" [; "KEYWORD" [; ...]]
    if pattern_keywords.fullmatch(keywords):
        yield from map(lambda x: x.strip("\"").strip(), keywords.split(";"))


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
            yield i, desc.strip(), categories, attributes, children


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

        yield category, elements, exceptions
            


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
            value_desc += ". The actual rules are more complicated than indicated."
        value_keywords = set(gen_keywords(value_desc))

        elements = set(map(lambda x: x.strip(";\n "), gen_elements(elements)))
        yield attribute.strip(), elements, desc.strip(), value_desc, value_keywords


def parse_index_event_handlers(soup):
    rows = soup.find("table", {"id": "ix-event-handlers"}).findNext("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all(["th", "td"])
        cells = [x.get_text() for x in cells]
        assert len(cells) == 4

        attribute, elements, _, _ = cells

        yield attribute.strip(), elements.strip()


def parse_input_type_keywords(soup):
    rows = soup.find("table", {"id": "attr-input-type-keywords"}).findNext("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all(["th", "td"])
        cells = [x.get_text() for x in cells]
        keyword, *_ = cells

        yield keyword.strip()



def element_wrapper(element_name):
    """NOTE: Not injection safe"""
    def f(content):
        return "<%s>%s</%s>" % (element_name, content, element_name)
    return f


with open("indices.html") as fp:
    soup = BeautifulSoup(fp, "lxml")


elements = parse_index_elements(soup)
categories = parse_index_categories(soup)
attributes = parse_index_attributes(soup) # excl. event handlers
event_handlers = parse_index_event_handlers(soup)


with open("input.html") as fp:
    soup = BeautifulSoup(fp, "lxml")


input_type_keywords = set(parse_input_type_keywords(soup))



def is_simple_list(xs):
    return all([isinstance(v, str) for x in xs])

def pformat_list(xs, indent=0):
    t = "    "*indent

    yield t + "[\n"
    for value, last in list_lastitems(sorted(xs)):
        yield from pformat(value, indent+1)
        if not last: yield ","
        yield "\n"
    yield t + "]"

def pformat_dict(xs, indent=0):
    t = "    "*indent

    yield t + "{\n"
    for key, last in list_lastitems(sorted(xs.keys())):
        value = xs[key]
        yield t + "    %s:" % repr(key)
        if isinstance(value, str):
            yield " "
            yield repr(value)
        else:
            yield "\n"
            yield from pformat(value, indent+1)
        if not last: yield ","
        yield "\n"
    yield t + "}"


def pformat(xs, indent=0):
    if isinstance(xs, types.GeneratorType):
        yield from pformat(list(xs), indent)
    elif isinstance(xs, str):
        yield "    "*indent + repr(xs)
    elif isinstance(xs, dict):
        yield from pformat_dict(xs, indent)
    elif isinstance(xs, list):
        yield from pformat_list(xs, indent)
    elif isinstance(xs, set):
        yield from pformat_list(xs, indent)
    else:
        yield "    "*indent + str(type(xs)) + ":" + repr(xs)


def map_from_list_of_tuples(xs, kvfn):
    result = {}
    for x in xs:
        key, value = kvfn(x)
        result[key] = value
    return result


#for i in elements: print(i)
#for i in categories: print(i)
#for i in attributes: print(i)
#for i in event_handlers: print(i)
#for i in input_type_keywords: print(i)

r = {
    "elements": elements,
    "categories": categories,
    "attributes": attributes,
    "event_handlers": map_from_list_of_tuples(event_handlers, lambda i: (i[0], {'applies_to': i[1]})),
    "input_element_type_attribute_values": input_type_keywords,
}

print("".join(pformat(r)))


