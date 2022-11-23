
import sys
sys.path.append('../src/')

from model.blog.tabnews import modelTabNews
from view.web.blog.tabnews import viewTabNews

class controllerTabNews:

    def home(user, page):

        if page:
            return viewTabNews.page(modelTabNews.get_content_from_slug(user, page))
        else:
            return viewTabNews.home(modelTabNews.get_content_from_user(user))
