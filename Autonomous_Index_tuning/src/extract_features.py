import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

# Path to your data
data_path = os.path.join("..", "data", "query_stats.csv")

# Load the query stats CSV
df = pd.read_csv(data_path)

# Show column names to debug issues
print("Available Columns:\n", df.columns.tolist())

# Rename columns if necessary
if 'text' in df.columns:
    df.rename(columns={'text': 'query_text'}, inplace=True)

# Filter out abnormally long queries
df = df[df['query_text'].str.len() < 1000]

# Add engineered feature: query length
df['query_length'] = df['query_text'].apply(len)

# Drop non-numeric or irrelevant columns for ML
df_features = df.drop(columns=['query_text', 'query_hash'])

# Scale all numeric values between 0–1
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df_features)
df_scaled = pd.DataFrame(scaled, columns=df_features.columns)

# Save to file
output_path = os.path.join("..", "data", "features_query_stats.csv")
df_scaled.to_csv(output_path, index=False)

print(f"✅ Feature engineering complete. Saved to {output_path}")
