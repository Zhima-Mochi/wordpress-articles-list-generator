import requests
import re
from datetime import datetime
import os


def main():
    url = os.getenv('url')
    cookie = os.getenv('cookie')

    r = requests.get(url, headers={'cookie': cookie})

    f = open(
        f"/output/articles_list_{'_'.join(datetime.now().ctime().split(' '))}", "w")
    for m in re.finditer(r'inline_[0-9]+?(.*?\n)*?.*?post_title">(?P<post_title>.*?)</div>'
                         r'(.*?\n)*?.*?post_name\">(?P<post_name>.*?)</div>'
                         r'(.*?\n)*?.*?post_author\">(?P<post_author>.*?)</div>'
                         r'(.*?\n)*?.*?comment_status\">(?P<comment_status>.*?)</div>'
                         r'(.*?\n)*?.*?ping_status\">(?P<ping_status>.*?)</div>'
                         r'(.*?\n)*?.*?_status\">(?P<_status>.*?)</div>'
                         r'(.*?\n)*?.*?jj\">(?P<d>.*?)</div>'
                         r'(.*?\n)*?.*?mm\">(?P<m>.*?)</div>'
                         r'(.*?\n)*?.*?aa\">(?P<Y>.*?)</div>'
                         r'(.*?\n)*?.*?hh\">(?P<H>.*?)</div>'
                         r'(.*?\n)*?.*?mn\">(?P<M>.*?)</div>'
                         r'(.*?\n)*?.*?ss\">(?P<S>.*?)</div>'
                         r'(.*?\n)*?.*?view(.*?\n)*?.*?href=\"(?P<url>.*?)\"', r.text):
        f.write(
            f"title: {m.group('post_title')} status: {m.group('ping_status')} src: {m.group('url')}\n")
    f.close()
