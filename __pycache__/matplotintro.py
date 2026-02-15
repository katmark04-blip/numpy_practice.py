import matplotlib.pyplot as plt
import numpy as np


x = np.array([1,2,3,4,5])
y = np.array([12,26,38,43,51])

#### you can create a dictionary for line descritions so that you do not re write them ###
line_des= dict(marker="o",markersize=10,
                        markerfacecolor="#03fc0b",
                        markeredgecolor="#fc3503",
                        linestyle="dashdot",
                        linewidth=3,
                        color="#fc03db")

#plt.plot(x,y,marker="o",markersize=10,
 #                       markerfacecolor="#03fc0b",
 #                       markeredgecolor="#fc3503",
 #                       linestyle="dashdot",
  #                      linewidth=3,
   #                     color="#fc03db")
#plt.plot(x,y)

### you use >>>**<<< to call it out #####
plt.plot(x,y, **line_des)   
plt.show()