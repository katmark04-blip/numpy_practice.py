import matplotlib.pyplot as plt
import numpy as np

items = np.array(["cups","bottles","rulers","pens","books"])
amount = np.array([12,22,51,63,42])
color =["orange","yellow","red","green","blue"]


plt.title("school items",fontweight="bold")
plt.pie(amount,labels=items,
        autopct="%.1f%%",
        colors=color,
        explode=[0,0,0.1,0,0.1],
        shadow=True,
        startangle=270)


plt.show()