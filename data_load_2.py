from pathlib import Path

import numpy as np
import pandas as pd

svi_file_to_col_names_to_svi_col = {
    "Massachusetts_SVI_2000.csv": {
        "tract": "FIPS",
        "pov": "G1V1R",
        "minority": "G3V1R",
    },
    "Massachusetts_SVI_2010.csv": {
        "tract": "FIPS",
        "pov": "E_P_POV",
        "minority": "P_MINORITY",
    },
    "Massachusetts_SVI_2014.csv": {
        "tract": "FIPS",
        "pov": "EP_POV",
        "minority": "EP_MINRTY",
    },
    "Massachusetts_SVI_2016.csv": {
        "tract": "FIPS",
        "pov": "EP_POV",
        "minority": "EP_MINRTY",
    },
    "Massachusetts_SVI_2018.csv": {
        "tract": "FIPS",
        "pov": "EP_POV",
        "minority": "EP_MINRTY",
    },
    # shift to 150% poverty level
    "Massachusetts_SVI_2020.csv": {
        "tract": "FIPS",
        "pov150": "EP_POV150",
        "minority": "EP_MINRTY",
    },
    "Massachusetts_SVI_2022.csv": {
        "tract": "FIPS",
        "pov150": "EP_POV150",
        "minority": "EP_MINRTY",
    },
}


def load_svi():
    root_path = Path("data/SocialVulnerabilityIndex")
    years = [2000, 2010, 2014, 2016, 2018, 2020, 2022]

    col_names = ["year", "tract", "pov", "pov150", "minority"]
    final_df = pd.DataFrame(columns=col_names)
    for year in years:
        fname = f"Massachusetts_SVI_{year}.csv"
        df = pd.read_csv(root_path / fname)
        df["year"] = year
        df = df.rename(columns={
            svi_name: col_name
            for col_name, svi_name in svi_file_to_col_names_to_svi_col[fname].items()})
        # append any columns present in the current df to final_df
        final_df = pd.concat([final_df, df[list(set(col_names) & set(df.columns))]])
    final_df = final_df.replace(-999.0, np.nan)
    return final_df


def col_intersection(fpaths):
    # finds and prints the intersection of column names across CSV files
    col_names_set = None
    for fpath in fpaths:
        df = pd.read_csv(fpath)
        if col_names_set is None:
            col_names_set = set(df.columns)
        else:
            col_names_set = col_names_set & set(df.columns)
    col_names = list(col_names_set)
    print(col_names)


if __name__ == "__main__":
    load_svi()
