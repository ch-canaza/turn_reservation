#!/usr/bin/env python3

from models.connectionpsql import db, app
from models.driverModel import DriverModel
from models.userModel import UserModel
from models.turnModel import TurnModel 
from flask import Flask, request, json

import urllib.request
#from main import create_Turn
import json


usrid = 5



@app.route('/turns/availability', methods=['GET'])
def turn_available():

    with urllib.request.urlopen('http://172.17.0.1:8001/turn/list_turns') as turns:
        turns_list = turns.read()

        turns_list = json.loads(turns_list)
        
        turns_taken = []
        for turn in turns_list['turns']:
            turns_taken.append(turn['turn_id'])

        #print(turns)

    with urllib.request.urlopen('http://172.17.0.1:8001/drivers/list_drivers') as drivers:
        drivers_list = drivers.read()

    drivers_list = json.loads(drivers_list)

    drivers_available = []
    for driver in drivers_list['drivers']:
        
        drivers_available.append(driver['id'])
        #print(i)
    print(f'drivers_avai {drivers_available}')

    ########################


    with urllib.request.urlopen('http://172.17.0.1:8001/users/list_users') as users:
        users_list = users.read()

    users_list = json.loads(users_list)

    users_registered = []
    for user in users_list['users']:
        users_registered.append(user['id'])
    print(f'user_regis {users_registered}')



    for id_pair in range(len(turns_taken)):
        
        print(id_pair)
        separate_id = turns_taken[id_pair].split('_')
        
        print(f' separate_id[0] {separate_id[0]}')
        
        #if int(separate_id[0]) in users_registered:
        if usrid in users_registered:
            
            #print(f'separate_id {separate_id}')
            print({"message":"ya tienes turno reservado"})
            return json.dumps({"message":"ya tienes turno reservado"})
            #break
        else:
            if int(separate_id[1]) not in drivers_available:
                
                #create_Turn()
                print({"message":"creando turno"})
                return json.dumps({"message":"creando turno"})
            
            else:

                return json.dumps({'message':"drivers ocupados"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




