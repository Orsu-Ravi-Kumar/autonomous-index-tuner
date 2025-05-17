from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model & scaler
model = joblib.load('C:/Users/Ravik/autonomous-index-tuner/data/index_recommender_model.pkl')
scaler = joblib.load('C:/Users/Ravik/autonomous-index-tuner/data/feature_scaler.pkl')

# Feature names
FEATURES = [
    'execution_count',
    'avg_cpu_time',
    'avg_elapsed_time',
    'avg_logical_reads',
    'avg_logical_writes',
    'query_length'
]

# Define input schema
class QueryMetrics(BaseModel):
    execution_count: int
    avg_cpu_time: float
    avg_elapsed_time: float
    avg_logical_reads: float
    avg_logical_writes: float
    query_length: int

# Init API app
app = FastAPI(title="Autonomous Index Tuning API")

@app.get("/")
def root():
    return {"message": "Autonomous Index Tuner is up!"}

@app.post("/recommend")
def recommend_index(metrics: QueryMetrics):
    df = pd.DataFrame([metrics.dict()])[FEATURES]
    df_scaled = scaler.transform(df)
    prediction = model.predict(df_scaled)[0]

    if prediction == 1:
        return {
            "index_needed": True,
            "sql": "CREATE NONCLUSTERED INDEX IX_YourTable_Column ON YourTable(YourColumn);"
        }
    else:
        return {
            "index_needed": False,
            "message": "Query does not require indexing."
        }
