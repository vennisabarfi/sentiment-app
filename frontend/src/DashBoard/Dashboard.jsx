
import Menubar from "./Menubar";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import "./Dashboard.css"
import "../index.css"
import Overview from "./Overview";
import Analytics from "./Analytics";
import { ModeToggle } from "@/components/ui/mode-toggle";
import {
    Tabs,
    TabsList,
    TabsTrigger,
  } from "@/components/ui/tabs"
import { TabsContent } from "@radix-ui/react-tabs";

export default function Dashboard(){
    return(

      
        <>
          
       <body>
          
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
    
        <div className="dashboard-layout ">

            <div className="header">
            <h2 className="name-header">Hi, Welcome back 👋</h2>
            <div className="toggle-mode">
            <ModeToggle/>
            </div>

    
                
        </div>
          
        <div className="overview-analytics">
        <Tabs defaultValue="overview" className="space-y-4">
          <TabsList>
            <TabsTrigger value="overview">
                Overview
                </TabsTrigger>

            <TabsTrigger value="analytics">
              Analytics
            </TabsTrigger>
          </TabsList>

          <TabsContent value="overview">
          <Overview/>
          </TabsContent>

          <TabsContent value="analytics">
          <Analytics/>
          </TabsContent>
          
            </Tabs>
           
        </div>
        </div>

        </body>

        {/* Overview and Analytics Toggle */}

       
       

       
        
        </>

    );
}