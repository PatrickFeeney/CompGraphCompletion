from pathlib import Path
import pickle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

from data_load_2 import load_svi


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


def gp_fname(dataset1, col_name1, dataset2, col_name2):
    return f"{dataset1}_{col_name1}_{dataset2}_{col_name2}.dump"


def save_gp(gp: GaussianProcessRegressor, fname: str):
    with open(Path("./models") / Path(fname), "wb") as f:
        pickle.dump(gp, f)


def load_gp(fname: str):
    return pickle.load(open(Path("./models") / Path(fname), "rb"))


def vis_gp(X: np.ndarray, y, xlabel, ylabel, X_lin, mean_pred, std_pred):
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
    _ = plt.title("Gaussian Process Regression")
    plt.savefig(f"{xlabel}_{ylabel}.png")
    plt.close()


if __name__ == "__main__":
    df = load_svi()
    dataset1 = "svi"
    col_name1 = "minority"
    X = np.expand_dims(df[col_name1].to_numpy(), axis=1)
    for col_name in ["pov", "pov150"]:
        dataset2 = "svi"
        col_name2 = col_name
        y = df[col_name].to_numpy()
        # For each edge of interest, grab subset of rows such that each side of the edge has data
        mask = np.logical_not(np.logical_or(np.isnan(X)[:, 0], np.isnan(y)))
        mask_X = X[mask, :]
        mask_y = y[mask]
        # Reshape data so that each row indexes a unique combo of location and time
        # Divide data into train and test based on time
        # Fit GP on the subset (grid search with validation set for kernel hyperparameters?)
        gp = fit_gp(mask_X, mask_y)
        # or load the GP from a previous run
        # Save predictions and pickle model
        X_lin = vis_linspace(mask_X)
        mean_pred, std_pred = pred_gp(X_lin[:, None], gp)
        save_gp(gp, gp_fname(dataset1, col_name1, dataset2, col_name2))
        # Visualize GP
        vis_gp(mask_X, mask_y, "Minority %", col_name, X_lin, mean_pred, std_pred)
