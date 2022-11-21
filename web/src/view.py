
class View:

    def index():
        return open('src/index.html', 'r').read()

    def table_scraping():
        return open('src/tools/table_scraping.html', 'r').read()