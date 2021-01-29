import React, { useState } from 'react'


export default function Drivercard({ drivercard }) {
    let [flip, setFlip] = useState(false)

    const createTurn = () => {
        let d = new Date();
        let date = d.getDay() + '-' + d.getDate() + '-' + d.getFullYear();
        //console.log(date);
        
        if(!flip) {
            fetch('http://0.0.0.0:8002/turn/create', {
            method: 'POST',
            modde: 'cors',
            headers: {
                'Content-Type': 'application/json',
            },
        
            body: JSON.stringify({     
            
                driver_id: drivercard.id,
                user_id: 4,
                date: date
        
            }),
            
            })
            .then((res) => res.json())          
            .then(data => alert(data.message))
            .then(data => console.log(drivercard.id));
            
        }
        
      }


      const delete_turn = () => {
        
        if (flip){
            fetch('http://0.0.0.0:8001/turn/delete_turn/' + drivercard.id, {
            method: 'DELETE',
            
            })
            .then((res) => res.json())
            .then(data => alert(data.message))
            //.then(data => verifyMessage(data.message))
            .then(data => console.log(drivercard.id));
        }
      }
    
    /*const verifyMessage = message => {
        if (message === "ya tienes turno reservado, 4--['4', '1']") {
            flip = false
        }
    } */
   
    return (
        <div 
            className={`card ${flip ? 'flip' : ''}`}
            onClick={() => { setFlip(!flip); createTurn(); delete_turn() }}
            
           
        >
    
            <div className="front">
               <p> Driver: {drivercard.name}</p>
                    id: {drivercard.id}
            </div>

            <div className="back">
               You've selected plate #: {drivercard.plate} </div>
  
          
        </div>
    )
}
