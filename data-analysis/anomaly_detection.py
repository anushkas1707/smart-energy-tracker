import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(data_path):
    df = pd.read_csv(data_path)
    model = IsolationForest(contamination=0.01)
    df['anomaly'] = model.fit_predict(df[['kwh']])
    return df[df['anomaly'] == -1]
