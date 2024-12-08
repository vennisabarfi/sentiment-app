import "./Overview.css"
import {
    Card,
    CardContent,
    CardFooter,
    CardHeader,
    CardTitle,
    CardDescription,
  } from "@/components/ui/card"
  
import { useState, useEffect } from "react";
import axios from "axios";
import { Skeleton } from "@/components/ui/skeleton"

// import { Bar, BarChart,  CartesianGrid, XAxis } from "recharts"



export default function Overview(){
    
  const [totalfeedback, setTotalFeedback] = useState([]);
  const [averagerating, setAverageRating] = useState([]);
  const [positivesentiment, setPostiveSentiment] = useState([]);
  const [negativesentiment, setNegativeSentiment] = useState([]);
  const [commentsdata, setCommentsData] = useState([]);
  const [loading, setLoading] = useState(true); //update this to react loader
  const [serverMessage, setServerMessage] = useState('');
  const [serverErrors, setServerErrors] = useState('');

  // receive total feedback value from backend
  useEffect(function(){
      async function fetchTotalFeedbackData(){
        try {
          const response = await axios.get(`http://localhost:5000/comments/total`);

          setTotalFeedback(response.data["Total Feedback"]);
        
         
          if (response.status === 200) {

            setServerMessage(response.data.message)
            // console.log(response.data)
          }

        }catch (error) {
          setServerErrors(error.response.data.message)
            
          console.log(`Error retrieving resources information: ${error.response.data.message}`)
        }
      }
      fetchTotalFeedbackData();
  }, [])

    // receive total positive sentiments from backend
    useEffect(function(){
      async function fetchPositiveSentimentsData(){
        try {
          const response = await axios.get(`http://localhost:5000/model/positive/all`);

          // work on fixing decimal points issue
          setPostiveSentiment(response.data["Positive Sentiments"]);
        
         
          if (response.status === 200) {

            setServerMessage(response.data.message)
            
          }

        }catch (error) {
          setServerErrors(error.response.data.message)
            
          console.log(`Error retrieving resources information: ${error.response.data.message}`)
        }
      }
      fetchPositiveSentimentsData();
  }, [])

     // receive negative sentiments value from backend
     useEffect(function(){
      async function fetchNegativeSentimentsData(){
        try {
          const response = await axios.get(`http://localhost:5000/model/negative/all`);

          // work on fixing decimal points issue
          setNegativeSentiment(response.data["Negative Sentiments"]);
        
         
          if (response.status === 200) {

            setServerMessage(response.data.message)
           
          }

        }catch (error) {
          setServerErrors(error.response.data.message)
            
          console.log(`Error retrieving resources information: ${error.response.data.message}`)
        }
      }
      fetchNegativeSentimentsData();
  }, [])


     // receive average ratings value from backend
     useEffect(function(){
      async function fetchAverageRatingData(){
        try {
          const response = await axios.get(`http://localhost:5000/model/rating/average`);

          // work on fixing decimal points issue
          setAverageRating(response.data["Average Rating"]);
        
         
          if (response.status === 200) {

            setServerMessage(response.data.message)
            console.log(response.data.value)
          }

        }catch (error) {
          setServerErrors(error.response.data.message)
            
          console.log(`Error retrieving resources information: ${error.response.data.message}`)
        }
      }
      fetchAverageRatingData();
  }, [])

 
// view comment data in intervals
 useEffect(function(){
  async function fetchCommentsData(){
    // loading information
    
    try {
      setLoading(true);
      const response = await axios.get(`http://localhost:5000/comments/total`);

      setCommentsData(response.data["Total Feedback"]);
    
     
      if (response.status === 200) {

        setServerMessage(response.data.message)
        setLoading(false)
        // console.log(response.data)
      }

    }catch (error) {
      setServerErrors(error.response.data.message)
      setLoading(false); //work on better integration
        
      console.log(`Error retrieving resources information: ${error.response.data.message}`)
    }
  }
  fetchCommentsData();
}, [])

// update this to be more dynamic
// Render loading, error, or data
// if (loading) return( <
// </div>);


  return(

    


        <>

              {/* style this properly */}
  {serverMessage && <p className="server-message">{serverMessage}</p>}
  {serverErrors && <p className="server-error">{serverErrors}</p>}

{/* form submitted number */}

<div className="overview-cards">

<Card className="overview-card">
  <CardHeader>
    <CardTitle className="mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">Total Feedback</CardTitle>
  </CardHeader>
  <CardContent className="-mt-2 scroll-m-20 text-3xl font-semibold tracking-tight">
    <p>{totalfeedback}</p>
  </CardContent>
  <CardFooter className="text-sm text-muted-foreground">
    <p>*Forms Submitted</p>
  </CardFooter>
</Card>

{/* average ratings */}
<Card className="overview-card">
  <CardHeader>
    <CardTitle className="mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">Average Rating</CardTitle>
  </CardHeader>
  <CardContent className="-mt-2 scroll-m-20 text-3xl font-semibold tracking-tight">
    <p>{averagerating}</p>
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
    <p>{positivesentiment}</p>
  </CardContent>
  <CardFooter className="text-sm text-muted-foreground">
    <p>*Greater than 3/5</p>
  </CardFooter>
</Card>

<Card className="overview-card">
  <CardHeader>
    <CardTitle className="mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">Negative</CardTitle>
  </CardHeader>
  <CardContent className="-mt-2 scroll-m-20 text-3xl font-semibold tracking-tight">
    <p>{negativesentiment}</p>
  </CardContent>
  <CardFooter className="text-sm text-muted-foreground">
    <p>*Less than 3/5</p>
  </CardFooter>
</Card>


</div>
{/* make this better. work on skeleton design */}
<div>
{loading && <div className="flex flex-col space-y-3">
<Skeleton className="h-[125px] w-[250px] rounded-xl" />
<div className="space-y-2">
<Skeleton className="h-4 w-[250px]" />
<Skeleton className="h-4 w-[200px]" />
</div></div>}
  {!loading && (

    <Card>
      <h1>hello</h1>
      <span>{commentsdata}</span>
    </Card>
  )}
</div>

<div className="chart-comments-section">

  <div className="chart">
  <Card>
  <CardHeader>
    <CardTitle>Chart Section</CardTitle>
    <CardDescription>Card Description</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Card Content</p>
  </CardContent>
  <CardFooter>
    <p>Card Footer</p>
  </CardFooter>
</Card>
  </div>

  <div className="comments-section">
  <Card>
  <CardHeader>
    <CardTitle>Incoming Comments</CardTitle>
    <CardDescription>Card Description</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Card Content</p>
  </CardContent>
  <CardFooter>
    <p>Card Footer</p>
  </CardFooter>
</Card>
  </div>
</div>



        </>
    );
}