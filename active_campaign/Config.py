from os import environ

try:
    ACTIVECAMPAIGN_URL = environ['ACTIVECAMPAIGN_URL']
    ACTIVECAMPAIGN_API_KEY = environ['ACTIVECAMPAIGN_API_KEY']
except KeyError:
    raise Exception('you must specify ACTIVECAMPAIGN_URL and ACTIVECAMPAIGN_API_KEY '
                    'as environment variables')
