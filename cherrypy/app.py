import cherrypy

header = open('src\header.html', 'r').read()

class Root(object):

    @cherrypy.expose
    def index(self):
        return header

class AboutPage:

    @cherrypy.expose
    def index(self):
        return header

root = Root()
root.about = AboutPage()

if __name__ == '__main__':
   cherrypy.quickstart(root, '/')