import numpy as np
import matplotlib.pyplot as plt
from dydwt import DyDWT

#2次スプライン係数
h = [0, 0.125, 0.375, 0.375, 0.125, 0]
g = [0, 0, -0.5, 0.5, 0, 0]

t = np.linspace(-5, 5, 16) 
f = np.sin(t)

test = DyDWT(h, g, cenH=2, cenG=2)
a, d = test.translate(f, 1)

plt.subplots_adjust(wspace=0.4, hspace=0.6)
plt.subplot(3, 1, 1)
plt.title("target = sin(t)")
plt.scatter(t, f)

plt.subplot(3, 1, 2)
plt.title("low frequency component")
plt.scatter(t, a)

plt.subplot(3, 1, 3)
plt.title("high frequency component")
plt.scatter(t, d)

plt.show()