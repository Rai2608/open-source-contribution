import numpy as np
from sklearn.ensemble import IsolationForest

# Dummy ML Model - Training on normal behavior
def train_model():
    # Simulated normal communication data [packet_size, freq, error_rate, suspicious_score]
    X_train = np.array([
        [200, 3, 0.01, 0],
        [180, 4, 0.00, 0],
        [220, 3, 0.02, 0],
        [210, 5, 0.01, 0],
        [190, 4, 0.01, 0],
    ])
    
    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(X_train)
    return model

# Threat Detector Function
def detect_threat(input_metrics, model):
    """
    input_metrics = [packet_size, frequency, error_rate, suspicious_score]
    """
    X = np.array([input_metrics])
    prediction = model.predict(X)[0]  # -1 = anomaly, 1 = normal

    if prediction == 1:
        return "Low"
    else:
        # Optionally add custom rules for severity
        score = sum(input_metrics)  # crude scoring logic
        if score > 500:
            return "High"
        else:
            return "Moderate"

# Example usage
if __name__ == "__main__":
    clf = train_model()
    
    # Normal scenario
    metrics_1 = [200, 4, 0.01, 0]
    print("Threat Level 1:", detect_threat(metrics_1, clf))

    # Suspicious scenario
    metrics_2 = [300, 10, 0.05, 1]
    print("Threat Level 2:", detect_threat(metrics_2, clf))
