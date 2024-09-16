from openai import OpenAI
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
router = APIRouter()

openai = OpenAI(
    base_url = "http://localhost:1234/v1/",
    api_key = "not-needed",
)
class ResearchRequest(BaseModel):
    prospect_name: str
    company_name: str
    
@router.post("/prospect")
async def research_prospect(request: ResearchRequest):
    try:
        prompt = f"Research details about {request.prospect_name} and their company {request.company_name}."
        response = openai.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        research_text = {"research": response.choices[0].message.content.strip()}
        if not research_text:
                raise HTTPException(status_code=404, detail="Research report not found")
        return research_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
