import pandas as pd
import requests

import sys
sys.path.append('../')

from src.model.extract.scraper import modelScraper

class controllerScraper:
    

    def __init__(self):
        return None

    def main(input_value=None, scraper_type=None, index=0):

        scraper_type = str(scraper_type)
        input_value = str(input_value)
        index = int(index)

        if scraper_type == "table_scraping":
            try:
                return f"{modelScraper.get_tables(f'{input_value}')[index].to_html()}"
            except:
                return f'{input_value}'
        else:
            return ""