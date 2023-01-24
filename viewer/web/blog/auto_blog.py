import pandas as pd
import requests
import markdown
import sys
sys.path.append('../')

class viewAutoBlog:
    
    def __init__(self):
        return None

    def home(post_content):
        body = "<br>"
        body += '<div class="container"><div class="card-group">'
        body += "<ul class='list-group list-group-flush'>"
        for post in post_content:
            body += f"<li class='list-group-item'><a href='../blog?theme={post}'>{post}</a></li>"
        body += "</ul>"
        return body

    def page(post_content):

        body = "<br>"
        body += '<div class="container"><div class="card-group">'
        body += f"<hr class='mt-3 mb-3'/><p>{markdown.markdown(post_content)}</p>"
        body += '</div></div>'
        return body

