from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.0-flash")


class Review(TypedDict):
    key_themes : Annotated
    summary: Annotated[str, "A breif summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review, either positive or negative"]
    pros: Annotated[Optional[list[str]], "A list of pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "A list of cons mentioned in the review"]
structured_model = model.with_structured_output(Review) #? Not implemented yet for google generative AI


result = structured_model.invoke("""The hardware is great, but the software is terrible. I would not recommend this product.""")
print(result)
print(result.summary)
print(result.sentiment)