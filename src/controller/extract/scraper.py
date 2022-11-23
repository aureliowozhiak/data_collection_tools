import pandas as pd
import requests

import sys
sys.path.append('../src/')

from model.extract.scraper import modelScraper
from view.web.extract.scraper import viewScraper
from model.transform.transform_scraper_data import transformScraperData

class controllerScraper:
    

    def __init__(self):
        return None

    def main(input_value=None, scraper_type=None, index=0):
        
        input_value = str(input_value)
        scraper_type = str(scraper_type)

        if scraper_type == "table_scraping":
            return viewScraper.table_scraping(input_value, modelScraper.get_tables(input_value), index)
        
        if scraper_type == "web_scraping":
            page_content = modelScraper.get_data_from_page(input_value)
            html_soup = transformScraperData.html_parser(page_content)

            dict_of_data = {
                'df_links': transformScraperData.get_all_links(html_soup),
                'page_title': transformScraperData.page_title(html_soup)
                }

            return viewScraper.web_scraping(dict_of_data, input_value)

        if scraper_type == "links_scrapping":
            page_content = modelScraper.get_data_from_page(input_value)
            html_soup = transformScraperData.html_parser(page_content)
            df_links = transformScraperData.get_all_links(html_soup)
            
            return viewScraper.links(df_links)

        return ""