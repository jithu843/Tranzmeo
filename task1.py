
#1. Read the CSV file and identify out-of-line coordinates.
#2. Fix the coordinates to form a continuous path.
#3. Save the corrected coordinates to a new CSV file.
#4. Plot the coordinates before and after fixing.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev

# Step 1: Load the CSV file
input_file = 'latitude_longitude_details.csv'
output_file = 'corrected_latitude_longitude_details.csv'
df = pd.read_csv(input_file)

# Step 2: Plot the original coordinates
plt.figure(figsize=(10, 5))
plt.plot(df['longitude'], df['latitude'], 'o-', label='Original Path')
plt.title('Original Path')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.legend()
plt.savefig('original_path.png')
plt.show()

# Step 3: Fix the coordinates to form a continuous path using spline fitting
tck, u = splprep([df['longitude'], df['latitude']], s=0)
new_points = splev(np.linspace(0, 1, len(df)), tck)

# Step 4: Save the corrected coordinates to a new CSV file
corrected_df = pd.DataFrame({'longitude': new_points[0], 'latitude': new_points[1]})
corrected_df.to_csv(output_file, index=False)

# Step 5: Plot the corrected coordinates
plt.figure(figsize=(10, 5))
plt.plot(corrected_df['longitude'], corrected_df['latitude'], 'o-', label='Corrected Path', color='red')
plt.title('Corrected Path')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.legend()
plt.savefig('corrected_path.png')
plt.show()

# Step 6: Plot both original and corrected coordinates for comparison
plt.figure(figsize=(10, 5))
plt.plot(df['longitude'], df['latitude'], 'o-', label='Original Path')
plt.plot(corrected_df['longitude'], corrected_df['latitude'], 'o-', label='Corrected Path', color='red')
plt.title('Original vs Corrected Path')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.legend()
plt.savefig('comparison_path.png')
plt.show()
