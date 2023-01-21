import sys

sys.path.append('../')
from src.controller.extract.scraper import controllerScraper
from src.view.web.web_view import WebView
from src.controller.blog.tabnews import controllerTabNews
from src.controller.blog.auto_blog import controllerAutoBlog

from src.controller.another_tools.math import controllerMath

sys.path.append('web/')
header = open('src/header.html', 'r').read()

sys.path.append('../cherrypy/')
import cherrypy


"""
    App constructor using CherryPy module:
        Here we have all routes and pages flow
"""

class Root(object):

    @cherrypy.expose
    def index(self):
        return header + WebView.index()

class AboutPage:

    @cherrypy.expose
    def index(self):
        return header + controllerAutoBlog.home()
        #return header + controllerTabNews.home(user="aureliowozhiak", page="data-tools-ferramenta-em-desenvolvimento-para-trabalhar-com-dados-projeto-github")



class BlogPage:

    @cherrypy.expose
    def index(self, theme = None):
        return header + controllerAutoBlog.home(theme=theme)
        #return header + controllerTabNews.home(user="aureliowozhiak", page=page)

class Tools:
    def __init__(self):
        self.table_scraping = TableScraping()
        self.web_scraping = WebScraping()
        self.math = Math()

        self.scraper = ScraperTools()

    @cherrypy.expose
    def index(self):
        return "<script>window.location.replace('/');</script>"

class TableScraping:

    @cherrypy.expose
    def index(self):
        return header + WebView.table_scraping()

class WebScraping:

    @cherrypy.expose
    def index(self):
        return header + WebView.web_scraping()

class ScraperTools:

    @cherrypy.expose
    def index(self, input_value=None, scraper_type=None, index=0):
        return header + controllerScraper.main(input_value, scraper_type, index)['html']

class Search:
    @cherrypy.expose
    def index(self, search=None):
        return header + f"{search}"

class Math:
    @cherrypy.expose
    def index(self, input_value="2+2", math_type="calc_expression"):
        return header + WebView.math() + controllerMath.main(input_value=input_value, math_type=math_type)
            
root = Root()
root.about = AboutPage()

root.blog = BlogPage()

root.tools = Tools()

root.search = Search()

if __name__ == '__main__':
   #cherrypy.quickstart(root, '/', {'global': {'server.socket_host':'0.0.0.0','server.socket_port': 80}})
   cherrypy.quickstart(root, '/', {'global': {'server.socket_host':'127.0.0.1','server.socket_port': 80}})