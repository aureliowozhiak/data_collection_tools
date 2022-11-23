
class WebView:

    def index():
        return open('src/index.html', 'r').read()

    def table_scraping():
        return open('src/tools/table_scraping.html', 'r').read()

    def web_scraping():
        return open('src/tools/web_scraping.html', 'r').read()

    def add_card(title, describe, button_text, button_href):
        return f"""<div class="card" style="width: 18rem;">
            <!-- <img class="card-img-top" src="..." alt="Card image cap"> --> 
            <div class="card-body"> 
            <h5 class="card-title">{title}</h5>
            <p class="card-text">{describe}</p>
            <a href="{button_href}" class="btn btn-primary">{button_text}</a>
            </div>
        </div>"""