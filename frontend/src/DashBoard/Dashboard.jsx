
import Menubar from "./Menubar";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import "./Dashboard.css"

export default function Dashboard(){
    return(
        <>

            
        <div className="sidebar-layout">
        <SidebarProvider
         style={{
            "--sidebar-width": "20rem",
            "--sidebar-width-mobile": "20rem",
          }}>
        <Menubar/>
        <main>
        <SidebarTrigger className="sidebar-icon" />
        </main>
        </SidebarProvider>
        </div>
    
        <div className="dashboard-layout">
            <h2 className="name-header">Hi, Welcome back 👋</h2>
            

        </div>

        
       
        
        </>

    );
}