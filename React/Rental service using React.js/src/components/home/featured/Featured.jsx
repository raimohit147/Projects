import React from 'react'
import "./Featured.css"
import Featuredcard from './Featuredcard'
import Heading from '../../common/Heading'


const Featured = () => {
  return (
    <> <section className='featured background'>
    <div className='container'>
      <Heading title='Featured Property Types' subtitle='Find All Type of Property.' />
      <Featuredcard />
    </div>
  </section>
    </>
  )
}

export default Featured
