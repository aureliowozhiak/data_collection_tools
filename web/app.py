import sys

sys.path.append('../')
from src.controller.extract.scraper import controllerScraper
from src.view.web.web_view import WebView
from src.controller.blog.tabnews import controllerTabNews

sys.path.append('web/')
header = open('src/header.html', 'r').read()

sys.path.append('../cherrypy/')
import cherrypy


class Root(object):

    @cherrypy.expose
    def index(self):
        return header + WebView.index()

class AboutPage:

    @cherrypy.expose
    def index(self):
        return header

class ContactPage:

    @cherrypy.expose
    def index(self):
        return header + "<h1>Contact us</h1>"

class BlogPage:

    @cherrypy.expose
    def index(self, page = None):
        return header + controllerTabNews.home(user="aureliowozhiak", page=page)

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
        return header + WebView.table_scraping()

class ScraperTools:

    @cherrypy.expose
    def index(self, input_value=None, scraper_type=None, index=0):
        return controllerScraper.main(input_value, scraper_type, index)


root = Root()
root.about = AboutPage()
root.contact = ContactPage()

root.blog = BlogPage()

root.tools = Tools()

if __name__ == '__main__':
   cherrypy.quickstart(root, '/', {'global': {'server.socket_host':'0.0.0.0','server.socket_port': 8080}})