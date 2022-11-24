
class WebView:

    """
    A class to build html pages

    ---

    Attributes
    ----------
    title : string
        Title of content

    describe : string
        Describe of content

    button_text : string
        Button text of content

    button_href : string
        Button href to link the content with another page

    Methods
    -------
    index():
        return the 'src/index.html' content file
        
    about():
        return the 'src/about.html' content file
        
    table_scraping():
        return the 'src/tools/table_scraping.html' content file
        
    web_scraping():
        return the 'src/tools/web_scraping.html' content file

    add_card(
        title,
        describe,
        button_text,
        button_href
    ):
        Returns an html card based on given parameters
    
    """

    def index():
        return open('src/index.html', 'r').read()

    def about():
        return open('src/about.html', 'r').read()

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