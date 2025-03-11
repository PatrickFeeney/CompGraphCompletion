
import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point  # Import the Point class

## City of Boston Bike Data

bikeridership_path = '/mnt/c/Users/court/Documents/d3m_project/data/bikeridership/bikeridership_boston'
#2016

bike_tract_2016_summer_file=(bikeridership_path+'/bike_tract_2016_summer.csv')
bike_tract_2016_summer=pd.read_csv(bike_tract_2016_summer_file)

bike_tract_2016_fall_file=(bikeridership_path+'/bike_tract_2016_fall.csv')
bike_tract_2016_fall=pd.read_csv(bike_tract_2016_fall_file)

#2017

bike_tract_2017_fall_file=(bikeridership_path+'/bike_tract_2017_fall.csv')
bike_tract_2017_fall=pd.read_csv(bike_tract_2017_fall_file)

#2018

bike_tract_2018_summer_file=(bikeridership_path+'/bike_tract_2018_summer.csv')
bike_tract_2018_summer=pd.read_csv(bike_tract_2018_summer_file)

bike_tract_2018_fall_file=(bikeridership_path+'/bike_tract_2018_fall.csv')
bike_tract_2018_fall=pd.read_csv(bike_tract_2018_fall_file)

#2019

bike_tract_2019_summer_file=(bikeridership_path+'/bike_tract_2019_summer.csv')
bike_tract_2019_summer=pd.read_csv(bike_tract_2019_summer_file)

bike_tract_2019_fall_file=(bikeridership_path+'/bike_tract_2019_fall.csv')
bike_tract_2019_fall=pd.read_csv(bike_tract_2019_fall_file)

#2020

bike_tract_2020_summer_file=(bikeridership_path+'/bike_tract_2020_summer.csv')
bike_tract_2020_summer=pd.read_csv(bike_tract_2020_summer_file)

bike_tract_2020_fall_file=(bikeridership_path+'/bike_tract_2020_fall.csv')
bike_tract_2020_fall=pd.read_csv(bike_tract_2020_fall_file)

bike_tract_2020_spring_file=(bikeridership_path+'/bike_tract_2020_spring.csv')
bike_tract_2020_spring=pd.read_csv(bike_tract_2020_spring_file)

bike_tract_2020_winter_file=(bikeridership_path+'/bike_tract_2020_winter.csv')
bike_tract_2020_winter=pd.read_csv(bike_tract_2020_winter_file)

#2021

bike_tract_2021_summer_file=(bikeridership_path+'/bike_tract_2021_summer.csv')
bike_tract_2021_summer=pd.read_csv(bike_tract_2021_summer_file)

bike_tract_2021_fall_file=(bikeridership_path+'/bike_tract_2021_fall.csv')
bike_tract_2021_fall=pd.read_csv(bike_tract_2021_fall_file)

bike_tract_2021_spring_file=(bikeridership_path+'/bike_tract_2021_spring.csv')
bike_tract_2021_spring=pd.read_csv(bike_tract_2021_spring_file)

bike_tract_2021_winter_file=(bikeridership_path+'/bike_tract_2021_winter.csv')
bike_tract_2021_winter=pd.read_csv(bike_tract_2021_winter_file)

#2022

bike_tract_2022_summer_file=(bikeridership_path+'/bike_tract_2022_summer.csv')
bike_tract_2022_summer=pd.read_csv(bike_tract_2022_summer_file)

bike_tract_2022_fall_file=(bikeridership_path+'/bike_tract_2022_fall.csv')
bike_tract_2022_fall=pd.read_csv(bike_tract_2022_fall_file)

bike_tract_2022_spring_file=(bikeridership_path+'/bike_tract_2022_spring.csv')
bike_tract_2022_spring=pd.read_csv(bike_tract_2022_spring_file)

bike_tract_2022_winter_file=(bikeridership_path+'/bike_tract_2022_winter.csv')
bike_tract_2022_winter=pd.read_csv(bike_tract_2022_winter_file)

#2023

bike_tract_2023_summer_file=(bikeridership_path+'/bike_tract_2023_summer.csv')
bike_tract_2023_summer=pd.read_csv(bike_tract_2023_summer_file)

bike_tract_2023_fall_file=(bikeridership_path+'/bike_tract_2023_fall.csv')
bike_tract_2023_fall=pd.read_csv(bike_tract_2023_fall_file)

bike_tract_2023_spring_file=(bikeridership_path+'/bike_tract_2023_spring.csv')
bike_tract_2023_spring=pd.read_csv(bike_tract_2023_spring_file)

