import "./Overview.css"
import {
    Card,
    CardContent,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
  

export default function Overview(){
    return(

        <>

{/* form submitted number */}

<div className="overview-cards">
<Card className="overview-card">
  <CardHeader>
    <CardTitle className="mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">Total Feedback</CardTitle>
  </CardHeader>
  <CardContent className="-mt-2 scroll-m-20 text-3xl font-semibold tracking-tight">
    <p>115</p>
  </CardContent>
  <CardFooter className="text-sm text-muted-foreground">
    <p>*Forms Submitted</p>
  </CardFooter>
</Card>

{/* average ratings */}
<Card className="overview-card">
  <CardHeader>
    <CardTitle className="mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">Average Ratings</CardTitle>
  </CardHeader>
  <CardContent className="-mt-2 scroll-m-20 text-3xl font-semibold tracking-tight">
    <p>3.4</p>
  </CardContent>
  <CardFooter className="text-sm text-muted-foreground">
    <p>*rated out of 5</p>
  </CardFooter>
</Card>


<Card className="overview-card">
  <CardHeader>
    <CardTitle className="mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">Positive</CardTitle>
  </CardHeader>
  <CardContent className="-mt-2 scroll-m-20 text-3xl font-semibold tracking-tight">
    <p>67</p>
  </CardContent>
  <CardFooter className="text-sm text-muted-foreground">
    <p>*Greater than 3.5/5</p>
  </CardFooter>
</Card>

<Card className="overview-card">
  <CardHeader>
    <CardTitle className="mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">Negative</CardTitle>
  </CardHeader>
  <CardContent className="-mt-2 scroll-m-20 text-3xl font-semibold tracking-tight">
    <p>35</p>
  </CardContent>
  <CardFooter className="text-sm text-muted-foreground">
    <p>*Less than 2.5/5</p>
  </CardFooter>
</Card>




</div>



        </>
    );
}