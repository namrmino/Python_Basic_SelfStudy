import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randn
import numpy as np
import seaborn as sns

x = np.random.rand(3, 1) # 0~1
np.random.randn(2, 1) # 정규분

x = np.arange(0.00001, 3, 0.01)
np.random.shuffle(x)



X_b = np.c_[np.ones((100, 1)), X]