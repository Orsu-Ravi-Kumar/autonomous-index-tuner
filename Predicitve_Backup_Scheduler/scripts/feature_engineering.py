import pandas as pd

def generate_features(backup_csv_path):
    # Load backup logs
    df = pd.read_csv(backup_csv_path)

    # Convert to datetime
    df['backup_startup_date'] = pd.to_datetime(df['backup_startup_date'])

    # Extract time features
    df['hour'] = df['backup_startup_date'].dt.hour
    df['day_of_week'] = df['backup_startup_date'].dt.dayofweek

    # Label: risky if backup took more than 10 minutes (600 seconds)
    df['failure_risk'] = df['duration_seconds'].apply(lambda x: 1 if x > 600 else 0)

    # Final feature set
    final_df = df[['hour', 'day_of_week', 'backup_size', 'failure_risk']]
    
    # Save to CSV for modeling
    final_df.to_csv("C:/Users/Ravik/autonomous-index-tuner/Predicitve_Backup_Scheduler/data/features.csv", index=False)
    print("✅ Feature file saved as data/features.csv")

# Run this if executing standalone
if __name__ == "__main__":
    generate_features("C:/Users/Ravik/autonomous-index-tuner/Predicitve_Backup_Scheduler/data/backup_logs.csv")
