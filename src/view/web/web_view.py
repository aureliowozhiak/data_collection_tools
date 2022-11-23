
class WebView:

    def index():
        return open('src/index.html', 'r').read()

    def table_scraping():
        return open('src/tools/table_scraping.html', 'r').read()

    def web_scraping():
        return open('src/tools/web_scraping.html', 'r').read()