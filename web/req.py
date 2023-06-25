#!/usr/bin/env python3

from flask import Flask, request
import requests
import re

VALID_URL_REGEX = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

app = Flask(__name__)

cache = {}


@app.route('/', methods=['GET'])
def get_website():
    website = request.args.get('website')

    if website in cache:
        return cache[website]

    try:
        data = make_website_request(website)

        cache[website] = data

        return data
    except Exception as err:
        return str(err), 400


def make_website_request(website: str):
    if website is None or re.match(VALID_URL_REGEX, website) is None:
        raise Exception('invalid website URL')

    res = requests.get(website)

    return res.text


if __name__ == '__main__':
    app.run()