## EPA AQ Data
##only need CO, NO2, and Ozone for project
#CO - NEED

aq_co_path ='/mnt/c/Users/court/Documents/d3m_project/data/epa_aq_data/epa_aq_data_CO'

aq_co_2016_file=(aq_co_path+'/epa_aq_data_CO_2016.csv')
aq_co_2016 = pd.read_csv(aq_co_2016_file)

aq_co_2017_file=(aq_co_path+'/epa_aq_data_CO_2017.csv')
aq_co_2017 = pd.read_csv(aq_co_2017_file)

aq_co_2018_file=(aq_co_path+'/epa_aq_data_CO_2018.csv')
aq_co_2018 = pd.read_csv(aq_co_2018_file)

aq_co_2019_file=(aq_co_path+'/epa_aq_data_CO_2019.csv')
aq_co_2019 = pd.read_csv(aq_co_2019_file)

aq_co_2020_file=(aq_co_path+'/epa_aq_data_CO_2020.csv')
aq_co_2020 = pd.read_csv(aq_co_2020_file)

aq_co_2021_file=(aq_co_path+'/epa_aq_data_CO_2021.csv')
aq_co_2021 = pd.read_csv(aq_co_2021_file)

aq_co_2022_file=(aq_co_path+'/epa_aq_data_CO_2022.csv')
aq_co_2022 = pd.read_csv(aq_co_2022_file)

aq_co_2023_file=(aq_co_path+'/epa_aq_data_CO_2023.csv')
aq_co_2023 = pd.read_csv(aq_co_2023_file)

aq_co_2024_file=(aq_co_path+'/epa_aq_data_CO_2024.csv')
aq_co_2024 = pd.read_csv(aq_co_2024_file)

aq_co_2016_tract_file=(aq_co_path+'/epa_aq_CO_2016_tract.csv')
aq_co_tract_2016 = pd.read_csv(aq_co_2016_tract_file)

aq_co_2017_tract_file = (aq_co_path + '/epa_aq_CO_2017_tract.csv')
aq_co_tract_2017 = pd.read_csv(aq_co_2017_tract_file)

aq_co_2018_tract_file = (aq_co_path + '/epa_aq_CO_2018_tract.csv')
aq_co_tract_2018 = pd.read_csv(aq_co_2018_tract_file)

aq_co_2019_tract_file = (aq_co_path + '/epa_aq_CO_2019_tract.csv')
aq_co_tract_2019 = pd.read_csv(aq_co_2019_tract_file)

aq_co_2020_tract_file = (aq_co_path + '/epa_aq_CO_2020_tract.csv')
aq_co_tract_2020 = pd.read_csv(aq_co_2020_tract_file)

aq_co_2021_tract_file = (aq_co_path + '/epa_aq_CO_2021_tract.csv')
aq_co_tract_2021 = pd.read_csv(aq_co_2021_tract_file)

aq_co_2022_tract_file = (aq_co_path + '/epa_aq_CO_2022_tract.csv')
aq_co_tract_2022 = pd.read_csv(aq_co_2022_tract_file)

aq_co_2023_tract_file = (aq_co_path + '/epa_aq_CO_2023_tract.csv')
aq_co_tract_2023 = pd.read_csv(aq_co_2023_tract_file)

aq_co_2024_tract_file = (aq_co_path + '/epa_aq_CO_2024_tract.csv')
aq_co_tract_2024 = pd.read_csv(aq_co_2024_tract_file)
#NO2 - NEED
aq_NO2_path = '/mnt/c/Users/court/Documents/d3m_project/data/epa_aq_data/epa_aq_data_NO2'

aq_NO2_2016_file = (aq_NO2_path + '/epa_aq_data_NO2_2016_georeferenced.csv')
aq_NO2_2016 = pd.read_csv(aq_NO2_2016_file)

aq_NO2_2017_file = (aq_NO2_path + '/epa_aq_data_NO2_2017_georeferenced.csv')
aq_NO2_2017 = pd.read_csv(aq_NO2_2017_file)

aq_NO2_2018_file = (aq_NO2_path + '/epa_aq_data_NO2_2018_georeferenced.csv')
aq_NO2_2018 = pd.read_csv(aq_NO2_2018_file)

aq_NO2_2019_file = (aq_NO2_path + '/epa_aq_data_NO2_2019_georeferenced.csv')
aq_NO2_2019 = pd.read_csv(aq_NO2_2019_file)

aq_NO2_2020_file = (aq_NO2_path + '/epa_aq_data_NO2_2020_georeferenced.csv')
aq_NO2_2020 = pd.read_csv(aq_NO2_2020_file)

