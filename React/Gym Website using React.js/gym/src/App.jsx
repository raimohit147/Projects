import React from "react";
import Navbar from "./gym/navbar";
import Header from "./gym/header";
import Feature from "./gym/feature";
import Offer from "./gym/offer";
import About from "./gym/about";
import Contact from "./gym/contact";

function App(){
      return(
        <div className="App">
      
          <Navbar/>
          <Header/>
          <Feature/>
          <Offer/>
          <About/>
          <Contact/>

        </div>
      )
}
 export default App