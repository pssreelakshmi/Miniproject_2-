import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv('plant_data.csv')

# Features and targets
features = [f'feature_{i}' for i in range(20)]
targets = ['soil_type', 'climate', 'pesticide', 'application_period']

# Train separate models for each target
models = {}
for target in targets:
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model for {target} - Accuracy: {accuracy:.2f}")
    
    models[target] = model

# Save models
joblib.dump(models, 'plant_models.joblib')
print("Models trained and saved successfully!")