aq_NO2_2021_file = (aq_NO2_path + '/epa_aq_data_NO2_2021_georeferenced.csv')
aq_NO2_2021 = pd.read_csv(aq_NO2_2021_file)

aq_NO2_2022_file = (aq_NO2_path + '/epa_aq_data_NO2_2022_georeferenced.csv')
aq_NO2_2022 = pd.read_csv(aq_NO2_2022_file)

aq_NO2_2023_file = (aq_NO2_path + '/epa_aq_data_NO2_2023_georeferenced.csv')
aq_NO2_2023 = pd.read_csv(aq_NO2_2023_file)

aq_NO2_2024_file = (aq_NO2_path + '/epa_aq_data_NO2_2024_georeferenced.csv')
aq_NO2_2024 = pd.read_csv(aq_NO2_2024_file)

#Ozone - NEED
aq_ozone_path = '/mnt/c/Users/court/Documents/d3m_project/data/epa_aq_data/epa_aq_data_ozone'

aq_ozone_2016_file = (aq_ozone_path + '/epa_aq_data_ozone_2016_georeferenced.csv')
aq_ozone_2016 = pd.read_csv(aq_ozone_2016_file)

aq_ozone_2017_file = (aq_ozone_path + '/epa_aq_data_ozone_2017_georeferenced.csv')
aq_ozone_2017 = pd.read_csv(aq_ozone_2017_file)

aq_ozone_2018_file = (aq_ozone_path + '/epa_aq_data_ozone_2018_georeferenced.csv')
aq_ozone_2018 = pd.read_csv(aq_ozone_2018_file)

aq_ozone_2019_file = (aq_ozone_path + '/epa_aq_data_ozone_2019_georeferenced.csv')
aq_ozone_2019 = pd.read_csv(aq_ozone_2019_file)

aq_ozone_2020_file = (aq_ozone_path + '/epa_aq_data_ozone_2020_georeferenced.csv')
aq_ozone_2020 = pd.read_csv(aq_ozone_2020_file)

aq_ozone_2021_file = (aq_ozone_path + '/epa_aq_data_ozone_2021_georeferenced.csv')
aq_ozone_2021 = pd.read_csv(aq_ozone_2021_file)

aq_ozone_2022_file = (aq_ozone_path + '/epa_aq_data_ozone_2022_georeferenced.csv')
aq_ozone_2022 = pd.read_csv(aq_ozone_2022_file)

aq_ozone_2023_file = (aq_ozone_path + '/epa_aq_data_ozone_2023_georeferenced.csv')
aq_ozone_2023 = pd.read_csv(aq_ozone_2023_file)

aq_ozone_2024_file = (aq_ozone_path + '/epa_aq_data_ozone_2024_georeferenced.csv')
aq_ozone_2024 = pd.read_csv(aq_ozone_2024_file)

# #Pb
# aq_Pb_path = '/mnt/c/Users/court/Documents/d3m_project/data/epa_aq_data/epa_aq_data_Pb'

# aq_Pb_2016_file = (aq_Pb_path + '/epa_aq_data_Pb_2016_georeferenced.csv')
# aq_Pb_2016 = pd.read_csv(aq_Pb_2016_file)

#PM10
aq_PM10_path = '/mnt/c/Users/court/Documents/d3m_project/data/epa_aq_data/epa_aq_data_PM10'

aq_PM10_2016_file = (aq_PM10_path + '/epa_aq_data_PM10_2016_georeferenced.csv')
aq_PM10_2016 = pd.read_csv(aq_PM10_2016_file)

aq_PM10_2017_file = (aq_PM10_path + '/epa_aq_data_PM10_2017_georeferenced.csv')
aq_PM10_2017 = pd.read_csv(aq_PM10_2017_file)

aq_PM10_2018_file = (aq_PM10_path + '/epa_aq_data_PM10_2018_georeferenced.csv')
aq_PM10_2018 = pd.read_csv(aq_PM10_2018_file)

aq_PM10_2019_file = (aq_PM10_path + '/epa_aq_data_PM10_2019_georeferenced.csv')
aq_PM10_2019 = pd.read_csv(aq_PM10_2019_file)

aq_PM10_2020_file = (aq_PM10_path + '/epa_aq_data_PM10_2020_georeferenced.csv')
aq_PM10_2020 = pd.read_csv(aq_PM10_2020_file)

aq_PM10_2021_file = (aq_PM10_path + '/epa_aq_data_PM10_2021_georeferenced.csv')
aq_PM10_2021 = pd.read_csv(aq_PM10_2021_file)

