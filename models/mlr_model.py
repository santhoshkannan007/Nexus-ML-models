import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def get_mlr_data_and_model():
    # 2. Multiple Linear Regression (MLR): YouTube Video Viral Potential
    # Features: Thumbnail Saturation (0-100), Title Length (words), Tags (count), Video Duration (mins)
    # Target: Engagement Score (0-100)
    
    np.random.seed(42)
    n_samples = 300
    
    saturation = np.random.uniform(30, 100, n_samples)
    title_length = np.random.uniform(3, 20, n_samples)
    tags = np.random.randint(0, 30, n_samples)
    duration = np.random.uniform(1, 60, n_samples)
    
    # Engagement formula + noise
    # Optimal title length around 8-10, let's make it a linear combination for MLR
    # (saturation gives positive boost, duration gives slight negative if too long, tags give small boost)
    engagement = 10 + (saturation * 0.4) + (title_length * 0.5) + (tags * 0.8) - (duration * 0.2) + np.random.normal(0, 5, n_samples)
    engagement = np.clip(engagement, 0, 100) # Keep within 0-100
    
    df = pd.DataFrame({
        'Thumbnail_Saturation': saturation,
        'Title_Length': title_length,
        'Num_Tags': tags,
        'Video_Duration': duration,
        'Engagement_Score': engagement
    })
    
    X = df[['Thumbnail_Saturation', 'Title_Length', 'Num_Tags', 'Video_Duration']]
    y = df['Engagement_Score']
    
    model = LinearRegression()
    model.fit(X, y)
    
    return df, model
