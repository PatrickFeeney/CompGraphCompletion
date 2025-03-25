from pathlib import Path

import pandas as pd


col_names_to_vis_names = {
    "co": "Yearly Average Max 8-hour CO Concentration",
}


def load():
    root_path = Path("data/epa_aq_CO")
    years = list(range(2017, 2025))
    years.remove(2021)

    col_names = ["year", "tract", "co"]
    final_df = pd.DataFrame(columns=col_names)
    for year in years:
        tract_df = pd.read_csv(root_path / f"epa_aq_CO_{year}_tract.csv")
        measure_df = pd.read_csv(root_path / f"epa_aq_data_CO_{year}.csv")
        # Aggregate "Daily Max 8-hour CO Concentration" by "Site ID"
        measure_df = measure_df[["Site ID", "Daily Max 8-hour CO Concentration"]]\
            .groupby("Site ID").mean().reset_index()
        measure_df = measure_df.rename(columns={"Site ID": "Site_ID"})
        # Map census tract "tl_2024_25_tract_GEOID" to "Site_ID" CO
        joined_df = tract_df[["Site_ID", "tl_2024_25_tract_GEOID"]].merge(measure_df, on="Site_ID")
        joined_df = joined_df[["tl_2024_25_tract_GEOID", "Daily Max 8-hour CO Concentration"]]\
            .rename(columns={
                "tl_2024_25_tract_GEOID": "tract",
                "Daily Max 8-hour CO Concentration": "co"
            })
        joined_df["year"] = year
        final_df = pd.concat([final_df, joined_df[col_names]])
    return final_df