aq_PM10_2022_file = (aq_PM10_path + '/epa_aq_data_PM10_2022_georeferenced.csv')
aq_PM10_2022 = pd.read_csv(aq_PM10_2022_file)

aq_PM10_2023_file = (aq_PM10_path + '/epa_aq_data_PM10_2023_georeferenced.csv')
aq_PM10_2023 = pd.read_csv(aq_PM10_2023_file)

aq_PM10_2024_file = (aq_PM10_path + '/epa_aq_data_PM10_2024_georeferenced.csv')
aq_PM10_2024 = pd.read_csv(aq_PM10_2024_file)

#PM25
aq_PM25_path = '/mnt/c/Users/court/Documents/d3m_project/data/epa_aq_data/epa_aq_data_PM25'

aq_PM25_2016_file = (aq_PM25_path + '/epa_aq_data_PM25_2016_georeferenced.csv')
aq_PM25_2016 = pd.read_csv(aq_PM25_2016_file)

aq_PM25_2017_file = (aq_PM25_path + '/epa_aq_data_PM25_2017_georeferenced.csv')
aq_PM25_2017 = pd.read_csv(aq_PM25_2017_file)

aq_PM25_2018_file = (aq_PM25_path + '/epa_aq_data_PM25_2018_georeferenced.csv')
aq_PM25_2018 = pd.read_csv(aq_PM25_2018_file)

aq_PM25_2019_file = (aq_PM25_path + '/epa_aq_data_PM25_2019_georeferenced.csv')
aq_PM25_2019 = pd.read_csv(aq_PM25_2019_file)

aq_PM25_2020_file = (aq_PM25_path + '/epa_aq_data_PM25_2020_georeferenced.csv')
aq_PM25_2020 = pd.read_csv(aq_PM25_2020_file)

aq_PM25_2021_file = (aq_PM25_path + '/epa_aq_data_PM25_2021_georeferenced.csv')
aq_PM25_2021 = pd.read_csv(aq_PM25_2021_file)

aq_PM25_2022_file = (aq_PM25_path + '/epa_aq_data_PM25_2022_georeferenced.csv')
aq_PM25_2022 = pd.read_csv(aq_PM25_2022_file)

aq_PM25_2023_file = (aq_PM25_path + '/epa_aq_data_PM25_2023_georeferenced.csv')
aq_PM25_2023 = pd.read_csv(aq_PM25_2023_file)

aq_PM25_2024_file = (aq_PM25_path + '/epa_aq_data_PM25_2024_georeferenced.csv')
aq_PM25_2024 = pd.read_csv(aq_PM25_2024_file)

#SO2
aq_SO2_path = '/mnt/c/Users/court/Documents/d3m_project/data/epa_aq_data/epa_aq_data_SO2'

aq_SO2_2016_file = (aq_SO2_path + '/epa_aq_data_SO2_2016_georeferenced.csv')
aq_SO2_2016 = pd.read_csv(aq_SO2_2016_file)

aq_SO2_2017_file = (aq_SO2_path + '/epa_aq_data_SO2_2017_georeferenced.csv')
aq_SO2_2017 = pd.read_csv(aq_SO2_2017_file)

aq_SO2_2018_file = (aq_SO2_path + '/epa_aq_data_SO2_2018_georeferenced.csv')
aq_SO2_2018 = pd.read_csv(aq_SO2_2018_file)

aq_SO2_2019_file = (aq_SO2_path + '/epa_aq_data_SO2_2019_georeferenced.csv')
aq_SO2_2019 = pd.read_csv(aq_SO2_2019_file)

aq_SO2_2020_file = (aq_SO2_path + '/epa_aq_data_SO2_2020_georeferenced.csv')
aq_SO2_2020 = pd.read_csv(aq_SO2_2020_file)

aq_SO2_2021_file = (aq_SO2_path + '/epa_aq_data_SO2_2021_georeferenced.csv')
aq_SO2_2021 = pd.read_csv(aq_SO2_2021_file)

aq_SO2_2022_file = (aq_SO2_path + '/epa_aq_data_SO2_2022_georeferenced.csv')
aq_SO2_2022 = pd.read_csv(aq_SO2_2022_file)

aq_SO2_2023_file = (aq_SO2_path + '/epa_aq_data_SO2_2023_georeferenced.csv')
aq_SO2_2023 = pd.read_csv(aq_SO2_2023_file)

aq_SO2_2024_file = (aq_SO2_path + '/epa_aq_data_SO2_2024_georeferenced.csv')
aq_SO2_2024 = pd.read_csv(aq_SO2_2024_file)

