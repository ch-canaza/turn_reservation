from models.connectionpsql import db, app
from models.driverModel import DriverModel
from models.userModel import UserModel
from models.turnModel import TurnModel 
from flask import Flask, request
#from availability import drivers_fun
import urllib.request
#from main import create_Turn
import json

      
@app.route('/drivers/create', methods=['POST'])
def create_drivers():
    """
        #method that creates drivers
    """

    if request.is_json:
        data = request.get_json()
        new_driver = DriverModel(name=data['name'], placa=data['placa'])
        db.session.add(new_driver)
        db.session.commit()
        return {"message": f"driver {new_driver.name} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}


@app.route('/drivers/list_drivers', methods=['GET'])    
def get_all_drivers(): 
    """
        #method that retrieves a list of registred drivers
    """

    drivers = DriverModel.query.all()
    
    results = [
        {
            "id": driver.driver_id,
            "name": driver.name,
            "placa": driver.placa   ,
        } for driver in drivers
    ]    

    
    #return {"count": len((results)), "drivers": (results)}
    return {"drivers": (results)}

@app.route('/users/create', methods=['POST'])
def create_users():
    """
        #method that creates users
    """

    if request.is_json:
        data = request.get_json()
        new_user = UserModel(name=data['name'])
        db.session.add(new_user)
        db.session.commit()
        return {"message": f"user {new_user.name} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}


@app.route('/users/list_users', methods=['GET'])    
def get_all_users(): 
    """
        #method that retrieves a list of registred users
    """

    users = UserModel.query.all()
    #print(drivers)
    
    results = [
        {
            "id": user.user_id,
            "name": user.name
        } for user in users
    ]    

    return {"count": len((results)), "users": (results)}


@app.route('/turn/create', methods=['POST'])
def create_Turn():
    """
        #method that creates Turn
    """

    if request.is_json:
        data = request.get_json()
        #return (str(data))
        
        new_turn = TurnModel(driver_id=data['driver_id'],\
                             user_id=data['user_id'],\
                             date=data['date'],           
                             )
        
        db.session.add(new_turn)
        db.session.commit()
        
        return {"message": f"turn at {new_turn.date} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}


@app.route('/turn/list_turns', methods=['GET'])    
def get_all_turns(): 
    """
        #method that retrieves a list of turns booked
    """

    turns = TurnModel.query.all()
    #print(drivers)
    
    results = [
        {
            "date": turn.date,
            "turn_id": f'{turn.user_id}_{turn.driver_id}'
        } for turn in turns
    ]    

    return {"count": len((results)), "turns": (results)}

###############
"""
@app.route('/turns/availability', methods=['GET'])
def turn_available():

    with urllib.request.urlopen('http://0.0.0.0:8001/turn/list_turns') as turns:
        turns_list = turns.read()

        turns_list = json.loads(turns_list)
        
        turns_taken = []
        for turn in turns_list['turns']:
            turns_taken.append(turn['turn_id'])

        #print(turns)

    with urllib.request.urlopen('http://0.0.0.0:8001/drivers/list_drivers') as drivers:
        drivers_list = drivers.read()

    drivers_list = json.loads(drivers_list)

    drivers_available = []
    for driver in drivers_list['drivers']:
        
        drivers_available.append(driver['id'])
        #print(i)
    print(f'drivers_avai {drivers_available}')

    ########################


    with urllib.request.urlopen('http://0.0.0.0:8001/users/list_users') as users:
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
        
        if int(separate_id[0]) in users_registered:
            
            #print(f'separate_id {separate_id}')
            return({"message":"ya tienes turno reservado"})
            #break
        else:
            if int(separate_id[1]) not in drivers_available:
                
                #create_Turn()
                return({"message":"creando turno"})
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
