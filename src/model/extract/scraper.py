import pandas as pd
import requests


class Scraper:
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

    """

    def __init__(self):
        return None


    def get_generical_page(url_page = "https://pt.wikipedia.org/wiki/Python"):
        return requests.get(url_page)

    