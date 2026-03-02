import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def get_knn_data_and_model():
    # 4. K-Nearest Neighbors (KNN): Cybersecurity Network Intrusion Detection
    # Features: Packet Size (bytes), Frequency (req/s)
    # Target: Class (0 = Normal, 1 = Malicious)
    
    np.random.seed(42)
    
    # Normal traffic
    n_normal = 150
    normal_packet = np.random.normal(500, 100, n_normal)
    normal_freq = np.random.normal(50, 15, n_normal)
    
    # Malicious traffic (e.g., DDOS: small packets, high freq OR large packets, low freq for payload export)
    n_malicious = 100
    malicious_packet1 = np.random.normal(100, 20, n_malicious // 2)
    malicious_freq1 = np.random.normal(200, 30, n_malicious // 2)
    
    malicious_packet2 = np.random.normal(1500, 200, n_malicious // 2)
    malicious_freq2 = np.random.normal(10, 5, n_malicious // 2)
    
    packet_size = np.concatenate([normal_packet, malicious_packet1, malicious_packet2])
    frequency = np.concatenate([normal_freq, malicious_freq1, malicious_freq2])
    labels = np.concatenate([np.zeros(n_normal), np.ones(n_malicious)])
    
    df = pd.DataFrame({
        'Packet_Size': packet_size,
        'Frequency': frequency,
        'Class': labels
    })
    
    X = df[['Packet_Size', 'Frequency']]
    y = df['Class']
    
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X, y)
    
    return df, model
