import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([30, 40, 50, 60, 70])

model = LinearRegression()

model.fit(X, Y)
