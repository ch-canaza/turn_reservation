#!/usr/bin/env python3
from models.connectionpsql import db, app
from models.driverModel import DriverModel
from models.userModel import UserModel
from models.turnModel import TurnModel 
from flask import Flask, request, json

import urllib.request
#from main import create_Turn
import json

    

#@app.route('/turns/availability', methods=['GET'])
#def turn_available():

@app.route('/turn/create', methods=['POST'])
def create_Turn():

    """
        method that creates Turn
    """

    if request.is_json:
        data = request.get_json()
        #return (str(data))
        
        new_turn = TurnModel(driver_id=data['driver_id'],\
                            user_id=data['user_id'],\
                            date=data['date'],           
                            )
        
        ############3 Available #############

        driver_id = int(data['driver_id'])
        user_id = int(data['user_id'])

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


        available = False
        for id_pair in range(len(turns_taken)):
            
            print(id_pair)
            separate_id = turns_taken[id_pair].split('_')
            
            print(f' separate_id[0] {separate_id[0]}')
            
            #if int(separate_id[0]) in users_registered:
            if user_id == int(separate_id[0]): # and user_id in users_registered:
                
                    print({"message":"ya tienes turno reservado"})
                    return json.dumps({"message":f'ya tienes turno reservado, {user_id}--{separate_id}'})
                
            else:
                if user_id not in users_registered:   
                    return json.dumps({"message": f'you are not a valid user{users_registered}'})

                else:
                    
                    
                    if driver_id == int(separate_id[1]): # and driver_id in drivers_available:
                    
                        return json.dumps({'message':f'driver ocupado {drivers_available}'})
                        
                    else:
                        if driver_id in drivers_available: 
                            #drivers_available.pop(driver_id)
                            #return str(driver_id)
                            #return json.dumps({"message": "available"})
                            available = True 
                            #return json.dumps({"message": "creando turno"})
                                    
                    
                        else:
                            return json.dumps({"message": f'driver not in db{drivers_available}{driver_id}'})

            
            
            
            
            ########################
        if available == True:

            db.session.add(new_turn)
            db.session.commit()
            
            return {"message": f"turn at {new_turn.date} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




