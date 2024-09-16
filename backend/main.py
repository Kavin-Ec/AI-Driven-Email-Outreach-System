from fastapi import FastAPI
from research import router as research_router
from email_generation import router as email_gen_router
from email_review import router as email_review_router
from email_sender import router as email_sender_router

app = FastAPI()

app.include_router(research_router, prefix="/research")
app.include_router(email_gen_router, prefix="/generate")
app.include_router(email_review_router, prefix="/review")
app.include_router(email_sender_router, prefix="/send")

@app.get("/")
def read_root():
    return {"message": "SDR AI system running!"}
