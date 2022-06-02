# Curve fitting
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

def func(x, a, b, c):
    return a + np.exp(x/b) + np.exp(x/c)

step = 0.01
t = np.arange(0, 2, step)
dc = -0.4
T1 = 0.8
T2 = 2

# noisy signal
sig = dc + np.exp(-t/T1) + np.exp(t/T2) + 0.3*np.random.normal(0.9, 0.2, size=t.size)

popt, pcov = curve_fit(func, t, sig, bounds=([-np.inf, -np.inf, 0], [np.inf, 0, np.inf]))


plt.figure('test_figure', figsize=(8, 8), dpi=200)

plt.subplot2grid((2,2), (0,0), colspan=2)
plt.plot(t, sig, label='data')
plt.plot(t, func(t, *popt), 'r-', label='fit')
plt.legend(loc = 'lower right')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude ($\mu$V)')
plt.subplot2grid((2,2), (1,0))
plt.plot(t, sig - func(t, *popt), 'k')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude ($\mu$V)')

plt.subplot2grid((2,2), (1,1))
plt.plot(t, abs(sig - func(t, *popt)), 'k')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude ($\mu$V)')

#plt.subplots_adjust(left=0.1, bottom=0.2, right=1.5, top=1.5, wspace=0.24, hspace=0.3)
plt.savefig("test_figure.png")

# plt.show() should be always the last line associated with a plot
plt.show()
