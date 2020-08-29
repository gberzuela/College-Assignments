# Project3.py
#   The main module that uses MapQuest output from output_typing.py
#   and MapQuest API interaction from MapQuest_API.py
#
#   Handles user inputs and when to print
#
# ICS 32 - Alex Thornton
# Gerald Berzuela


import output_typing
import MapQuest_API


def number_of_address() -> int:
    ''' Returns the number of addresses to use '''
    return int(input())


def addresses(add_num: int) -> [str]:
    ''' Creates and returns a list of addresses to give to MapQuest '''
    addresses = []
    
    for i in range(add_num):
        addresses.append(input())

    return addresses


def number_of_outputs() -> int:
    ''' Returns the number of outputs user wishes to be printed '''
    return int(input())


def outputs_to_get(out_num: int) -> [str]:
    ''' Creates and returns a list of what outputs the user wishes to see '''
    outputs = []

    for i in range(out_num):
        outputs.append(input().upper())

    return outputs


def print_outputs(outputs: [str], json_response: dict):
    ''' Printing according to what the user wanted '''
    for i in range(len(outputs)):
        if 'STEPS' == outputs[i]:
            output_typing.steps.print_steps(json_response)
        elif 'TOTALDISTANCE' == outputs[i]:
            output_typing.totaldistance.print_distance(json_response)
        elif 'TOTALTIME' == outputs[i]:
            output_typing.totaltime.print_time(json_response)
        elif 'LATLONG' == outputs[i]:
            output_typing.latlong.print_latlong(json_response)
        elif 'ELEVATION' == outputs[i]:
            output_typing.elevation.print_elevation(json_response)
        

def main(debug = False) -> None:
    ''' User inputs '''
    if debug: # Testing purposes
        locations = ['564654', '98798798']
        outputs = ['ELEVATION', 'LATLONG', 'TOTALDISTANCE', 'TOTALTIME', 'STEPS']
    else:
        add_num = number_of_address()
        locations = addresses(add_num)
        out_num = number_of_outputs()
        outputs = outputs_to_get(out_num)

    ''' API interaction and printing '''    
    url = MapQuest_API.build_url(locations)
    
    ''' Program will end if there is any error with MapQuest '''
    json_response = MapQuest_API.build_response(url)
    if json_response is None:
        return
    
    print_outputs(outputs, json_response)


if __name__ == '__main__':
    main()
    print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
