from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from comp_graph_completion import col_names_to_vis_names, comparison_fname, load_gp, pred_gp
import data_load_bike
import data_load_svi


if __name__ == "__main__":
    merge_df_full = pd.merge(data_load_svi.load(), data_load_bike.load(), on=["year", "tract"])
    for col in ["pov", "pov150"]:
        merge_df = merge_df_full[["year", "count", "minority", col]].dropna(axis=0)
        # Divide data into train and test based on time
        test_df = merge_df[merge_df["year"] == max(merge_df["year"])]
        # Grab columns of interest
        X_test_1 = np.expand_dims(test_df[col].to_numpy(), axis=1)
        X_test_2 = np.expand_dims(test_df["minority"].to_numpy(), axis=1)
        y_test_2 = test_df["count"].to_numpy()
        # Load GPs
        gp_1 = load_gp(comparison_fname("svi", col, "svi", "minority", "dump"))
        gp_2 = load_gp(comparison_fname("svi", "minority", "bike", "count", "dump"))
        # Chained GP predictions
        mean_pred_1, _ = pred_gp(X_test_1, gp_1)
        mean_pred_2, std_pred_2 = pred_gp(mean_pred_1[:, None], gp_2)
        # Calculate score
        u = ((y_test_2 - mean_pred_2) ** 2).sum()
        v = ((y_test_2 - y_test_2.mean()) ** 2).sum()
        score = 1 - u/v
        # Visualize
        plt.scatter(X_test_2, y_test_2, label="Observations")
        sort_ind = np.argsort(mean_pred_1)
        plt.plot(mean_pred_1[sort_ind], mean_pred_2[sort_ind], label="Mean prediction")
        plt.fill_between(
            mean_pred_1[sort_ind],
            mean_pred_2[sort_ind] - 1.96 * std_pred_2[sort_ind],
            mean_pred_2[sort_ind] + 1.96 * std_pred_2[sort_ind],
            alpha=0.5,
            label=r"95% confidence interval",
        )
        plt.legend()
        plt.xlabel(col_names_to_vis_names["minority"])
        plt.ylabel(col_names_to_vis_names["count"])
        _ = plt.title(f"Chained Test Coef. of Determination: {score:.3f}")
        plt.savefig(Path("./plots") / Path(f"chain_{col}_minority_count.png"), bbox_inches='tight')
        plt.close()
