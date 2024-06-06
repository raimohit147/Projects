import React from "react"
import img from "../Images/services.jpg"
import Back from "../common/Back"
import "../home/featured/Featured.css"
import Featuredcard from "../home/featured/Featuredcard"

const Services = () => {
  return (
    <>
      <section className='services mb'>
        <Back name='Services' title='Services -All Services' cover={img} />
        <div className='featured container'>
          <Featuredcard />
        </div>
      </section>
    </>
  )
}

export default Services