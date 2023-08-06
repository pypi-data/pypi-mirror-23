"""
content_list
"""
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import requests


from jinja2 import Environment, FileSystemLoader
ENV = Environment(
    #loader=PackageLoader('inv_content_list', 'templates'),
    loader=FileSystemLoader(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates'))
)


URL = 'https://inv999abc.docebosaas.com'
CLIENT_ID = 'acaspike'
CLIENT_SECRET = 'e06504ec7b8e8a8696ccc83f942445d5c2752fcc'

def get_api_token():
    """

    :return:
    """
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='%s/oauth2/token' % URL,
                              client_id=CLIENT_ID,
                              client_secret=CLIENT_SECRET)
    return token['access_token']


def get_course_list():
    """

    :return:
    """
    post_data = {'access_token': get_api_token()}
    response = requests.post('https://inv999abc.docebosaas.com/api/course/courses', data=post_data)
    content = response.content
    import json
    dct = json.loads(content)
    return dct


def display_content_list(template_file):
    """

    :param template_file:
    :return:
    """
    context = get_course_list()['courses']
    template = ENV.get_template(template_file)
    return template.render(content=context)
