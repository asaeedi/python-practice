import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np


def modify_plot(fig):
    for i, ax in enumerate(fig.axes):
        #ax.text(0.5, 0.5, "ax%d" %(i+1), va='center', ha='center')
        ax.tick_params(labelbottom=False, labelleft=False)
        ax.plot(np.linspace(0, 1, 100), np.random.normal(0.5, 0.5, 100))        

gs = GridSpec(2, 2, width_ratios=[1,3], height_ratios=[2,5] )

fig = plt.figure()
fig.suptitle('Using GridSpec to make fancy subplots')

ax0 = fig.add_subplot(gs[0])
ax1 = fig.add_subplot(gs[1])
ax2 = fig.add_subplot(gs[2])
ax3 = fig.add_subplot(gs[3])

modify_plot(fig)

plt.show()

gs = GridSpec(3, 3)

fig = plt.figure()
fig.suptitle('Using GridSpec to make fancy subplots')

ax1 = fig.add_subplot(gs[0,:])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, 2])
ax4 = fig.add_subplot(gs[2, 0])
ax5 = fig.add_subplot(gs[2, 1])

modify_plot(fig)

plt.show()
