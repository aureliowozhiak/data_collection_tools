import pandas as pd
import requests

import sys
sys.path.append('../')

from src.view.web.web_view import WebView
import os


tabletools_js = open('src/js/tabletools.js', 'r').read()

class viewScraper:
    """
    A class to consolidate the html pages for the scraper modules

    ---

    Attributes
    ----------
    input_value : string
        The generic input value of the url parameter (informed in the html form)

    tables : list of dataframes
        The return from table scraping, this is a list with all dataframes founded

    index : int
        It's a index indentifier to find the item position

    dict_of_data : dict
        A dict with the return from the web scraping

    df_links : dataframe
        A dataframe with links found on the page in table format

    Methods
    -------
    table_scraping(
        input_value=None, 
        tables=None, 
        index=0
    ):
        Return the html to create a page with the table and a link to download the table found.

    
    web_scraping(
        dict_of_data, 
        input_value
    ):
        Return the html to create the web scraping page result. This page has a logic based in: 
            "just create the element if you find something"
    links(
        df_links
    ):
        Return the html to create a page with a table containing the links in the df_links

    """

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
                return f'<div class="container"><div class="row"><div class="col-sm"><script>{tabletools_js}</script> \
                    <script></script> \
                    <br>\
                    <a href="#" onclick="download_table_as_csv(\'dataframe\');"><button type="button" class="btn btn-primary">Download as CSV</button></a> \
                     <br> <br> {table.to_html()} <br></div> \
                        <script type="text/javascript"> \
                        add_class_by_class(\'table\', \'dataframe\'); \
                    </script></div></div>'
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


    def links(df_links):
        return f'<div class="container"><div class="row"><div class="col-sm"><script>{tabletools_js}</script> \
                    <br>\
                    <a href="#" onclick="download_table_as_csv(\'dataframe\');"><button type="button" class="btn btn-primary">Download as CSV</button></a> \
                     <br> <br> {df_links.to_html()} <br> \
                      <script type="text/javascript"> \
                        add_class_by_class(\'table\', \'dataframe\'); \
                    </script> \
                     </div></div></div>'


