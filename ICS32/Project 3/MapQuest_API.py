# MapQuest_API.py
#   Builds the url with given locations and gets JSON response
#
# ICS 32 Spring 2017
# Gerald Berzuela


import json
import urllib.parse
import urllib.request


MAPQUEST_KEY = 'tC4t3zuRuEfjE3gxmCdibIsVh2OLNNUF'
MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?'
ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'


def build_url(addresses = [str]) -> str:
    '''
    Builds a list of tuples to encode for the URL
    The list is initialized with the key and first address for URL format
    '''
    URL_parameters = [('key', MAPQUEST_KEY), ('from', addresses[0])]

    for i in range(1, len(addresses)):
        URL_parameters.append(('to', addresses[i]))

    return MAPQUEST_URL + urllib.parse.urlencode(URL_parameters)


def build_response(url: str) -> 'json':
    ''' Takes URL and returns the parsed JSON reponse as a dictionary '''
    response = None
    
    try:
        response = urllib.request.urlopen(url)
        json_response = response.read().decode(encoding = 'utf-8')
        return json.loads(json_response)

    except urllib.error.URLError:
        print('MAPQUEST ERROR')
        return None

    finally:
        if response != None:
            response.close()


def build_elevation_URL(latlong: [float]) -> str:
    '''
    Similar to build_url() - This function takes in a list consisting of
    latlong info from previously accessed json_response
    '''
    URL_parameters = [('key', MAPQUEST_KEY), ('shapeFormat', 'raw'), ('latLngCollection', ','.join(str(item) for item in latlong))]

    return ELEVATION_URL + urllib.parse.urlencode(URL_parameters)




