from openai import OpenAI
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

openai = OpenAI(
    base_url = "http://localhost:1234/v1/",
    api_key = "not-needed",
)
# Define Pydantic model for the email optimization request
class EmailOptimizationRequest(BaseModel):
    generated_email: str
    templates: str

@router.post("/optimize")
async def optimize_email(request: EmailOptimizationRequest):
    try:
        generated_email = request.generated_email
        templates = request.templates
        
        # Call OpenAI API or your optimization function here
        # For example, let's assume we use OpenAI's API for optimization
        prompt = f"Optimize this email based on these templates:\n\nTemplates:\n{templates}\n\nEmail:\n{generated_email}. The email should be ready to be sent without any placeholders or extra information."
    
        response = openai.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        review_output = response.choices[0].message.content.strip()
        return {"optimized_email": review_output}
    except Exception as e:
     # Handle and log exceptions
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
