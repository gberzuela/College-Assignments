# output_typing.py
#   Handles output classes and prints
#
# ICS 32 Spring 2017
# Gerald Berzuela


import MapQuest_API


class steps:
    def print_steps(json_response: 'json') -> None:
        ''' Iterates through the JSON dictionary to find and print the steps '''
        try:
            print('\nDIRECTIONS')
            for items in json_response['route']['legs']: 
                for obj in items['maneuvers']: 
                    print(obj['narrative'])

        except KeyError:
            print('NO ROUTE FOUND')


class totaldistance:
    def print_distance(json_response: 'json') -> None:
        ''' Simply prints the total distance of the journey '''
        try:
            print('\nTOTAL DISTANCE: ', end = '')
            print(str(round(json_response['route']['distance'])) + ' miles')

        except KeyError:
            print('NO ROUTE FOUND')


class totaltime:
    def print_time(json_response: 'json') -> None:
        '''
        Finds the total time which I saw to be in seconds,
        used integer division to convert to minutes
        '''
        try:
            print('\nTOTAL TIME: ', end = '')
            print(str(json_response['route']['time'] // 60) + ' minutes')

        except KeyError:
            print('NO ROUTE FOUND')


class latlong:
    def print_latlong(json_response: 'json') -> None:
        '''
        Finds lat and long withing the JSON response
        and formats to two decimal places
        '''
        try:
            print('\nLATLONGS')
            for items in json_response['route']['locations']:
                
                lat = float('{0:.2f}'.format(items['latLng']['lat']))
                lng = float('{0:.2f}'.format(items['latLng']['lng']))

                '''
                Checks to see if lat ot long is negative
                Gets absolute value and returns a string with
                correct cardinal direction
                '''
                if lat < 0 :
                    lat = str(abs(lat)) + ' S'
                else:
                    lat = str(lat) + ' N'
                    
                if lng < 0:
                    lng = str(abs(lng)) + ' W'
                else:
                    lng = str(lng) + ' E'
                    
                print(lat + ' ' + lng )

        except KeyError:
            print('NO ROUTE FOUND')
        

class elevation:
    def print_elevation(json_response: 'json') -> None:
        '''
        This function stores the latlongs of each location into a nested list
        It then sends each latlong to build the elevation URL and prints
        elevation individually.
        '''
        latlng = []
        
        try:
            for items in json_response['route']['locations']:
                latlng.append([items['latLng']['lat'], items['latLng']['lng']])

            print('\nELEVATIONS')
            for i in range(len(latlng)):
                elevation_URL = MapQuest_API.build_elevation_URL(latlng[i])
                elevation_json = MapQuest_API.build_response(elevation_URL)

                for items in elevation_json['elevationProfile']:
                    print(str(round(items['height'] * 3.28)))
                
        except KeyError:
            print('NO ROUTE FOUND')
        
