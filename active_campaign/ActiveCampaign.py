from .Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from .Connector import Connector

import active_campaign


class ActiveCampaign(Connector):
    def __init__(self, url, api_key, api_user='', api_pass=''):
        self.url = url
        self.api_key = api_key
        Connector.__init__(self, url, api_key, api_user, api_pass)

    def api(self, path, post_data={}):
        # IE: "subscriber/view"
        components = path.split('/')
        component = components[0]

        if '?' in components[1]:
            # query params appended to method
            # IE: subscriber/edit?overwrite=0
            method_arr = components[1].split('?')
            method = method_arr[0]
            params = method_arr[1]
        else:
            # just a method provided
            # IE: "subscriber/view
            if components[1]:
                method = components[1]
                params = ''
            else:
                return 'Invalid method.'

        # adjustments
        if component == 'branding':
            # reserved word
            classname = 'Design'

        elif component == 'sync':
            classname = 'Subscriber'
            method = 'sync'

        elif component == 'singlesignon':
            classname = 'Auth'

        else:
            classname = component.capitalize()

        module = getattr(active_campaign, classname)
        factory = getattr(module, classname)
        endpoint = factory(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY)

        if method == 'list':
            # reserved word
            method = 'list_'

        if method in dir(endpoint):
            return getattr(endpoint, method)(params, post_data)

        raise Exception('endpoint not yet implemented')
