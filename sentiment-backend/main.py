from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

# Initialize the sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the Pydantic model
class TextRequest(BaseModel):
    text: str

@app.post("/analyze/")
async def analyze_sentiment(request: TextRequest):
    # Use the classifier to analyze the sentiment of the input text
    result = classifier(request.text)[0]  # Access the first result from the classifier
    return {
        "label": result["label"],  # Positive/Negative
        "score": result["score"],  # Confidence score
    }