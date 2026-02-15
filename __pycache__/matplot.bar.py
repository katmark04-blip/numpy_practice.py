import matplotlib.pyplot as plt
import numpy as np

cars= np.array(["toyota","rangerover","benz","dodge","brabus"])
cost= np.array([230,132,400,356,450])

### for plotting bar graphs ##
plt.bar(cars,cost,color="purple")
plt.tick_params(axis="both",colors="orange")
### for horizontal bar graph ##
#plt.barh(cars,cost)
plt.show()