import pandas as pd
from bs4 import BeautifulSoup


class transformScraperData:
    """
    A class to transform the data extract from scraper  

    ---

    Attributes
    ----------
    request_content : string
        All content from http request | get_generical_page().content

    html_soup : bs4.BeautifulSoup
        The return from html_parser()

    key : string
        A text value in a html element

    element_id : string
        An id from a html element


    Methods
    -------
    html_parser(
        request_content
    ):
        Process the bytes from request_content to html parsed version


    page_title(
        html_soup
    ):
        Get the text from tag <title> in html and return in a string

    get_all_links(
        html_soup
    ):
        Get all the links and their respective texts and generate a text/href dictionary sorted by index

    get_link_by_key(
        html_soup,
        key
    ):
        Receives a key and returns a list of all links found

    get_all_key_content(
        html_soup
    ):
        Returns all list item <ul>, <ol> and <li> content found in page

    get_all_paragraph_content(
        html_soup
    ):
        Returns all paragraph <p> content found in page

    get_value_by_id(
        html_soup,
        element_id
    ):
        Return an element by id
    


    """

    def __init__(self):
        return None

    def html_parser(request_content):
        return BeautifulSoup(request_content, 'html.parser')

    def page_title(html_soup):
        try:
            return html_soup.title.get_text()
        except:
            return ""
    
    def get_all_links(html_soup):
        links = {"text":[],"href":[]}

        for link in html_soup.find_all('a'):
            links["text"].append(link.get_text())
            links["href"].append(link.get('href'))

        df_links = pd.DataFrame()
        df_links["text"] = links["text"]
        df_links["href"] = links["href"]

        df_links = df_links.drop(df_links[df_links.href == "#"].index)
        df_links = df_links.drop(df_links[df_links.text == ""].index)
        df_links = df_links.reset_index()[['text', 'href']]

        return df_links

    def get_link_by_key(html_soup, key):
        links = transformScraperData.get_all_links(html_soup)

        result_links = []
        for text, href in zip(links['text'], links['href']):
            if key.replace(" ", "")  == text.replace(" ", ""):
                result_links.append(href)
                
        return result_links

    def get_all_key_content(html_soup):
        items = []
        for i in html_soup.find_all('ul') + html_soup.find_all('ol') + html_soup.find_all('li'):
            items = items + i.text.strip().split("\n")

        key_content = []
        for item in items:
            if item.replace(" ", "") != "":
                key_content.append(item.strip())

        return list(dict.fromkeys(key_content))
        
    def get_all_paragraph_content(html_soup):
        paragraph_content_list = []
        for phrase in html_soup.find_all('p'):
            phrase_clean = phrase.text.strip().replace("\n", "").replace("\t", "")
            if phrase_clean.replace(" ", "") != "":
                paragraph_content_list.append(phrase_clean)

        return list(dict.fromkeys(paragraph_content_list))

    #### NEEDS TO BE FINISHED
    def get_value_by_id(html_soup, element_id):
        return html_soup.find(id=element_id)

