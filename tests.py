from flask import Flask
import logging
from pymongo import MongoClient

DB_IP_ADDRESS = "127.0.0.1"
DB_PORT = 27017


cities = ['delhi', 'cairo', 'geneva', 'berth', 'new york', 'hawaii', 'paris', 'london', 'los angeles', 'tokyo', 'chicago', 'san francisco', 'berlin', 'rome', 'barcelona', 'amsterdam', 'miami', 'hong kong', 'sydney', 'madrid', 'boston', 'las vegas', 'toronto', 'washington dc', 'florida', 'bangkok', 'beijing', 'milan', 'detroit', 'california', 'washington', 'frankfurt', 'dubai', 'shanghai', 'atlanta', 'moscow', 'singapore', 'philadelphia', 'brussels', 'virginia', 'seattle', 'melbourne', 'san diego', 'texas', 'dallas', 'florence', 'buenos aires', 'venice', 'istanbul', 'stockholm']
countries = ['india', 'england', 'canada', 'australia', 'new zealand', 'south africa', 'france', 'ireland', 'germany', 'japan', 'china', 'pakistan', 'spain', 'united kingdom', 'italy', 'united states', 'usa', 'singapore', 'malaysia', 'sri lanka', 'bangladesh', 'mexico', 'thailand', 'brazil', 'philippines', 'indonesia', 'argentina', 'hong kong', 'uk', 'portugal']
company = ['ibm', 'microsoft', 'google', 'shell', 'tata', 'nortel', 'hp', 'cisco', 'oracle', 'apple', 'vmware', 'citrix', 'adobe', 'comptia', 'sun', 'emc', 'dell', 'juniper', 'ciw', 'checkpoint', 'symantec', 'intel', 'pmi', 'exin', 'novell', 'sony', '3com', 'lpi', 'samsung', 'sap', 'linux', 'avaya', 'nokia', 'lotus', 'toshiba', 'isc', 'cognos', 'yahoo', 'fujitsu', 'acer', 'netapp', 'lenovo', 'blackberry', 'iseb', 'asus', 'cwnp', 'eccouncil']
department = ['finance', 'marketing', 'business', 'technology', 'management', 'insurance', 'shopping', 'automotive', 'accounting', 'sales', 'retail', 'healthcare', 'it', 'computers', 'advertising', 'economics', 'science', 'politics', 'legal', 'investing', 'law', 'lifestyle', 'arts', 'technology', 'world', 'religion', 'environment', 'finance', 'society', 'culture', 'shopping', 'economy', 'gaming', 'health', 'philosophy', 'food', 'automotive', 'people', 'travel', 'humor', 'opinion', 'family', 'relationships', 'art', 'marketing', 'psychology', 'us', 'government', 'hobbies', 'crime', 'recreation', 'pets', 'beauty', 'literature', 'fashion', 'national', 'nature', 'writing', 'reference', 'weather', 'media', 'insurance', 'film', 'local']
languages = ['tamil', 'english', 'french', 'spanish', 'german', 'italian', 'japanese', 'chinese', 'russian', 'korean', 'portuguese', 'hindi', 'arabic', 'dutch', 'greek', 'polish', 'thai', 'turkish', 'swedish', 'telugu', 'indian', 'vietnamese', 'danish', 'czech']
industries = ['petroleum', 'manufacturing', 'automation', 'software', 'energy', 'aerospace', 'life sciences', 'pharmaceutical', 'automotive', 'healthcare', 'government', 'retail', 'financial services', 'construction', 'consumer goods', 'semiconductor', 'insurance', 'defence', 'transportation', 'technology', 'telecommunications', 'electronics', 'medical devices', 'chemicals', 'mining', 'finance', 'law', 'food beverage', 'business services', 'industrial equipment', 'shipbuilding', 'chemical']
first_names = ['michael', 'sam', 'steven', 'andrea', 'chris', 'sarah', 'john', 'tom', 'jeff', 'david', 'ashley', 'james', 'alex', 'kelly', 'laura', 'robert', 'matt', 'daniel', 'victoria', 'jennifer', 'kenneth', 'brian', 'greg', 'peter', 'andrew', 'mark', 'lauren', 'ben', 'courtney', 'mel', 'rachel', 'jessica', 'nick', 'damien', 'richard', 'joe', 'joseph', 'vignesh', 'abdul', 'mohammed', 'ram', 'melhores', 'mundo', 'climber', 'do', 'klimber', 'populares', 'jaja', 'os', 'salim', 'afy', 'naz', 'sammie', 'asif', 'yahya', 'zakir', 'zorra', 'josef']
last_names = ['belfort', 'hobart', 'fish', 'sidduqe', 'arafat', 'gupta', 'thakur', 'jain', 'saxena', 'singh', 'mishra', 'goldman', 'stalin', 'bush', 'bieden', 'lenin', 'marx', 'mao', 'radyo', 'engels', 'revolusjon', 'teori', 'demokrati', 'bush', 'bieden', 'doorsturen', 'afdrukken', 'bewaren']



