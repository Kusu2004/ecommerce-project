from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from models import SessionRequest
from feature_extractor import extract_features
from rules_engine import classify_shopper


app = FastAPI()


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Ecommerce Personalization Rules Engine is running"
    }


@app.post("/classify")
def classify_session(request: SessionRequest):

    # Step 1: Convert events into feature counts
    features = extract_features(request.events)

    # Step 2: Classify the shopper
    classification = classify_shopper(features)

    # Step 3: Return final result
    return {
        "user_id": request.user_id,
        "features": features,
        "classification": classification
    }