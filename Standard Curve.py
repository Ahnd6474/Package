from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np

X_axis='O.D. 600'
Y_axis='CFU/ml'

x=np.array([1,2,3,4,5])
y=np.array([1.1,1.9,3.1,4,5.1])
slope, intercept, r, p, se = linregress(x, y)

print(f'y = {slope:.3f}x + {intercept:.3f}')

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label=f'y = {slope:.3f}x + {intercept:.3f}, R^2={r**2:.3f}')

plt.xlabel(X_axis)

# Set the y-axis label
plt.ylabel(Y_axis)
plt.legend()
plt.show()