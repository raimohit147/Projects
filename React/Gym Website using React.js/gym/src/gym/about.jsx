import React from "react";
import aboutimage from "../images/about.png";
function About(){
    return(
        <div id="about">
            <div className="about-image">
                <img src={aboutimage} alt=""/>
            </div>
            <div className="about-text">
                <h1>LEARN MORE ABOUT US</h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis corrupti est, id ad laudantium sequi accusantium quam! Velit sapiente ea alias quae fugiat quo, ab, eum veritatis nisi enim nihil.</p>
                <button>READ MORE</button>
            </div>
        </div>
    )
}
export default About;