from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str = "nitesh"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10,default=0.0,description="CGPA of the student")


new_student = Student(email='abc')

student_json = new_student.model_dump_json()
print(student_json)
print(new_student.name)



from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, Literal, List
from pydantic import BaseModel, Field

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.0-flash")

class Review(BaseModel):
    key_themes: Optional[str] = Field(None, description="Key themes of the review")
    summary: str = Field(..., description="A brief summary of the review")
    sentiment: Literal["positive", "negative"] = Field(..., description="The sentiment of the review, either positive or negative")
    pros: Optional[List[str]] = Field(None, description="A list of pros mentioned in the review")
    cons: Optional[List[str]] = Field(None, description="A list of cons mentioned in the review")

structured_model = model.with_structured_output(Review) #? Not implemented yet for google generative AI

result = structured_model.invoke("""The hardware is great, but the software is terrible. I would not recommend this product.""")
print(result)
print(result.summary)
print(result.sentiment)