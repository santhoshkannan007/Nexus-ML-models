import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def get_poly_data_and_model():
    # 3. Polynomial Regression: Server CPU Cooling Efficiency
    # Feature: Fan Speed (RPM)
    # Target: CPU Temperature (C)
    
    np.random.seed(42)
    n_samples = 200
    
    # Fan speed from 1000 to 5000 RPM
    fan_speed = np.random.uniform(1000, 5000, n_samples)
    
    # Temp reduction drops off at higher RPMs (exponential decay or polynomial curve)
    # Temp = base_temp - a * speed + b * speed^2 + noise
    # At low speed, temp is high. At high speed, temp drops but plateaus.
    
    cpu_temp = 90 - 0.02 * fan_speed + 0.0000025 * (fan_speed ** 2) + np.random.normal(0, 2, n_samples)
    cpu_temp = np.clip(cpu_temp, 30, 100)
    
    df = pd.DataFrame({'Fan_Speed': fan_speed, 'CPU_Temp': cpu_temp})
    
    X = df[['Fan_Speed']]
    y = df['CPU_Temp']
    
    # Pipeline for Polynomial Regression (degree 2)
    model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
    model.fit(X, y)
    
    return df, model
