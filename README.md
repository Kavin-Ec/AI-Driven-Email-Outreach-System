# AI-Powered SDR Email Outreach System
This project automates the email outreach process for SDRs.

To Run the Overall Project:

To activate the venv(meta llama): 
1)cd project
2) first start the server(Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf - model) in LM Studio
3).\llama\Scripts\Activate.ps1 ( both in frontend and backend)

To run the backend:
1)cd backend
2)uvicorn main:app --reload

To run the frontend:
1)cd frontend
2)streamlit run app.py
