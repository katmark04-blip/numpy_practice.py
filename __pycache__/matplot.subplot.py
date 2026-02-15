import matplotlib.pyplot as plt
import numpy as np

x= np.array([2,4,6,8])

figure,axes = plt.subplots(2,2)
axes[0,0].bar(x,x*2)
axes[0,0].set_title("gragh 1")
axes[0,1].scatter(x,x**3,color="red")
axes[0,1].set_title("gragh 2",color="red")
axes[1,0].plot(x,x**4,color="yellow")
axes[1,0].set_title("gragh 3",color="yellow")
axes[1,1].plot(x,x**5,color="green")
axes[1,1].set_title("gragh 4",color="green")
### we use >>plt.tight_layout() <<< to make sure data doesnt overlap
plt.tight_layout()
plt.show()