import pandas as pd
import requests
import markdown
import sys
sys.path.append('../')

class viewTabNews:
    
    def __init__(self):
        return None

    def home(post_content):
        body = "<br>"
        body += '<div class="container"><div class="card-group">'
        body += "<ul class='list-group list-group-flush'>"
        for post in post_content:
            body += f"<li class='list-group-item'><a href='../blog?page={post['slug']}'>{post['title']}</a></li>"
        body += "</ul>"
        return body

    def page(post_content):

        tabnews_list = f"https://www.tabnews.com.br/{post_content['owner_username']}/{post_content['slug']}"

        body = "<br>"
        body += '<div class="container"><div class="card-group">'
        body += f"<h1>{markdown.markdown(post_content['title'])}</h1><hr class='mt-3 mb-3'/><p>{markdown.markdown(post_content['body'])}</p>"
        body += '</div></div>'

        body += '<div class="container"><div class="card-group">'
        body += '<blockquote class="blockquote"><footer class="blockquote-footer">'
        body += f"<p><em>[Para ver o conteúdo na integra e interagir com esse post, acesse <a href='{tabnews_list}'>tabnews.com.br</a>]</em></p>"
        body += '</footer></blockquote>'

        body += '</div></div>'
        return body

