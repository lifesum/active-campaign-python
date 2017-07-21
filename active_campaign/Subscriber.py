import json
import urllib

from .ActiveCampaign import ActiveCampaign

import requests

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Subscriber(ActiveCampaign):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=subscriber_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urlencode(post_data)
        req = urllib.request.Request(request_url, post_data)
        response = json.loads(urllib.request.urlopen(req).read())
        return response

    def delete(self, params, post_data={}):
        request_url = '%s&api_action=subscriber_delete&api_output=%s&%s' % (
            self.url, self.output, params
        )
        response = json.loads(urllib.request.urlopen(request_url).read())
        return response

    def delete_list(self, params, post_data={}):
        request_url = '%s&api_action=subscriber_delete_list&api_output=%s&%s' % (
            self.url, self.output, params
        )
        response = json.loads(urllib.request.urlopen(request_url).read())
        return response

    def edit(self, params, post_data):
        request_url = '%s&api_action=subscriber_edit&api_output=%s&%s' % (
            self.url, self.output, params
        )
        post_data = urlencode(post_data)
        req = urllib.request.Request(request_url, post_data)
        response = json.loads(urllib.request.urlopen(req).read())
        return response

    def list_(self, params, post_data={}):
        request_url = '%s&api_action=subscriber_list&api_output=%s&%s' % (
            self.url, self.output, params
        )
        response = json.loads(urllib.request.urlopen(request_url).read())
        return response

    def paginator(self, params, post_data={}):
        request_url = '%s&api_action=subscriber_paginator&api_output=%s&%s' % (
            self.url, self.output, params
        )
        response = json.loads(urllib.request.urlopen(request_url).read())
        return response

    def sync(self, params, post_data):
        request_url = '%s&api_action=subscriber_sync&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        response = requests.post(request_url, data=post_data).json()
        return response

    def view(self, params, post_data={}):
        if params.startswith('email='):
            action = 'subscriber_view_email'
        elif params.startswith('hash='):
            action = 'subscriber_view_hash'
        elif params.startswith('id='):
            action = 'subscriber_view'
        else:
            action = 'subscriber_view'
        request_url = '%s&api_action=%s&api_output=%s&%s' % (self.url, action, self.output, params)
        response = json.loads(urllib.request.urlopen(request_url).read())
        return response
