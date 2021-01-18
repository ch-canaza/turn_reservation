import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';


  
function Vehicle1() {
    
    const [availability, setColor] = useState('green');
    
    function selectTurn() {
        const newColor = availability === 'green' ? 'red' : 'green'
        setColor(newColor)
    }

    


    return (
        <div>
        <button style={{background:availability}} className='button_color' onClick = {()=>{selectTurn()}}>vehicle</button>
        </div>
);
};
export default Vehicle1;
