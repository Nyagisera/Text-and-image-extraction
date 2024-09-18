from fastapi import FastAPI, File, UploadFile
import fitz
from app.summarization import summarize_text

app = FastAPI()

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    """API endpoint to extract and summarize data from a PDF."""
    doc = fitz.open(file.file)
    text = ""
    for page in doc:
        text += page.get_text("text")
    
    summarized_text = summarize_text(text)
    
    return {"summary": summarized_text}
