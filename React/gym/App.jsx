//import { useState , useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
// import React from 'react'
// //import Searchbox from './weather/search.jsx'
// //import Sideeffect from './handling'
// //import Info from './weather/info.jsx'
// import WeatherApp from './weather/weather.jsx'
// function  App()
//   {
//    return(
//     <>
//  <WeatherApp></WeatherApp>
//     </>
//  )
//  }
// export default App
// // import Pro from'./productlib.jsx'
// import Todo from'./123.jsx'
// import NoteContext from './usecontext.jsx'
// import About from'./blog'
// import Nodestate from './notestate.jsx'
// import Home from './home'
// import About from './about1'
// import React from "react";
// import {
//   BrowserRouter as Router,
//   Routes,
//   Route,
//   Link
// } from "react-router-dom";

// export default function App() {
//   return (
//     <>
//     <Router>
// {     
//       <div>
//         <nav>
//           <ul>
//             <li>
//               <Link to="/">Home</Link>
//             </li>
//             <li>
//               <Link to="/about">About</Link>
//             </li>
//             <li>
//               <Link to="/users">Users</Link>
//             </li>
//           </ul>
//         </nav> */}

//         {/* A <Switch> looks through its children <Route>s and
//             renders the first one that matches the current URL. */}
 //         <Routes>
//           <Route path="/about1">
//             <About />
//           </Route>
//           <Route index >
//             <Home />
//           </Route>
//         </Routes>
      
//     </Router></> 
//   );
// }


// function Home() {
//   return <h2>Home</h2>;
// }

// function About() {
//   return <h2>About</h2>;
// }

// function Users() {
//   return <h2>Users</h2>;
// }
// import {
//   BrowserRouter as Router,
//   Routes,
//   Route,
//   Link,
//   BrowserRouter
// } from "react-router-dom";
// import Home from "./home";
// import About from "./about1";
// function App(){
// return(<>
//  <BrowserRouter>
//  <Routes>
//   <Route index  element={<Home/>}/>
//   <Route path="/about1"  element={<About/>}/>
// </Routes>
//  </BrowserRouter>
// </>)

// }
// export default App
// import Productcontext from './productcontext'
// import Productstate from "./productstate.jsx";
// import Home from './home'
// import About from './about.jsx'
// function App(){
//   return (
//     <>
//     <Productstate>
// <Home>
// </Home>
// <About></About>
//     </Productstate>
//     </>
//   )
// }
// export default App

// import './App.css'
// import {Provider} from 'react-redux'
// import store from './book/bookstor.jsx'
// import Bookreducer from './book/bookreucer.jsx'
// import BookContainer from './book/bookcontainer.jsx'
// function App () {
//     return ( <>
//      <Provider store={store}>
//        <BookContainer>
//        </BookContainer>
//      </Provider>
//         </> ) }
// export default App

// import "./App.css"
// import Nodestate from "./notestate"
// import About from "./about"
// function App(){
//   return(
//     <>
//     <Nodestate></Nodestate>
//     <About></About>
//     </>
//   )
// }
// export default App
//       --------...........-------------------gym website...---------------------------------------------------------
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
// import React   from "react";
// import './app.css'
// import Navbar from "./react-project/Navbar"
//  const App = () => {
// return<>
// <Navbar/>
// </>;
//  };
//  export default App;

     