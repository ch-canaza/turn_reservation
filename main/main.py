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
            "turn_id": f'{turn.user_id}_{turn.driver_id}',
            "driver_id": turn.driver_id
        } for turn in turns
    ]    

    return {"count": len((results)), "turns": (results)}

@app.route('/turn/delete_turn/<driver>', methods=['DELETE'])
def delete_turn(driver):
    """ 
        deletes a turn based on its time
        only can delete turns before 30 seconds created
    """
    turn = TurnModel.query.get(driver)
    #turn = turns.query.get(turn_id)
    db.session.delete(turn)
    db.session.commit()
   
    return {"mesaage": "turn deleted succesfuly"}



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
