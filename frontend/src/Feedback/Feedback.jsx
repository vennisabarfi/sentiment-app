
import "./Feedback.css"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
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


export default function Feedback(){

    return(
        <>
        <div className="feedback-form">
            
        <div className="name-fields">
        <div className="field">
        <Label className="mb-2" htmlFor="first-name">First Name</Label>
        <Input className="w-[200px]" type="text" id="first-name" placeholder="Enter your first name here ..." />
        </div>
       
        <div className="field">
        <Label className="mb-2" htmlFor="last-name">Last Name</Label>
        <Input className="w-[200px]" type="text" id="last-name" placeholder="Enter your last name here ..." />
        </div>
        
        </div>

        <div className="name-fields">
        <div className="field">
        <Label className="mb-2" htmlFor="email">Email</Label>
        <Input className="w-[200px]" type="email" id="email" placeholder="example@gmail.com" />
        </div>
       
        <div className="field">
        {/* 
        <Input type="text" id="last-name" placeholder="Enter your last name here ..." /> */}
        <Label className="mb-2" htmlFor="product-list">Product</Label>
        <Select className="product-list">
      <SelectTrigger className="w-[200px]">
        <SelectValue placeholder="Select a product" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectLabel>Products</SelectLabel>
          <SelectItem value="software">Software</SelectItem>
          <SelectItem value="hardware">Hardware</SelectItem>
          <SelectItem value="ai-chatbot">AI Chatbot</SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
        </div>
        

        </div>

        <div className="feedback-box">
      <Label htmlFor="feedback-area">Feedback</Label>
      <Textarea placeholder="Leave your feedback here." id="feedback-area" />
      <p className="text-sm text-muted-foreground">
        Your message will be copied to the support team.
      </p>
     </div>
       
        </div>
        
        </>
    );
}