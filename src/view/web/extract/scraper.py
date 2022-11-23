import pandas as pd
import requests

import sys
sys.path.append('../')

from src.view.web.web_view import WebView
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
                return f'<div class="container"><script>{tabletools_js}</script> \
                    <br>\
                    <a href="#" onclick="download_table_as_csv(\'dataframe\');"><button type="button" class="btn btn-primary">Download as CSV</button></a> \
                     <br> <br> {table.to_html()} <br></div>'
            else:
                return f'This page has just {max} tables'
        except:
            return f'Tables not found'

    def web_scraping(dict_of_data, input_value):

        body = '<br><div class="container text-center">'

        body += ""

        count_cards = 0

        count_links = len(dict_of_data['df_links'])

        body += f"<h1>WebScraping</h1><p>Veja algumas das informações encontradas \
             na página <a href='{input_value}'>{dict_of_data['page_title']}</a>"

        body += '<div class="card-group">'
        if count_links > 0:
            body += WebView.add_card(title = f"{count_links} Links encontrados", 
            describe = "Veja todos os links que encontramos nessa página", 
            button_text = "Acessa lista dos links", 
            button_href = f"?scraper_type=links_scrapping&index=-1&input_value={input_value}")

            count_cards += 1

        body += '</div></div><br>'
        return body


    def links(df):
        return f'<div class="container"><script>{tabletools_js}</script> \
                    <br>\
                    <a href="#" onclick="download_table_as_csv(\'dataframe\');"><button type="button" class="btn btn-primary">Download as CSV</button></a> \
                     <br> <br> {df.to_html()} <br></div>'


