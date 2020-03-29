import os
import sys
import requests
from lxml import etree
from io import StringIO
import argparse

BASE_PATH = os.path.dirname(os.path.realpath(__file__).rpartition('/')[0])
sys.path.append(BASE_PATH)

from utils import parser as p
from utils import alerts as a


AWS_URL = "https://www.amazon.com.au/s?k={}"


def run(search_keywords=["toilet", "paper"], brands=["Quilton"]):
    search_str = "+".join(search_keywords)
    url = AWS_URL.format(search_str)
    print("Searching {}".format(url))

    sess = requests.Session()
    sess.headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"
    res = sess.get(url)
    search_results = get_search_results_section(res.text)
    is_found, results = find_keywords_in_results(search_results, keywords=brands)

    if is_found:
        print("Found matched results.")
        alert("Found {}! Please wipe freely!".format(" ".join(search_keywords)))
    else:
        print("No matched result found.")
        #alert("No {} found. Please regulate your current usage.".format(" ".join(search_keywords)))

    return is_found, results


def get_search_results_section(html_doc):
    root = p.get_html_root(html_doc)
    sections = p.find_div_contains_class(root, 's-search-results')
    if len(sections) > 0:
        return sections[0]


def find_keywords_in_results(section, keywords=["Quilton"]):
    is_keyword = False
    results = []
    rows = p.find_div_by_class(section, 'sg-row')
    print('Found {} result rows'.format(len(rows)))
    for row in rows:
        for kw in keywords:
            res = p.find_span_contains_text(row, kw)
            results.extend(res)
    if len(results) > 0:
        is_keyword = True

    return is_keyword, results


def alert(message):
    a.voice_alert(message)


def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--keywords", help="Keywords to search on AWS AU; seperated by space")
    arg_parser.add_argument("--brands", help="Brands to focus on search results; seperated by space")
    args = arg_parser.parse_args()
    return args


def main():
    args = parse_args()
    if not args.keywords:
        search_keywords = ["toilet", "paper"]
    else:
        search_keywords = args.keywords.split(" ")
    if not args.brands:
        brands = ["Quilton"]
    else:
        brands = args.brands.split(" ")
    is_found, results = run(search_keywords, brands)


if __name__ == "__main__":
    main()