##SVI
SVI_Path = '/mnt/c/Users/court/Documents/d3m_project/data/SVI/MA_SVI/SocialVulnerabilityIndex'
            
svi_2000_file = (SVI_Path + '/Massachusetts_SVI_2000.csv')
svi_2000 =pd.read_csv(svi_2000_file)

svi_2010_file = (SVI_Path + '/Massachusetts_SVI_2010.csv')
svi_2010 =pd.read_csv(svi_2010_file)

svi_2014_file = (SVI_Path + '/Massachusetts_SVI_2014.csv')
svi_2014 =pd.read_csv(svi_2014_file)

svi_2016_file = (SVI_Path + '/Massachusetts_SVI_2016.csv')
svi_2016 =pd.read_csv(svi_2016_file)

svi_2018_file = (SVI_Path + '/Massachusetts_SVI_2018.csv')
svi_2018 =pd.read_csv(svi_2018_file)

svi_2020_file = (SVI_Path + '/Massachusetts_SVI_2020.csv')
svi_2020 =pd.read_csv(svi_2020_file)

svi_2022_file = (SVI_Path + '/Massachusetts_SVI_2022.csv')
svi_2022 =pd.read_csv(svi_2022_file)






# modify the blue bike data so it can be used in ArcGIS
# # Define the folder path
# bluebike_folder_path = '/mnt/c/Users/court/Documents/d3m_project/data/BlueBikes/bluebike_boston'
# output_folder = '/mnt/c/Users/court/Documents/d3m_project/data/BlueBikes/bluebike_boston_georeferenced'
# census_tracts_shapefile = '/mnt/c/Users/court/Documents/d3m_project/data/TIGER_lines/TIGER_lines_2024/tl_2024_25_tract/tl_2024_25_tract.shp'
# # Iterate over all files in the folder
# # for filename in os.listdir(bluebike_folder_path):
# #     # Check if the file is a CSV file
# #     if filename.endswith('.csv'):
# #         # Replace '-' with '_' in the filename
# #         new_filename = filename.replace('-', '_')
        
# #         # Get the full paths for the old and new filenames
# #         old_file_path = os.path.join(bluebike_folder_path, filename)
# #         new_file_path = os.path.join(bluebike_folder_path, new_filename)
        
# #         # Rename the file
# #         os.rename(old_file_path, new_file_path)
# #         print(f'Renamed: {filename} -> {new_filename}')
# # for filename in os.listdir(bluebike_folder_path):
# #     # Check if the file is a CSV file
# #     if filename.endswith('.csv'):
# #         # Construct the full file path
# #         file_path = os.path.join(bluebike_folder_path, filename)
        
# #         # Load the CSV file into a pandas DataFrame
# #         df = pd.read_csv(file_path)
        
# #         # Replace spaces with underscores in all column names
# #         df.columns = [col.replace(" ", "_") for col in df.columns]
        
# #         # Save the modified DataFrame back to CSV
# #         df.to_csv(file_path, index=False)
# #         print(f'Updated column names in: {filename}')

# # print("All files have been processed.")
# # Load the census tracts shapefile into a GeoDataFrame
# census_tracts_gdf = gpd.read_file(census_tracts_shapefile)
# # Ensure the output folder exists
# os.makedirs(output_folder, exist_ok=True)

# # Iterate over all CSV files in the bluebike folder
# for csv_file in os.listdir(bluebike_folder_path):
#     if csv_file.endswith('.csv'):
#         # Construct full file path
#         csv_path = os.path.join(bluebike_folder_path, csv_file)
        
#         # Read the CSV file
#         df = pd.read_csv(csv_path)
        
#         # Assuming the CSV has 'start_station_longitude' and 'start_station_latitude' columns
#         geometry = [Point(xy) for xy in zip(df['start_station_longitude'], df['start_station_latitude'])]
#         gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')  # Ensure CRS is set
        
#         # Perform spatial join with census tracts
#         joined_gdf = gpd.sjoin(gdf, census_tracts_gdf, how='inner', predicate='within')  # Use the GeoDataFrame, not the file path
        
#         # Drop the geometry column to save as CSV (optional, depending on your needs)
#         joined_df = pd.DataFrame(joined_gdf.drop(columns=['geometry']))
        
#         # Construct the output file name
#         base_name = os.path.splitext(csv_file)[0]
#         output_file_name = f"{base_name}_georeferenced.csv"
#         output_path = os.path.join(output_folder, output_file_name)
        
#         # Save the joined DataFrame to a new CSV file
#         joined_df.to_csv(output_path, index=False)
        
#         print(f"Processed and saved: {output_file_name}")

# print("All files have been processed.")