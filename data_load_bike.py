from pathlib import Path

import pandas as pd

col_names_to_vis_names = {
    "count": "Yearly Average Daily Bike Count",
}

bike_file_to_col_names_to_bike_col = {
    "bikeridership_boston_2016/bikeridership_boston_2016_fall_georeferenced.csv": {
        "location": "Neighborho",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2016/bikeridership_boston_2016_summer_georeferenced.csv": {
        "location": "Neighborho",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2017/bikeridership_boston_2017_fall_georeferenced.csv": {
        "location": "Neighborho",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2018/bikeridership_boston_2018_fall_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2018/bikeridership_boston_2018_summer_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2019/bikeridership_boston_2019_fall_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2019/bikeridership_boston_2019_summer_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2020/bikeridership_boston_2020_fall_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Bikes", "Day2Bikes"],
    },
    "bikeridership_boston_2020/bikeridership_boston_2020_spring_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Bikes", "Day2Bikes"],
    },
    "bikeridership_boston_2020/bikeridership_boston_2020_summer_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Bikes", "Day2Bikes"],
    },
    "bikeridership_boston_2020/bikeridership_boston_2020_winter_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Bikes", "Day2Bikes"],
    },
    "bikeridership_boston_2021/bikeridership_boston_2021_fall_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Total", "Day2Total"],
    },
    "bikeridership_boston_2021/bikeridership_boston_2021_spring_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Total", "Day2Total"],
    },
    "bikeridership_boston_2021/bikeridership_boston_2021_summer_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Total", "Day2Total"],
    },
    "bikeridership_boston_2021/bikeridership_boston_2021_winter_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Total", "Day2Total"],
    },
    "bikeridership_boston_2022/bikeridership_boston_2022_fall_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Total", "Day2Total"],
    },
    "bikeridership_boston_2022/bikeridership_boston_2022_spring_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Total", "Day2Total"],
    },
    "bikeridership_boston_2022/bikeridership_boston_2022_summer_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Total", "Day2Total"],
    },
    "bikeridership_boston_2022/bikeridership_boston_2022_winter_georeferenced.csv": {
        "location": "Location",
        "tract": "tl_2024_25_tract_GEOID",
        "count": ["Day1Total", "Day2Total"],
    },
    "bikeridership_boston_2023/bikeridership_boston_2023_fall_georeferenced.csv": {
        "location": "Location_Name",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2023/bikeridership_boston_2023_spring_georeferenced.csv": {
        "location": "Location_Name",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
    "bikeridership_boston_2023/bikeridership_boston_2023_summer_georeferenced.csv": {
        "location": "Location_Name",
        "tract": "tl_2024_25_tract_GEOID",
        "count": "DayBikes",
    },
}


def load():
    root_path = Path("data/bikeridership_boston")
    years = list(range(2016, 2024))

    col_names = ["year", "tract", "count"]
    final_df = pd.DataFrame(columns=col_names)
    for year in years:
        year_df = pd.DataFrame()
        last_fname = None  # track last working fname to enable dict lookups later
        for season in ["fall", "winter", "spring", "summer"]:
            fname = f"bikeridership_boston_{year}/bikeridership_boston_{year}_{season}_georeferenced.csv"
            if (root_path / fname).exists():
                last_fname = fname
                df = pd.read_csv(root_path / fname)
                df = df.rename(columns={
                    bike_file_to_col_names_to_bike_col[fname]["location"]: "location",
                    bike_file_to_col_names_to_bike_col[fname]["tract"]: "tract",
                })
                df["year"] = year
                season_col_names = col_names[:2]
                if type(bike_file_to_col_names_to_bike_col[fname]["count"]) is list:
                    season_col_names += bike_file_to_col_names_to_bike_col[fname]["count"]
                else:
                    season_col_names += [bike_file_to_col_names_to_bike_col[fname]["count"]]
                year_df = pd.concat([year_df, df[season_col_names]])
        # take mean over the year per tract
        year_df_mean = year_df.groupby("tract").mean().reset_index()
        if type(bike_file_to_col_names_to_bike_col[last_fname]["count"]) is list:
            year_df_mean["count"] = year_df_mean[
                bike_file_to_col_names_to_bike_col[last_fname]["count"]].mean(axis=1)
        else:
            year_df_mean = year_df_mean.rename(columns={
                bike_file_to_col_names_to_bike_col[last_fname]["count"]: "count"})
        # append the current df to final_df
        final_df = pd.concat([final_df, year_df_mean[col_names]])
    return final_df
