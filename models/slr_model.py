import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def get_slr_data_and_model():
    # 1. Simple Linear Regression (SLR): EV Charging Station Load Prediction
    # Feature: Ambient Temperature (-10 to 45 C)
    # Target: Power Demand (kW)
    # Story: Batteries charge differently in extreme temperatures; heating/cooling needs rise.
    
    np.random.seed(42)
    n_samples = 200
    
    temp = np.random.uniform(-10, 45, n_samples)
    
    # Power demand relationship: higher when very cold (battery heating) or very hot (AC/cooling)
    # But for SLR, let's keep it a bit more linear conceptually, or just use a linear segment.
    # Actually, a charging station demand index might just increase linearly with temperature in a specific climate,
    # or let's say: more temperature -> more cooling needed -> more ambient power demand.
    # Base load + temp * coefficient + noise
    power_demand = 50 + (temp * 1.5) + np.random.normal(0, 10, n_samples)
    
    df = pd.DataFrame({'Temperature': temp, 'PowerDemand': power_demand})
    
    X = df[['Temperature']]
    y = df['PowerDemand']
    
    model = LinearRegression()
    model.fit(X, y)
    
    return df, model
