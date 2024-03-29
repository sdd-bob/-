import numpy as np
import matplotlib.pyplot as plt
labels ='Frogs','Hogs','Dogs','Logs'
colors = ['yellowgreen','gold','#FF0000','lightcoral']
explode = (0, 0.1, 0, 0.1)
fig = plt.figure()
ax = fig.gca()
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90,radius=0.25, center=(0, 0), frame=True) 
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=45,radius=0.25, center=(1, 1), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90,radius=0.25, center=(0, 1), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,autopct='%1.2f%%', shadow=False, startangle=135,radius=0.35, center=(1, 0), frame=True)
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["Sunny","Cloudy"])
ax.set_yticklabels(["Dry","Rainy"])
ax.set_xlim((-0.5, 1.5)) 
ax.set_ylim((-0.5, 1.5))
ax.set_aspect('equal') 
plt.show()