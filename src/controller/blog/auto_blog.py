
import sys
sys.path.append('../src/')

from model.blog.auto_blog import modelAutoBlog
from view.web.blog.auto_blog import viewAutoBlog

class controllerAutoBlog:
    
    def home(theme = []):

        if type(theme) != list:
            try:
                return viewAutoBlog.page(modelAutoBlog.get_content_from_theme(theme))
            except:
                return viewAutoBlog.home(modelAutoBlog.get_content_from_theme())
        else:
            return viewAutoBlog.home(modelAutoBlog.get_list_of_content())
