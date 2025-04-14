import itertools
from pathlib import Path
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

import data_load_aq
import data_load_bike
import data_load_svi


def fit_gp(X_train: np.ndarray, y_train: np.ndarray):
    """Fit GP to data

    Args:
        X_train (np.ndarray): Training data (N, F_in)
        y_train (np.ndarray): Target data (N,) or (N, F_out)

    Returns:
        GaussianProcessRegressor: GP fit to data
    """
    # what would produce zero mean unit variance?
    kernel = RBF(length_scale=X_train.shape[-1]*[0.5]) + \
        WhiteKernel(noise_level=0.5, noise_level_bounds=(1e-5, 1e1))
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=0, normalize_y=True)
    gp.fit(X_train, y_train)
    return gp


def pred_gp(X_lin: np.ndarray, gp: GaussianProcessRegressor):
    mean_pred, std_pred = gp.predict(X_lin, return_std=True)
    return mean_pred, std_pred


def vis_linspace(X: np.ndarray):
    X_range = X.max() - X.min()
    return np.linspace(X.min() - X_range * 0.1, X.max() + X_range * 0.1, 200)


def comparison_fname(dataset1, col_name1, dataset2, col_name2, extension):
    return f"{dataset1}_{col_name1}_{dataset2}_{col_name2}.{extension}"


def save_gp(gp: GaussianProcessRegressor, fname: str):
    with open(Path("./models") / Path(fname), "wb") as f:
        pickle.dump(gp, f)


def load_gp(fname: str):
    return pickle.load(open(Path("./models") / Path(fname), "rb"))


def vis_gp(X: np.ndarray, y, xlabel, ylabel, X_lin, mean_pred, std_pred, score, fname):
    plt.scatter(X, y, label="Observations")
    plt.plot(X_lin, mean_pred, label="Mean prediction")
    plt.fill_between(
        X_lin.ravel(),
        mean_pred - 1.96 * std_pred,
        mean_pred + 1.96 * std_pred,
        alpha=0.5,
        label=r"95% confidence interval",
    )
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    _ = plt.title(f"Test Coef. of Determination: {score:.3f}")
    plt.savefig(Path("./plots") / Path(fname), bbox_inches='tight')
    plt.close()


col_names_to_vis_names = {
    **data_load_aq.col_names_to_vis_names,
    **data_load_bike.col_names_to_vis_names,
    **data_load_svi.col_names_to_vis_names,
}


df_dict = {
    "aq": data_load_aq.load(),
    "bike": data_load_bike.load(),
    "svi": data_load_svi.load(),
}


if __name__ == "__main__":
    dataset_and_col = [
        ("svi", "minority"),
        ("svi", "pov"),
        ("svi", "pov150"),
        ("aq", "co"),
        ("bike", "count"),
    ]
    experiments = [(*d_c_1, *d_c_2) for d_c_1, d_c_2 in
                   itertools.permutations(dataset_and_col, r=2)]
    exp_to_scores = {}
    for experiment in experiments:
        dataset1, col_name1, dataset2, col_name2 = experiment
        # Use year and tract to merge
        if dataset1 != dataset2:
            X_df = df_dict[dataset1]
            y_df = df_dict[dataset2]
            merge_df = pd.merge(X_df, y_df, on=["year", "tract"])
        # Otherwise just use the shared dataframe
        else:
            merge_df = df_dict[dataset1]
        # For each edge of interest, grab subset of rows such that each side of the edge has data
        merge_df = merge_df[["year", col_name1, col_name2]].dropna(axis=0)
        # Skip rest of loop if not enough overlap
        if len(merge_df) == 0 or np.all(merge_df["year"] == max(merge_df["year"])):
            continue

        # Divide data into train and test based on time
        train_df = merge_df[merge_df["year"] < max(merge_df["year"])]
        test_df = merge_df[merge_df["year"] == max(merge_df["year"])]
        # Grab columns of interest
        X_train = np.expand_dims(train_df[col_name1].to_numpy(), axis=1)
        X_test = np.expand_dims(test_df[col_name1].to_numpy(), axis=1)
        y_train = train_df[col_name2].to_numpy()
        y_test = test_df[col_name2].to_numpy()

        # Fit GP on the train subset
        gp_fname = comparison_fname(dataset1, col_name1, dataset2, col_name2, "dump")
        if not (Path("./models") / Path(gp_fname)).exists():
            gp = fit_gp(X_train, y_train)
            save_gp(gp, gp_fname)
        # or load the GP from a previous run
        else:
            gp = load_gp(gp_fname)

        # Output predictions
        X_lin = vis_linspace(merge_df[col_name1])
        mean_pred, std_pred = pred_gp(X_lin[:, None], gp)
        score = gp.score(X_test, y_test)
        # Visualize GP
        vis_gp(X_test, y_test, col_names_to_vis_names[col_name1], col_names_to_vis_names[col_name2],
               X_lin, mean_pred, std_pred, score,
               comparison_fname(dataset1, col_name1, dataset2, col_name2, "png"))
        # Save score
        exp_to_scores[experiment] = score

    # Highlight scores greater than 0
    for exp, score in exp_to_scores.items():
        if score > 0:
            dataset1, col_name1, dataset2, col_name2 = exp
            print(f"{dataset1}_{col_name1}->{dataset2}_{col_name2} = {score}")
    # What gets printed as of 4/14/25:
    # svi_minority->svi_pov = 0.44056146329498413
    # svi_minority->svi_pov150 = 0.4085251814666093
    # svi_minority->bike_count = 0.06622401563512614
    # svi_pov->svi_minority = 0.48306124747153356
    # svi_pov150->svi_minority = 0.44676794127573227
    # aq_co->bike_count = 0.039877147364709264
