"""Configuration file for textgenerator.py
Contains a number of parameters used to adjust the model
"""

# ---------- Project information ---------------------------------------------
"""File path pointing to training data
"""
TRAINING_DATA_PATH = "C:\\Users\\daeur\\PycharmProjects\\mechanical\\Training Data"

"""Project name to be used in output file/folder naming and log files
"""
PROJECT_NAME = 'mechanical'  # Obviously currently a placeholder as default

# ---------- Basic parameters ------------------------------------------------

"""Number of training epochs
"""
EPOCHS = 25

"""Volatility of the prediction model.
Lower = more predictable, higher = more surprising.
This is a good number to tweak to change up results
"""
TEMPERATURE = 0.85

# ---------- Advanced settings -----------------------------------------------
# To be added in the future
