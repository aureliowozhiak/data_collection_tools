import pandas as pd
import requests

import sys
sys.path.append('../src/')

from model.extract.scraper import modelScraper
from view.web.extract.scraper import viewScraper
from model.transform.transform_scraper_data import transformScraperData

class controllerScraper:
    """
    A class to consolidate the flow between model and view classes

    ---

    Attributes
    ----------
    input_value : string
        The main parameter to do the web scraper, usually the url of a website

    scraper_type : string
        The type of scraper, can be a full web scraping, a table scraping or another type (types in developing)
    
    index : string
        In some cases, we have the content index to find specific content


    Methods
    -------
    main(
        input_value=None, 
        scraper_type=None,
        index=0
    ):
        Organize the flow and decide which type of scraper we have

    


    """

    def __init__(self):
        return None

    def main(input_value=None, scraper_type=None, index=0):
        
        input_value = str(input_value)
        scraper_type = str(scraper_type)
        index = int(index)

        if scraper_type == "table_scraping":
            return {
                    'html' : viewScraper.table_scraping(input_value, modelScraper.get_tables(input_value), index)
                    }
        
        
        page_content = modelScraper.get_data_from_page(input_value)
        html_soup = transformScraperData.html_parser(page_content)
        df_links = transformScraperData.get_all_links(html_soup)

        if scraper_type == "web_scraping":

            dict_of_data = {
                'df_links': df_links,
                'page_title': transformScraperData.page_title(html_soup)
                }

            return {
                    'html' : viewScraper.web_scraping(dict_of_data, input_value),
                    'dict_of_data' : dict_of_data,
                    'input_value' : input_value
                    }


        if scraper_type == "links_scrapping":
            return {
                    'html': viewScraper.links(df_links),
                    'df_links': df_links
                    }

        return ""