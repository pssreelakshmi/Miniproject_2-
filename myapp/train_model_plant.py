import os
import django
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace 'your_project_name' with your actual project name

# Setup Django
django.setup()

from myapp.models import Plant  # Import your model after setting up Django

# Load data from the database
def load_data():
    plants = Plant.objects.all()
    data = []
    for plant in plants:
        data.append([
            plant.climate,
            plant.soil_type,
            plant.pesticide,
            plant.pesticide_time,
            plant.growth_duration,
            plant.fertilizers_used,
            plant.harvesting_season,
            plant.name  # This will be the target variable
        ])
    return pd.DataFrame(data, columns=[
        "Climate", "Soil Type", "Pesticide", "Pesticide Application Time",
        "Growth Duration", "Fertilizers Used", "Harvesting Season", "Plant Name"
    ])

def train_model():
    df = load_data()

    # Print the columns to debug
    print("Columns in DataFrame:", df.columns.tolist())

    # Prepare your features and labels
    X = df.drop("Plant Name", axis=1)  # Features
    y = df["Plant Name"]  # Target variable

    # Convert categorical variables to numerical
    X = pd.get_dummies(X)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))

if __name__ == "__main__":
    train_model()