import pandas as pd
import requests

import sys
sys.path.append('../src/')

from model.extract.scraper import modelScraper
from view.web.extract.scraper import viewScraper

class controllerScraper:
    

    def __init__(self):
        return None

    def main(input_value=None, scraper_type=None, index=0):
        
        input_value = str(input_value)
        scraper_type = str(scraper_type)

        if scraper_type == "table_scraping":
            return viewScraper.table_scraping(input_value, modelScraper.get_tables(f"{input_value}"), index)
        
        return ""