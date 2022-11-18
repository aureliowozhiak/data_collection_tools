import cherrypy
from src.view import View

import sys
sys.path.append('../')

from src.controller.extract.scraper import controllerScraper


sys.path.append('cherrypy/')

header = open('src\header.html', 'r').read()

class Root(object):

    @cherrypy.expose
    def index(self):
        return header + View.index()

class AboutPage:

    @cherrypy.expose
    def index(self):
        return header

class Tools:
    def __init__(self):
        self.table_scraping = TableScraping()

        self.scraper = ScraperTools()

    @cherrypy.expose
    def index(self):
        return "<script>window.location.replace('/');</script>"

class TableScraping:

    @cherrypy.expose
    def index(self):
        return header + View.table_scraping()

class ScraperTools:

    @cherrypy.expose
    def index(self, input_value=None, scraper_type=None, index=0):
        return controllerScraper.main(input_value, scraper_type, index)


root = Root()
root.about = AboutPage()

root.tools = Tools()

if __name__ == '__main__':
   cherrypy.quickstart(root, '/')