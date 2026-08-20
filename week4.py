import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([30, 40, 50, 60, 70])

model = LinearRegression()

model.fit(X, Y)

Y_pred = model.predict(X)

print("Coefficient (Slope):", model.coef_)
print("Intercept:", model.intercept_)

hours = np.array([6]).reshape(-1, 1)
prediction = model.predict(hours)

print("Predicted marks for 6 hours:", prediction[0])

plt.scatter(X, Y, color="blue", label="Actual Data")
plt.plot(X, Y_pred, color="red", label="Regression Line")

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.legend()

plt.show()
