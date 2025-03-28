from pathlib import Path

import numpy as np
import pandas as pd

bike_file_to_col_names_to_location_col = {

    "bike_tract_2016_fall.csv": {
        "location": "Neighborho",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2016_summer.csv": {
        "location": "Neighborho",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2017_fall.csv": {
        "location": "Neighborho",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2018_fall.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2018_summer.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2019_fall.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2019_summer.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2020_fall.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2020_spring.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2020_summer.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2020_winter.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2021_fall.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2021_spring.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2021_summer.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2021_winter.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2022_fall.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2022_spring.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2022_summer.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2022_winter.csv": {
        "location": "Location",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2023_fall.csv": {
        "location": "Location_Name",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2023_spring.csv": {
        "location": "Location_Name",
        "tract":"tl_2024_25_tract_GEOID",
    },
    "bike_tract_2023_summer.csv": {
        "location": "Location_Name",
        "tract":"tl_2024_25_tract_GEOID",
    },
    
}


