import React, { useState, useEffect } from 'react';
import DrivercardList from './DrivercardList';
import './App.css'
import axios from 'axios'


export default function App() {
  const [drivercards, setDrivercards] = useState(DRIVERS_LIST);
  
  return (
    <div>
      <DrivercardList drivercards = {drivercards} />
    </div>
  );
}


const DRIVERS_LIST = [
      {
          "id": 1,
          "name": "jairo",
          "placa": "hfks"
      },
      {
          "id": 3,
          "name": "alberto",
          "placa": "shfrg"
      },
      {
          "id": 5,
          "name": "josue",
          "placa": "jshbd"
      },
      {
          "id": 6,
          "name": "miguel",
          "placa": "fdgj"
      },
      {
          "id": 7,
          "name": "fernando",
          "placa": "dsfe"
      }
  ]

