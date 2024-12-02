
import Menubar from "./Menubar";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"


export default function Dashboard(){
    return(
        <>
        
        <SidebarProvider>
        <Menubar/>
        <main>
        <SidebarTrigger />
        </main>
        </SidebarProvider>

        </>

    );
}