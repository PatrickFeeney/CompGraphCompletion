#modify the blue bike data so it can be used in ArcGIS
import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point  # Import the Point class
# Define the folder path
bluebike_folder_path = '/mnt/c/Users/court/Documents/d3m_project/data/BlueBikes/bluebike_boston'
output_folder = '/mnt/c/Users/court/Documents/d3m_project/data/BlueBikes/bluebike_boston_georeferenced'
census_tracts_shapefile = '/mnt/c/Users/court/Documents/d3m_project/data/TIGER_lines/TIGER_lines_2024/tl_2024_25_tract/tl_2024_25_tract.shp'
# Iterate over all files in the folder
# for filename in os.listdir(bluebike_folder_path):
#     # Check if the file is a CSV file
#     if filename.endswith('.csv'):
#         # Replace '-' with '_' in the filename
#         new_filename = filename.replace('-', '_')
        
#         # Get the full paths for the old and new filenames
#         old_file_path = os.path.join(bluebike_folder_path, filename)
#         new_file_path = os.path.join(bluebike_folder_path, new_filename)
        
#         # Rename the file
#         os.rename(old_file_path, new_file_path)
#         print(f'Renamed: {filename} -> {new_filename}')
# for filename in os.listdir(bluebike_folder_path):
#     # Check if the file is a CSV file
#     if filename.endswith('.csv'):
#         # Construct the full file path
#         file_path = os.path.join(bluebike_folder_path, filename)
        
#         # Load the CSV file into a pandas DataFrame
#         df = pd.read_csv(file_path)
        
#         # Replace spaces with underscores in all column names
#         df.columns = [col.replace(" ", "_") for col in df.columns]
        
#         # Save the modified DataFrame back to CSV
#         df.to_csv(file_path, index=False)
#         print(f'Updated column names in: {filename}')

# print("All files have been processed.")
# Load the census tracts shapefile into a GeoDataFrame
census_tracts_gdf = gpd.read_file(census_tracts_shapefile)
# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate over all CSV files in the bluebike folder
for csv_file in os.listdir(bluebike_folder_path):
    if csv_file.endswith('.csv'):
        # Construct full file path
        csv_path = os.path.join(bluebike_folder_path, csv_file)
        
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Assuming the CSV has 'start_station_longitude' and 'start_station_latitude' columns
        geometry = [Point(xy) for xy in zip(df['start_station_longitude'], df['start_station_latitude'])]
        gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')  # Ensure CRS is set
        
        # Perform spatial join with census tracts
        joined_gdf = gpd.sjoin(gdf, census_tracts_gdf, how='inner', predicate='within')  # Use the GeoDataFrame, not the file path
        
        # Drop the geometry column to save as CSV (optional, depending on your needs)
        joined_df = pd.DataFrame(joined_gdf.drop(columns=['geometry']))
        
        # Construct the output file name
        base_name = os.path.splitext(csv_file)[0]
        output_file_name = f"{base_name}_georeferenced.csv"
        output_path = os.path.join(output_folder, output_file_name)
        
        # Save the joined DataFrame to a new CSV file
        joined_df.to_csv(output_path, index=False)
        
        print(f"Processed and saved: {output_file_name}")

print("All files have been processed.")