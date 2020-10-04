#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:02:51 2020

@author: thebooort
"""

import json

with open('/mnt/ca481456-7d8c-4eb7-9107-e33490f23afc/Documentos/Otros_Proyectos/cms2020-plots/data/processed-data.json') as json_file:
    data = json.load(json_file)

dictionary = {'name':'math fields','children':[], 'notation':0}

for element in data:
    if element['notation'][0][-1] == 'X':
        dictionary['children'].append({'name':element['prefLabel']['en'],'children':[],'notation':element['notation'][0]})
'''
for element in data:
    for key in dictionary['children']:
        if 'broader' in element.keys():
            if element['broader'][0]['notation'][0] == key['notation']:
                key['children'].append({'name':element['prefLabel']['en'],'children':[],'notation':element['notation'][0]})

for element in data:
    for key in dictionary['children']:
        for key2 in key['children']:
            if 'broader' in element.keys():
                if element['broader'][0]['notation'][0] == key2['notation']:
                    key2['children'].append({'name':element['prefLabel']['en'],'children':[],'notation':element['notation'][0]})

for element in data:
    for key in dictionary['children']:
        for key2 in key['children']:
            for key3 in key2['children']:
                if 'broader' in element.keys():
                    if element['broader'][0]['notation'][0] == key3['notation']:
                        key3['children'].append({'name':element['prefLabel']['en'],'children':[],'notation':element['notation'][0]})
'''
with open('final_data_1level.json', 'w') as outfile:
    json.dump(dictionary, outfile)