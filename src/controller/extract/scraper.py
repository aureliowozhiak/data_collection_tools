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
                tables = modelScraper.get_tables(f"{input_value}")
                max = len(tables)

                if index <= 0:
                    index = max + 1

                if  max >= index:
                    table = tables[index - 1]
                    return f'<script>{tabletools_js}</script> \
                        {table.to_html()} <br> \
                        <a href="#" onclick="download_table_as_csv(\'dataframe\');">Download as CSV</a>'
                else:
                    return f'This page has just {max} tables'
            except:
                return f'Tables not found'
        else:
            return ""