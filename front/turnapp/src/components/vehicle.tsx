import React, { useState, useEffect } from 'react';


function Vehicle1() {
    
    const [availability, setColor] = useState('#38aa3c');
    const [drivers, setDrivers] = useState([]);
    
    function changeColor() {
        const newColor = availability === '#38aa3c' ? '#881b1b' : '#38aa3c'
        setColor(newColor)
    }
    
    useEffect(() => {
    const get_available = async () => {

        const response = await fetch('http://0.0.0.0:8002/turns/availability');

        const data = await response.json();

        interface MyObj {
            message: string;
        }
        
        // payload 
        let userData = null;

        try {
            // Parse a JSON
            userData = JSON.parse(data); 
        } catch (e) {
            // You can read e for more info
            // Let's assume the error is that we already have parsed the payload
            // So just return that
            userData = data;
        }

        // Now userData is the parsed result
        //console.log(userData)
        if (userData.message === "puedes crear turno") {
            console.log("ahora si estoy volando")
        }
                
    };
    get_available();

    },[]);
    
    

    return (
        <div className="select_driver">
        <button style={{background:availability}} className='button_color' onClick = {()=>{changeColor();}}>vehicle</button>
        </div>
);
};
export default Vehicle1;
