import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

def get_log_reg_data_and_model():
    # 5. Logistic Regression: Fintech Digital Payment Fraud Detection
    # Features: Transaction Amount ($), Time of Day (Hour: 0-23), Location Distance (miles)
    # Target: Fraud (1) or Legitimate (0)
    
    np.random.seed(42)
    n_samples = 400
    
    # Generating somewhat realistic distributions
    amount = np.random.exponential(scale=100, size=n_samples) # Mostly small, some very large
    time_of_day = np.random.uniform(0, 24, n_samples)
    distance = np.random.exponential(scale=20, size=n_samples)
    
    # Fraud logic: more likely if Amount is high, Distance is high, or Time is unusual (late night e.g., 2 AM)
    # Time diff from 3 AM
    time_penalty = np.abs(time_of_day - 3)
    # We want time_penalty to be max around 3 PM? Let's say closer to 3 AM is higher risk (lower diff)
    night_risk = 12 - np.minimum(time_penalty, 24 - time_penalty) # Peak at 3 AM (value=12), Min at 3 PM (value=0)
    
    z = -5 + (amount * 0.01) + (distance * 0.05) + (night_risk * 0.3)
    probability = 1 / (1 + np.exp(-z))
    
    fraud = np.random.binomial(1, probability)
    
    df = pd.DataFrame({
        'Transaction_Amount': amount,
        'Time_of_Day': time_of_day,
        'Location_Distance': distance,
        'Is_Fraud': fraud
    })
    
    X = df[['Transaction_Amount', 'Time_of_Day', 'Location_Distance']]
    y = df['Is_Fraud']
    
    # Increase max_iter to ensure convergence if needed, though our data is simple
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    
    return df, model
