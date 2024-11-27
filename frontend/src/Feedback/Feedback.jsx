
import "./Feedback.css"
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

    // initialize react-hook-form
    const {register, handleSubmit, formState: {errors}, setValue} = useForm();
    
    // handle onsubmit
    const onSubmit = async function(data){
        try{
            const response = await axios.post('http://localhost:5000/comments/add', data,  {headers: {
              'Content-Type': 'application/json',
            },
        });
            
            toast('Feedback has been sent!', {
              action: {
                label: 'Done',
                onClick: () => window.location.reload()
              },
            })
            console.log("Sent!")

            console.log('Form submitted successfully:', response.data);
        }catch(error){
            console.error('Error submitting form:', error);
        }
    }
    
    // const [isLoading, startLoading] = useTransition();
    // const loading = function(data){
    //     startLoading(async function(){
    //       await onSubmit(data);
    //     });
    // }
    
    return(
        <>
        <form onSubmit={handleSubmit(onSubmit)}>

     
        <div className="feedback-form">
            
        <div className="name-fields">
        <div className="field">
        <Label className="mb-2" htmlFor="first-name">First Name</Label>
        <Input className="w-[200px]" type="text" id="first-name" placeholder="Eg. Jane" {...register("first_name",{required: "First Name is required"})}/>
        {/* update this to show server errors instead from backend */}
        {/* update backend to handle order of data being sent */}
        {errors.name && <span>This field is required</span>}
        </div>
       
        <div className="field">
        <Label className="mb-2" htmlFor="last-name">Last Name</Label>
        <Input className="w-[200px]" type="text" id="last-name" placeholder="Eg. Doe" {...register("last_name",{required: "Last Name is required"})} />
        </div>
        
        </div>

        <div className="name-fields">
        <div className="field">
        <Label className="mb-2" htmlFor="email">Email</Label>
        <Input className="w-[200px]" type="email" id="email" placeholder="example@gmail.com" {...register("email",{required: "Email is required"})}/>
        </div>
       
        <div className="field">
        {/* 
        <Input type="text" id="last-name" placeholder="Enter your last name here ..." /> */}
        <Label className="mb-2" htmlFor="product-list">Product</Label>
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
      <Textarea placeholder="Leave your feedback here." id="feedback-area" {...register("feedback",{required: "Feedback field cannot be empty"})}/>
      <Toaster position="bottom-center"/>
      <Button type="submit">
      {/* {isLoading ? "Sending ..." : ""} */}
      {/* continue working on this and implementing a toast instead */}
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