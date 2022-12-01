import pandas as pd
import requests
import sqlite3
            
DB_STRING = 'scraper_data.db'
            
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

    get_data_from_page(
        url_page
    ):
        Return the content from get_generical_page()
    """

    def __init__(self):
        return None

    def save_url_queried_in_database(url_page, scraper_type):
        with sqlite3.connect(DB_STRING) as dbc:
            dbc.execute("INSERT INTO url_queried (url_page, scraper_type) VALUES (?, ?)",
                        [url_page, scraper_type])


    def get_generical_page(url_page = "https://pt.wikipedia.org/wiki/Python"):
        return requests.get(url_page)

    def get_tables(url_page = "https://pt.wikipedia.org/wiki/Python", index = None):

        modelScraper.save_url_queried_in_database(url_page, 'table_scraping')

        tables = pd.read_html(url_page)

        try:
            if index != None and index < len(tables):
                return tables[index]
            return tables
        except:
            return []

    def get_data_from_page(url_page = "https://pt.wikipedia.org/wiki/Python"):

        return modelScraper.get_generical_page(url_page).content
         