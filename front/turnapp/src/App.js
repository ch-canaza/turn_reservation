import React, { useState, useEffect } from 'react';
import DrivercardList from './DrivercardList';
import './App.css'
import axios from 'axios'


export default function App() {
  const [drivercards, setDrivercards] = useState([]);
  const [driverelement, setDataturns] = useState([])
  
  let name;
  let id;
  let plate;
  useEffect(() => {
    axios
      .get('http://0.0.0.0:8001/drivers/list_drivers')
      .then(res => {
        setDrivercards(res.data.drivers.map((driversItem, index) => {
          name = driversItem.name
          id = driversItem.id
          plate = driversItem.placa
          
          return {
            id: id,
            name: name,
            plate: plate
            
          }
          
        }))
        
      })
      
  },[]) 

    return (
      <div>
        <DrivercardList drivercards = {drivercards} />
      </div>
    );
  }
