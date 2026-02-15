import matplotlib.pyplot as plt
import numpy as np

x1= np.array([12,21,31,35,42,])
y1= np.array([22,31,41,55,52,])

x2= np.array([22,34,41,55,62,])
y2= np.array([32,46,51,65,62,])

plt.scatter(x1,y1,color="green",
                alpha=0.5,
                label="type A")
plt.scatter(x2,y2,color="brown",
                alpha=0.5,
                label="type B")
plt.xlabel("numbers")
plt.ylabel("items")
plt.tick_params(axis="both",colors="red")
plt.legend()

plt.show()