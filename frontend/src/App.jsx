
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css"
import Home from "./Home/Home";
import Feedback from "./Feedback/Feedback";

export default function App() {
  return (
   <>
   <BrowserRouter>
   <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/form" element={<Feedback/>}/>
   </Routes>
   </BrowserRouter>
    


   
   </>
  )
}
