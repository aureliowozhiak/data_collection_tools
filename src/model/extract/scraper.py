import pandas as pd
import requests


class modelScraper:
    """
    A class to do scraper in pages with specific (or not) parameters

    ---

    Attributes
    ----------
    url_page : string
        The url of page to run the http requests

    
    Methods
    -------
    get_generical_page(
        url_page = "https://pt.wikipedia.org/wiki/Python"
    ):
        Returns the request from the url passed. In this case we have a wikipedia page as default

    get_tables(
        url_page,
        index = None
    ):
        Return the tables found in the page in a dataframe
    """

    def __init__(self):
        return None


    def get_generical_page(url_page = "https://pt.wikipedia.org/wiki/Python"):
        return requests.get(url_page)

    def get_tables(url_page = "https://pt.wikipedia.org/wiki/Python", index = None):
        tables = pd.read_html(url_page)

        if index != None and index < len(tables):
            return tables[index]
        return tables