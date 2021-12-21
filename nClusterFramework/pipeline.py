import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import seaborn as sns
import sys
import re
import time

#prints INFO
info_verbose=False
debug_verbose=False
output_verbose=True #toggle automated output, prompted output is not effected


class Pipeline:
    """A collection of channels
    """
    num_feat = None
    channels = {}


class Channel:
    """Holds the data for a particular channel, as well as flags
    """
    data = None
    decay_type = "time" #time or length
    