from lxml import etree
from io import StringIO


def get_html_root(html_doc):
    f = StringIO(html_doc)
    parser = etree.HTMLParser()
    tree = etree.parse(f, parser)
    root = tree.getroot()
    return root


def find_div_contains_class(xml_element, class_name):
    expr_class = ".//div[contains(@class, '{}')]".format(class_name)
    results = xml_element.xpath(expr_class)
    return results


def find_div_by_class(xml_element, class_name):
    expr_class = ".//div[@class='{}']".format(class_name)
    results = xml_element.xpath(expr_class)
    return results


def find_span_contains_text(xml_element, text):
    expr_span = ".//span[contains(text(), '{}')]".format(text)
    results = xml_element.xpath(expr_span)
    return results


