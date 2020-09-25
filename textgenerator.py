"""TensorFlow text generation model for use by mechanical.py
Currently uses a single model but this will probably eventually be expanded
to have multiple model options, either selected in textgen_config.py or
passed as an argument to the TextGenerator class constructor.

Adapted from my project Pynk Floyd found here:
https://github.com/christopher-fisher/pynk_floyd
"""

import tensorflow as tf
import numpy as np
import os
import time

from textgen_config import *

class TextGenerator:
    """Text generating recurrent neural network.
    """

    def __init__(self, trainingdata):
        self.trainingdata = trainingdata