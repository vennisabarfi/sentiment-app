
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css"
import Home from "./Home/Home";
import Feedback from "./Feedback/Feedback";
import Dashboard from "./DashBoard/Dashboard";
import { ThemeProvider } from "./components/ui/theme-provider";
export default function App() {
  return (
   <>
   <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
   <BrowserRouter>
   <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/form" element={<Feedback/>}/>
      <Route path="/dashboard" element={<Dashboard/>}/>

   </Routes>
   </BrowserRouter>

       </ThemeProvider>
    


   
   </>
  )
}
