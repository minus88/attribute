import logging
import json
import os
from flask import request, url_for
import requests
from pymongo import MongoClient
import sys

DB_IP_ADDRESS = "127.0.0.1"
DB_PORT = 27017




def connect_to_database():
    client = MongoClient(DB_IP_ADDRESS, DB_PORT)    
    db = client.attributes
    return db


event_structure = {'start_time':'',
                   'end_time':'',
                   'event_name':'',
                   'purpose_tags':[],                  
                   'location':'',}

experience_structure = {'industry':'',
                        }


connection_structure = {'name':'',
                        'relationship':'',
                        'industry':'',
                        'languages':[],
                        'countries':[],
                        'experience':'',
                        'geography':'',
                        'meta':{'tie_strength':'',
                                'tags':'',},
                        }

    
example_connection = {'_id':'vignesh',
                      'name':'vignesh',
                      'country':'India',
                      'languages':['tamil', 'english'],
                      'connections': [{'name':'mike',
                                       'country':'India',
                                       'languages':['tamil', 'english'],
                                       'connections':[],
                                       'age':25}, 
                                      {'name':'john',
                                       'country':'canada',
                                       'languages':['tamil', 'english'],
                                       'connections':[],
                                       'age':25}],
                      'age':25}



def hello():
    print "test"    
    data = {'is_valid':False}
    return json.dumps(data)

def listUsers():
    usernames = []
    users = connect_to_database().user.find({})
    print users
    for each in users:
        print each
        usernames.append(each['_id'])
    return json.dumps(usernames)


def getUser():
    return json.dumps(example_connection)



def display_connection():
    return json.dumps(example_connection)


    
    
    

def is_healthy():
    data = {'is_healthy':True,
            'message':''}    
    return json.dumps(data)

    