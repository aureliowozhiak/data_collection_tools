import pandas as pd
import requests

import sys
sys.path.append('../')

from src.model.extract.scraper import modelScraper
import os



tabletools_js = open('src/js/tabletools.js', 'r').read()

class viewScraper:
    

    def __init__(self):
        return None

    def table_scraping(input_value=None, tables=None, index=0):
        
        input_value = str(input_value)
        index = int(index)
        print(os.listdir())
        try:
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
