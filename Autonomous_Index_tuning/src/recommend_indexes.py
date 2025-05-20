import pandas as pd
import joblib

# Load trained model and saved scaler
model = joblib.load('C:/Users/Ravik/autonomous-index-tuner/data/index_recommender_model.pkl')
scaler = joblib.load('C:/Users/Ravik/autonomous-index-tuner/data/feature_scaler.pkl')

FEATURES = [
    'execution_count',
    'avg_cpu_time',
    'avg_elapsed_time',
    'avg_logical_reads',
    'avg_logical_writes',
    'query_length'
]

def get_query_features():
    return {
        'execution_count': 45,
        'avg_cpu_time': 150000,         # Push these higher if no index recommended
        'avg_elapsed_time': 200000,
        'avg_logical_reads': 6000,
        'avg_logical_writes': 150,
        'query_length': 350
    }

def recommend_index(query_metrics: dict):
    df = pd.DataFrame([query_metrics])[FEATURES]
    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)[0]

    if prediction == 1:
        print("✅ Index Recommended for this query.")
        print("Suggested index: CREATE NONCLUSTERED INDEX IX_YourTable_Column ON YourTable(YourColumn);")
    else:
        print("❌ No index needed for this query.")

if __name__ == "__main__":
    metrics = get_query_features()
    recommend_index(metrics)
