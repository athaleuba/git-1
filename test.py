print('ceci est un test')
import numpy as np
import matplotlib.pyplot as plt
A = np.ones((6, 7))
X = np.linspace(-np.pi, np.pi, 10000000)
Y = np.sin(X)
plt.plot(X, Y)
plt.show()
print('tudo bem')