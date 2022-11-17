import pandas as pd
from bs4 import BeautifulSoup


class TransformScraperData:
    """
    A class to transform the data extract from scraper  

    ---

    Attributes
    ----------
    request_content : string
        All content from http request | get_generical_page().content

    html_soup : bs4.BeautifulSoup
        The return from html_parser()


    Methods
    -------


    """

    def __init__(self):
        return None

    def html_parser(request_content):
        return BeautifulSoup(request_content, 'html.parser')

    def page_title(html_soup):
        return html_soup.title.get_text()
    
    def get_all_links(html_soup):
        links = {"text":[],"href":[]}

        for link in html_soup.find_all('a'):
            links["text"].append(link.get_text())
            links["href"].append(link.get('href'))

        return links
