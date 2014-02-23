import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
#!/usr/bin/python
from numpy import *
from pylab import *
from matplotlib import rc, rcParams


fname=sys.argv[1]

fopen= open(fname,'r')

at=[]
for i in fopen.readlines():
        a=i.split(',')
        at.append([float(a[0]),float(a[1])])


fig = plt.figure()
ax = fig.add_subplot(111)
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
x, y = at[0][0],  at[0][1]
line = plt.plot([0,x],[0,y], 'bs-',color ='yellow',linewidth=2.5, linestyle="--")
annotate(r'$d1$',
         xy=(x,y), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

x2, y2 = at[1][0],  at[1][1]
line, = plt.plot([0,x2],[0,y2], 'bs-', picker=5, color ='red',linewidth=2.5, linestyle="--")
annotate(r'$d2$',
         xy=(x2,y2), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

x3, y3 = at[2][0],  at[2][1]
line, = plt.plot([0,x3],[0,y3], 'bs-', picker=5, color ='green',linewidth=2.5, linestyle="--")
annotate(r'$d3$',
         xy=(x3,y3), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

x4, y4 = at[3][0],  at[3][1]
line, = plt.plot([0,x4],[0,y4], 'bs-', picker=5, color ='green',linewidth=2.5, linestyle="--")
annotate(r'$d4$',
         xy=(x4,y4), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))


qx, qy = at[4][0],  at[4][1]
line, = plt.plot([0,qx],[0, qy], 'bs-', picker=5,color ='cyan',linewidth=2.5, linestyle="--")
annotate(r'$q$',
         xy=(qx,qy), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))
 
grid(True)
savefig('image_plot_data.png')

plt.show()
exit

