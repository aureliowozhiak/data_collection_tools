import pandas as pd
import requests

import sys
sys.path.append('../')

from src.model.extract.scraper import modelScraper

sys.path.append('cherrypy/')
tabletools_js = open('src/js/tabletools.js', 'r').read()
class controllerScraper:
    

    def __init__(self):
        return None

    def main(input_value=None, scraper_type=None, index=0):
        
        
        scraper_type = str(scraper_type)
        input_value = str(input_value)
        index = int(index)

        if scraper_type == "table_scraping":
            try:
                return f'<script>{tabletools_js}</script> \
                    {modelScraper.get_tables(f"{input_value}")[index].to_html()} <br> \
                    <a href="#" onclick="download_table_as_csv(\'dataframe\');">Download as CSV</a>'
            except:
                return f'{input_value}'
        else:
            return ""