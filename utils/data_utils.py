import csv
import json
from typing import List
from models.property import Property

def save_properties_to_csv(properties: List[dict], filename: str):
    if not properties:
        print("No properties to save.")
        return

    # Use field names from the Property model
    fieldnames = Property.model_fields.keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        # If properties is a list containing a list, take the first item
        data_to_write = properties[0] if isinstance(properties[0], list) else properties
        writer.writerows(data_to_write)
    print(f"Saved {len(data_to_write)} properties to '{filename}'.")

def save_properties_to_json(properties: List[dict], filename: str):
    if not properties:
        print("No properties to save.")
        return

    # If properties is a list containing a list, take the first item
    data_to_write = properties[0] if isinstance(properties[0], list) else properties
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data_to_write, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(data_to_write)} properties to '{filename}'.") 