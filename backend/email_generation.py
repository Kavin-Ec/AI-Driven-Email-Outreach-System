from openai import OpenAI
from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from pydantic import BaseModel
import pymupdf as fitz  # PyMuPDF
from typing import Optional

router = APIRouter()
openai = OpenAI(
    base_url = "http://localhost:1234/v1/",
    api_key = "not-needed",
)

router = APIRouter()

# Define Pydantic model for the research report
class ResearchReport(BaseModel):
    research_report: str

@router.post("/email")
async def generate_email(
    research_report: str = Form(...),  # Use Form for text input
    product_catalog: UploadFile = File(...)  # Use File for file upload
):
    try:
         # Read the uploaded PDF file
        pdf_document = fitz.open(stream=await product_catalog.read(), filetype="pdf")
        catalog_text = ""
        
        # Extract text from each page
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            catalog_text += page.get_text()
        # Construct the prompt for the API
        prompt = f"Compose a compelling email promoting a free trial of products - {catalog_text}. Clearly communicate the benefits, features, and unique selling points to encourage the prospect and company -\" {research_report}\" to take the next step and try it out."
        response = openai.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        email_draft = response.choices[0].message.content.strip()
        return {"email": email_draft}
    except Exception as e:
        # Handle and log exceptions
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
