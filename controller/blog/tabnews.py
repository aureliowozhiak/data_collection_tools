
import sys
sys.path.append('../src/')

from model.blog.tabnews import modelTabNews
from view.web.blog.tabnews import viewTabNews

class controllerTabNews:
    """
    A class to controller the Blog based on TabNews API v1

    ---

    Attributes
    ----------
    user : string
        A valid TabNews username

    page : string
        A page indentifier (slug)


    Methods
    -------
    home(
        user, 
        page
    ):
    This blog is based on just one page, with this rule:
            if the page parameter is valid then it creates a post page
            else: it creates a home page listing all posts

    """
    def home(user, page):

        if page:
            try:
                return viewTabNews.page(modelTabNews.get_content_from_slug(user, page))
            except:
                return viewTabNews.home(modelTabNews.get_content_from_user(user))
        else:
            return viewTabNews.home(modelTabNews.get_content_from_user(user))
