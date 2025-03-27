import os
import pandas as pd

# Path to the PlantVillage folder
dataset_path = 'PlantVillage'

# Create a list to store image paths and labels
data = []

# Loop through each folder in the dataset
for label in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, label)
    if os.path.isdir(folder_path):
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            data.append({'image_path': image_path, 'label': label})

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('plantvillage_dataset.csv', index=False)
print("CSV file created successfully!")