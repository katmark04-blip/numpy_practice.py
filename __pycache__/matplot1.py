import matplotlib.pyplot as plt
import numpy as np

x= np.array([120,240,35,430,516])
y= np.array([171,381,292,520,319])
v= np.array([202,102,422,623,324])
z= np.array([123,243,156,400,500])

### dealing with labels ###
plt.title("MARK DATA",color="brown",fontsize=30,fontweight="bold")

#### for ticks color we selected colors not color for both ###
plt.tick_params(axis=("both"), colors="#0307fc")
plt.xlabel("amount of money",color="red",fontsize=10,fontweight="bold")
plt.ylabel("no of women",color="green",fontsize=10,fontweight="bold")

### for grind lines ##
plt.grid(axis="x")
#plt.grid(axis="both",color="orange")

plt.plot(x,y,color="black")
plt.plot(v,z)
plt.show()
