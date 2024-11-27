
import "./Feedback.css"
import { useState } from "react"
import { useNavigate } from "react-router-dom"
import {Toaster, toast} from 'sonner'
// import { useTransition } from "react"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Button } from "@/components/ui/button"
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
  } from "@/components/ui/select"

  import { Textarea } from "@/components/ui/textarea"
  import { useForm } from "react-hook-form"
  import axios from 'axios'

export default function Feedback(){

    // handle navigation for toast
    const navigate = useNavigate()

    // handle multiple submissions
    const [isSubmitted, setIsSubmitted] = useState(false);

    // initialize react-hook-form
    const {register, handleSubmit, formState: {errors}, setValue} = useForm();
    
    // handle onsubmit
    const onSubmit = async function(data, e){
        e.preventDefault();
        // prevent multiple submissions
        if (isSubmitted) return;
        try{
          setIsSubmitted(true)
            const response = await axios.post('http://localhost:5000/comments/add', data,  {headers: {
              'Content-Type': 'application/json',
            },
        });
        
        toast('Feedback has been sent!')

        // 3 second delay and then navigate to home page
        setTimeout(function(){
          navigate("/")
        }, 2000);

            console.log('Form submitted successfully:', response.data);
            
          
            console.log("Sent!")

          

           
        }catch(error){
          // add toast for error
          toast.error("Error submitting form")
            console.error('Error submitting form:', error);
        }

      
    }
    
   
    
    return(
        <>
        <form onSubmit={handleSubmit(onSubmit)}>

     
        <div className="feedback-form">
            
        <div className="name-fields">
        <div className="field">
        <Label className="mb-2" htmlFor="first-name">First Name</Label>
        {errors.first_name && <span className="form-error">This field is required</span>}
        <Input className="w-[200px]" type="text" id="first-name" placeholder="Eg. Jane" {...register("first_name",
                                                                                            {required: "First Name is required" },)}/>
        {/* update this to show server errors instead from backend */}
        {/* update backend to handle order of data being sent */}
        
        </div>
       
        <div className="field">
        <Label className="mb-2" htmlFor="last-name">Last Name</Label>
        {errors.last_name && <span className="form-error">This field is required</span>}
        <Input className="w-[200px]" type="text" id="last-name" placeholder="Eg. Doe" {...register("last_name",{required: "Last Name is required"})} />
       
        </div>
        
        </div>

        <div className="name-fields">
        <div className="field">
        <Label className="mb-2" htmlFor="email">Email</Label>
        {errors.email && <span className="form-error">{errors.email.message}</span>}
        <Input
  className="w-[200px]"
  type="email"
  id="email"
  placeholder="example@gmail.com"
  {...register("email", {
    required: "Email is required",
    pattern: {
      value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
      message: "Invalid email address",
    },
  })}
/>



        </div>
       
        <div className="field">
        {/* 
        <Input type="text" id="last-name" placeholder="Enter your last name here ..." /> */}
        <Label className="mb-2" htmlFor="product-list">Product</Label>
        {errors.product_type && <span className="form-error">Select a product</span>}
        <Select className="product-list"  {...register('product_type', { required: 'Please select a product.' })}
          onValueChange={(value) => setValue('product_type', value)} >
      <SelectTrigger className="w-[200px]">
        <SelectValue placeholder="Select a product" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectLabel>Products</SelectLabel>
          <SelectItem value="Software">Software</SelectItem>
          <SelectItem value="Hardware">Hardware</SelectItem>
          <SelectItem value="AI Chatbot">AI Chatbot</SelectItem> 
        </SelectGroup>
      </SelectContent>
    </Select>
        </div>
        

        </div>

        <div className="feedback-box">
      <Label htmlFor="feedback-area">Feedback</Label>
      {errors.feedback && <span className="form-error">This field is required</span>}
      <Textarea placeholder="Leave your feedback here." id="feedback-area" {...register("feedback",{required: "Feedback field cannot be empty"})}/>
      <Toaster className="toaster" position="top-center"/>
      <Button type="submit">
        Send message</Button>
      <p className="text-sm text-muted-foreground">
        Your feedback will be sent to the support team.
      </p>
     </div>
       
        </div>
        
        </form>
        
       
        </> 
    );
}