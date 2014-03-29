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
    
    send_dict = {}
    user = None
    if 'username' in request.args:
        username = (request.args['username'])
        print username        
        user = connect_to_database().user.find_one({'_id': username})
        print user
        if user is None:
            send_dict['error'] = "requested username not found"
            return json.dumps(send_dict)
    else:
        send_dict['error'] = "param:username is required"
        return json.dumps(send_dict)    
    
    send_dict = {}
    
    print user
    
    send_dict['user'] = user
    return json.dumps(send_dict)

def is_diverse(list1,list2):
    for single_x in list2:
        if  single_x not in list1:
            return True
    return False





def add_connection():
    send_dict = {}
    single_user = None
    if 'username' in request.args:
        username = (request.args['username'])
        print username        
        single_user = connect_to_database().user.find_one({'_id': username})
        print single_user
        if single_user is None:
            send_dict['error'] = "requested username not found"
            return json.dumps(send_dict)
    else:
        send_dict['error'] = "param:username is required"
        return json.dumps(send_dict)    

    connection_username_single_user = None
    if 'follow' in request.args:
        username = (request.args['follow'])
        print username        
        connection_username_single_user = connect_to_database().user.find_one({'_id': username})
        print connection_username_single_user
        if connection_username_single_user is None:
            send_dict['error'] = "requested username not found"
            return json.dumps(send_dict)
    else:
        send_dict['error'] = "param:follow is required"
        return json.dumps(send_dict)    
    connection_username_single_user_temp = {}
    connection_username_single_user_temp['_id'] = connection_username_single_user['_id']
    connection_username_single_user_temp['name'] = connection_username_single_user['name']
    connection_username_single_user_temp['age'] = connection_username_single_user['age']        
    single_user['following'].append(connection_username_single_user_temp)    
    connection_username_single_user['followers'].append(username)    
    analyse_params = ['languages','department','industries','countries']    
    for each_param in analyse_params:         
        total_already  =  single_user['diversity'][each_param] * (single_user['total_following'])
        single_user['avg_connection_age']  =  ((single_user['avg_connection_age'] * (single_user['total_following'])) + connection_username_single_user['age'])/(single_user['total_following'] + 1)         
        if is_diverse(single_user[each_param],connection_username_single_user[each_param]):                
            single_user['diversity'][each_param] = (total_already + 1)/(len(single_user['following']) + 1)
        else:
            single_user['diversity'][each_param] = (total_already)/(len(single_user['following']) + 1)                        
    single_user['total_following'] += 1
    connection_username_single_user['total_followers'] += 1    
    connect_to_database().user.save(single_user)
    connect_to_database().user.save(connection_username_single_user)
    return json.dumps({'status':'success'})
    
    
    
    

def is_healthy():
    data = {'is_healthy':True,
            'message':''}    
    return json.dumps(data)

    