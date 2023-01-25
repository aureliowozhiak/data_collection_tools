import pandas as pd
import requests

import sys
sys.path.append('../src/')

from model.extract.scraper import modelScraper
#from view.web.extract.scraper import viewScraper
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

    extra_content : string
        Extra content to insert in html page

    Methods
    -------
    main(
        input_value=None, 
        scraper_type=None,
        index=0
    ):
        Organize the flow and decide which type of scraper we have

    wikipedia(
        html_soup, 
        input_value,
        extra_content
    )
        Controll the wikipedia page flow


    """

    def __init__(self):
        return None

    def main(input_value=None, scraper_type=None, index=0):
        
        input_value = str(input_value)
        scraper_type = str(scraper_type)
        index = int(index)

        if scraper_type == "table_scraping":
            return modelScraper.get_tables(input_value, index)
        
        
        def wikipedia(html_soup, input_value, extra_content=""):
            
            input_value = str(input_value.replace("pt.m.wikipedia", "pt.wikipedia"))
            page_content = modelScraper.get_data_from_page(input_value)
            html_soup = transformScraperData.html_parser(page_content)
            try:
                list_of_paragraphs = transformScraperData.get_all_paragraph_content(html_soup.find_all(class_="mw-content-container")[0])
                return list_of_paragraphs
                #return {
                #    'html' : extra_content + viewScraper.wikipedia_content(list_of_paragraphs, transformScraperData.page_title(html_soup), input_value),
                #    'list_of_paragraphs' : list_of_paragraphs
                #}
            except:
                return ''

        page_content = modelScraper.get_data_from_page(input_value)
        html_soup = transformScraperData.html_parser(page_content)
        df_links = transformScraperData.get_all_links(html_soup)
        if scraper_type == "wikipedia":
            extra_content = f'<script type="text/javascript"> \
            let element = document.evaluate("/html/body/div/nav", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); \
            element.singleNodeValue.remove(); </script>'
            return wikipedia(html_soup, input_value, extra_content)

        if scraper_type == "web_scraping":

            dict_of_data = {
                'df_links': df_links,
                'page_title': transformScraperData.page_title(html_soup),
                'all_paragraph_content' : transformScraperData.get_all_paragraph_content(html_soup),
                'all_key_content' : transformScraperData.get_all_key_content(html_soup),
                'wikipedia_content' : wikipedia(html_soup, input_value)
                }
            return dict_of_data
            #return {
            #        'html' : viewScraper.web_scraping(dict_of_data, input_value),
            #        'dict_of_data' : dict_of_data,
            #        'input_value' : input_value
            #        }


        if scraper_type == "links_scrapping":
            return df_links
            #return {
            #        'html': viewScraper.links(df_links),
            #        'df_links': df_links
            #        }

        if scraper_type == "p_scrapping":
            p_list = transformScraperData.get_all_paragraph_content(html_soup)
            return p_list
            #return {
            #        'html': viewScraper.list_to_table(p_list, 'paragraphs'),
            #        'p_list': p_list
            #}

        if scraper_type == "key_content_scrapping":
            key_content_scrapping_list = transformScraperData.get_all_key_content(html_soup)
            return key_content_scrapping_list
            #return {
            #        'html': viewScraper.list_to_table(key_content_scrapping_list, 'key_content'),
            #        'key_content_scrapping_list': key_content_scrapping_list
            #}

        return ""