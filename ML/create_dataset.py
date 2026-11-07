'''import pandas as pd
import random

# Locations in Dhaka
locations = [
    "Mirpur",
    "Uttara",
    "Dhanmondi",
    "Mohammadpur",
    "Badda",
    "Banani",
    "Bashundhara",
    "Rampura",
    "Khilgaon",
    "Farmgate"
]

data = []

# Generate 2,000 records
for i in range(2000):

    location = random.choice(locations)

    bedrooms = random.randint(1, 4)

    bathrooms = random.randint(1, 3)

    size = random.randint(600, 2200)

    floor = random.randint(1, 12)

    parking = random.choice(["Yes", "No"])

    furnished = random.choice(["Yes", "No"])

    balcony = random.choice(["Yes", "No"])

    building_age = random.randint(1, 20)

    # Calculate sample rent
    rent = (
        5000
        + bedrooms * 5000
        + bathrooms * 3000
        + size * 15
    )

    data.append([
        location,
        bedrooms,
        bathrooms,
        size,
        floor,
        parking,
        furnished,
        balcony,
        building_age,
        rent
    ])


# Create DataFrame
df = pd.DataFrame(data, columns=[
    "location",
    "bedrooms",
    "bathrooms",
    "size",
    "floor",
    "parking",
    "furnished",
    "balcony",
    "building_age",
    "rent"
])


# Save CSV file
df.to_csv("dataset/house_rent.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print(df.head())         '''