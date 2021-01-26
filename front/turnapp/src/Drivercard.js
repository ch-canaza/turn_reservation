import React, { useState, useEffect } from 'react'


export default function Drivercard({ drivercard }) {
    const [flip, setFlip] = useState(false)
    
    return (
        <div 
            className={`card ${flip ? 'flip' : ''}`}
            onClick={() => setFlip(!flip)}
            onClick={() => console.log('clickeando')}
        >
    
            <div className="front">
                {drivercard.name}

            </div>

            <div className="back">
               {drivercard.placa} is busy </div>
  
          
        </div>
    )
}