user_obj = {'_id':'vignesh',
                      'name':'vignesh',
                      'cities':['chennai'],
                      'countries':['India'],
                      'languages':['tamil', 'english'],
                      'companies':[],   
                      'department':[],
                      'industries':[],
                      'following': [],
                      'followers':[],
                      'diversity':{'languages':0.0,
                                   'department':0.0,
                                   'industries':0.0,                                   
                                   'countries':0.0,},
                      'avg_connection_age':0,
                      'total_following':0,
                      'total_followers':0,
                      'age':25}
import random

def get_random(list1):
    index = random.randint(0,len(list1)-1)
    return list1[index]

def get_random_sublist(list1):
    sublist = []
    count = random.randint(1,4)
    for i in range(0,count):
        single = get_random(list1)
        sublist.append(single)
    return sublist



def add_random_user():
    single_user = user_obj    
    userid = random.randint(100,999)
    first_name = get_random(first_names)
    last_name = get_random(last_names)
    single_user['age'] = random.randint(18,65)     
    single_user['_id'] = '%s%d' % (first_name,userid)
    single_user['cities'] = get_random_sublist(cities)
    single_user['name'] = "%s %s" % (first_name,last_name)
    single_user['countries'] = get_random_sublist(countries)
    single_user['company'] = get_random_sublist(company)
    single_user['languages'] = get_random_sublist(languages)
    single_user['department'] = get_random_sublist(department)
    single_user['industries'] = get_random_sublist(industries)
    print single_user['_id']
    db = connect_to_database()
    users = db.user    
    try:    
        usr_obj_id = users.insert(single_user)
    except:
        print 'Collision ignored'
    return single_user


def populate_users():
    user_names = []    
    for i in range(1,200):         
        username = add_random_user()['_id']        
        user_names.append(username)    
    for each_user in user_names:
        for i in range(1,random.randint(2,40)):
            to_connect = get_random(user_names)
            if to_connect == each_user:
                continue        
            add_connection(each_user,to_connect)
        
        single_user = connect_to_database().user.find_one({'_id': each_user})
        print "--"*20
        print single_user
        
                          
def add_connection(username,connection_username):
    
    single_user = connect_to_database().user.find_one({'_id': username})
    connection_username_single_user = connect_to_database().user.find_one({'_id': connection_username})
    connection_username_single_user_temp = connection_username_single_user
    
    
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
    
        
    return True
    

def is_diverse(list1,list2):
    for single_x in list2:
        if  single_x not in list1:
            return True
    return False





def connect_to_database():
    client = MongoClient(DB_IP_ADDRESS, DB_PORT)    
    db = client.attributes
    return db



print 'Hello'

connect_to_database().user.remove({})

populate_users()



quit()


list = [1, 2, 4, 5, 6]

print list

for each in list:
    print each
    
a = 'vignesh'

for each in a:
    print each

    
list_of_names = ['michael', 'joseph', 'john', 'james', 'david']

for e in list_of_names:
    print e
    
example_connection = {'name':'vignesh',
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

print example_connection['name']
print example_connection['connections'][1]['country']

     
db = connect_to_database()
users = db.user        
usr_obj_id = users.insert(example_connection)
print usr_obj_id






    
