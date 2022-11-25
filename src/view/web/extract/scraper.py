import pandas as pd
import requests

import sys
sys.path.append('../')

from src.view.web.web_view import WebView
import os

try:
    tabletools_js = open('src/js/tabletools.js', 'r').read()
    html2js_js = open('src/js/html2js.js', 'r').read()
except:
    pass

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

    list_to_table : list
        A list with data content to create a table in page

    title : string
        The title of something

    list_of_paragraphs : list
        A lista with paragraph tags value <p>

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

    list_to_table(
        list_to_table, 
        title
    ):
        Return the html to create a page with a table containing the list content

    wikipedia_content(
        list_of_paragraphs
    )
        Convert a list with paragraphs text, in a html <p> components

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


        body += f"<h1>WebScraping</h1><p>Veja algumas das informações encontradas \
             na página <a href='{input_value}'>{dict_of_data['page_title']}</a>"

        body += '<div class="card-group">'

        count_links = len(dict_of_data['df_links'])
        if count_links > 0:
            body += WebView.add_card(title = f"{count_links} Links encontrados", 
            describe = "Veja todos os links &lt;a&gt que encontramos nessa página", 
            button_text = "Visualizar", 
            button_href = f"?scraper_type=links_scrapping&index=-1&input_value={input_value}")
            
            count_cards += 1

        count_all_paragraph_content = len(dict_of_data['all_paragraph_content'])
        if count_all_paragraph_content > 0:
            body += WebView.add_card(title = f"{count_all_paragraph_content} Paragráfos encontrados", 
            describe = "Veja o conteúdo dos pagráfos &lt;p&gt; que encontramos nessa página", 
            button_text = "Visualizar", 
            button_href = f"?scraper_type=p_scrapping&index=-1&input_value={input_value}")
            
            count_cards += 1

        count_all_key_content = len(dict_of_data['all_key_content'])
        if count_all_key_content > 0:
            body += WebView.add_card(title = f"{count_all_key_content} Listas de itens encontrados", 
            describe = "Veja o conteúdo das listas &lt;ul&gt;, &lt;ol&gt; e &lt;li&gt; que encontramos", 
            button_text = "Visualizar", 
            button_href = f"?scraper_type=key_content_scrapping&index=-1&input_value={input_value}")
            
            count_cards += 1
        body += '</div>'

        body += '</div></div><br>'
        
        body += '<br><div class="container">'
        
        if dict_of_data['wikipedia_content']:
            body += str(dict_of_data['wikipedia_content']['html'])
            body += '</div>'

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

    

    def list_to_table(list_to_table, title):
        df = pd.DataFrame(list_to_table, columns = [title])
        
        return f'<div class="container"><div class="row"><div class="col-sm"><script>{tabletools_js}</script> \
                    <br>\
                    <a href="#" onclick="download_table_as_csv(\'dataframe\');"><button type="button" class="btn btn-primary">Download as CSV</button></a> \
                     <br> <br> {df.to_html()} <br> \
                      <script type="text/javascript"> \
                        add_class_by_class(\'table\', \'dataframe\'); \
                    </script> \
                     </div></div></div>'

    def wikipedia_content(list_of_paragraphs, title, url):

        content = f'<script type="text/javascript"> \
            let element = document.evaluate("/html/body/div/nav", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); \
            element.singleNodeValue.remove(); </script>'

        content += f"<h1>{title}</h1>"

        content += f"<p><small><em>&lt;Texto extraído da página: <a href='{url}'>{url}</a>&gt;"

        content += f"<a href='" + f"?scraper_type=wikipedia&index=-1&input_value={url}'> Ver apenas o artigo</a></em></small></p>"
        
        for p_text in list_of_paragraphs:
            content += f"<p>{p_text}</p>"

        return content

