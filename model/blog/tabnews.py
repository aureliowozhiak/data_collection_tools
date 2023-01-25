import requests
import json

class modelTabNews:
    """
    A class to colect data from TabNews usign the API v1: https://www.tabnews.com.br/api/v1/contents/

    ---

    Attributes
    ----------
    user : string
        the username from TabNews profile

    slug : string
        part of url content, post identifier

    Methods
    -------
    get_content_from_user(
        user
    ):
        get all content published from an {user}

    get_content_from_slug(
        user, 
        slug
    ):
        get a specific content from an {user} by {slug}

    """

    
    def get_content_from_user(user):
        r = requests.get(f"https://www.tabnews.com.br/api/v1/contents/{user}")

        all_user_content = json.loads(r.text)

        
        post_content = []

        for content in all_user_content:
            if content['title'] and content['status'] == 'published':
                post_content.append(content)

        return post_content

    def get_content_from_slug(user, slug):
        r = requests.get(f"https://www.tabnews.com.br/api/v1/contents/{user}/{slug}")
        return json.loads(r.text)
