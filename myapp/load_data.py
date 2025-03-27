import pandas as pd
from myapp.models import Plant

def run():
       file_path = "dataset/plants_data.xlsx"  # Ensure this is the correct path
       df = pd.read_excel(file_path)

       # Print the columns to debug
       print("Columns in DataFrame:", df.columns.tolist())

       for _, row in df.iterrows():
           plant, created = Plant.objects.update_or_create(
               name=row["Plant Name"],  # Match by plant name
               defaults={
                   "climate": row["Climate"],
                   "soil_type": row["Soil Type"],
                   "pesticide": row["Pesticide Used"],  # Check this line
                   "pesticide_time": row["Pesticide Application Time"],
                   "growth_duration": row["Growth Duration"],
                   "fertilizers_used": row["Fertilizers Used"],
                   "harvesting_season": row["Harvesting Season"],
               },
           )
           if created:
               print(f"Added new plant: {plant.name}")
           else:
               print(f"Updated plant: {plant.name}")