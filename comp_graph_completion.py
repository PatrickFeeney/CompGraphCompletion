
# For each edge of interest, grab subset of rows such that each side of the edge has data
# Reshape data so that each row indexes a unique combo of location and time
# Fit GP on the subset (grid search with validation set for kernel hyperparameters?)
# Save predictions and pickle model
# Visualize GP
