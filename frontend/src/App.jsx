
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css"
import Home from "./Home/Home";
import Feedback from "./Feedback/Feedback";
import Dashboard from "./DashBoard/Dashboard";

export default function App() {
  return (
   <>
   <BrowserRouter>
   <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/form" element={<Feedback/>}/>
      <Route path="/dashboard" element={<Dashboard/>}/>

   </Routes>
   </BrowserRouter>
    


   
   </>
  )
}
