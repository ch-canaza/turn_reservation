import React from 'react'
import Drivercard from './Drivercard';

export default function DrivercardList({ drivercards }) {
  return (
    <div className="card-grid">
      {drivercards.map(drivercard => {
        console.log(drivercard)
        return <Drivercard drivercard={drivercard} key={drivercard.name} />
      })}
    </div>
  )
}
