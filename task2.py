# Task 2: Generate KM Distance and Save to PostgreSQL
# Read the terrain classification CSV file.
# Calculate the KM distance for each latitude and longitude pair.
# Match the terrain information.
# Save the details to a PostgreSQL table.


import pandas as pd
from sqlalchemy import create_engine, text
from geopy.distance import geodesic

# Define the file path
input_file = 'corrected_latitude_longitude_details.csv'  # Path to the corrected coordinates CSV

# Step 1: Load the corrected coordinates
df = pd.read_csv(input_file)

# Step 2: Calculate KM distance for each pair
distances = [0]
for i in range(1, len(df)):
    prev_point = (df.iloc[i-1]['latitude'], df.iloc[i-1]['longitude'])
    curr_point = (df.iloc[i]['latitude'], df.iloc[i]['longitude'])
    distance = geodesic(prev_point, curr_point).km
    distances.append(distances[-1] + distance)

df['KM'] = distances

# Step 3: Save to MySQL using SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:@localhost/new_indel')

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS path_details (
            id INT AUTO_INCREMENT PRIMARY KEY,
            latitude FLOAT,
            longitude FLOAT,
            km FLOAT
        )
    """))
    
    df.to_sql('path_details', conn, if_exists='append', index=False)

print("Data saved to MySQL database successfully.")
