import pandas as pd
import numpy as np
from sklearn.datasets import make_classification

# Create synthetic dataset
np.random.seed(42)
num_samples = 1000

# Generate features (image features would normally come from CNN, but we'll simulate)
X, _ = make_classification(n_samples=num_samples, n_features=20, n_informative=15, n_redundant=5)

# Create target variables
plants = ['Tomato', 'Potato', 'Corn', 'Wheat', 'Rice', 'Soybean']
soil_types = ['Loamy', 'Sandy', 'Clay', 'Silty', 'Peaty']
climates = ['Tropical', 'Temperate', 'Arid', 'Mediterranean', 'Continental']
pesticides = ['Neem Oil', 'Pyrethrin', 'Spinosad', 'Bacillus Thuringiensis', 'Copper Fungicide']
periods = ['Weekly', 'Bi-weekly', 'Monthly', 'Seasonal', 'As needed']

data = {
    'plant_type': np.random.choice(plants, num_samples),
    'soil_type': np.random.choice(soil_types, num_samples),
    'climate': np.random.choice(climates, num_samples),
    'pesticide': np.random.choice(pesticides, num_samples),
    'application_period': np.random.choice(periods, num_samples)
}

# Add the synthetic features
for i in range(20):
    data[f'feature_{i}'] = X[:, i]

df = pd.DataFrame(data)
df.to_csv('plant_data.csv', index=False)
print("Dataset created successfully!")