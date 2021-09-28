print('ceci est un test')
import numpy as np
import matplotlib.pyplot as plt
A = np.ones((6, 7))
print(A)
X = np.linspace(-np.pi, np.pi, 100)
Y = np.sin(X)
plt.plot(X, Y)
plt.show()