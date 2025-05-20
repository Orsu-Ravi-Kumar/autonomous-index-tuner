from fastapi import FastAPI
import joblib
import pandas as pd

# Load model
#model = joblib.load("C:/Users/Ravik/autonomous-index-tuner/Predicitve_Backup_Scheduler/models/backup_predictor.pkl")
model = joblib.load("models/backup_predictor.pkl")

# Create FastAPI instance
app = FastAPI(title="Predictive Backup Scheduler API")

@app.get("/")
def root():
    return {"message": "Welcome to the Predictive Backup Scheduler API"}

@app.get("/predict/")
def predict(hour: int, day_of_week: int, backup_size: float):
    # Prepare input
    input_data = pd.DataFrame([[hour, day_of_week, backup_size]],
                              columns=["hour", "day_of_week", "backup_size"])
    
    # Predict
    prediction = model.predict(input_data)[0]

    # Format result
    recommendation = "Not Recommended" if prediction == 1 else "Recommended"
    return {
        "hour": hour,
        "day_of_week": day_of_week,
        "backup_size": backup_size,
        "prediction": int(prediction),
        "recommendation": recommendation
    }
