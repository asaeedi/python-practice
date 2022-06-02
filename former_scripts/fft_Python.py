import numpy as np
from numpy import pi

f_samp = 1000
step = 1/f_samp
t = np.arange(0, 1, step)
L = t.size
f = 5
dc = 0.5
sig = dc + np.cos(2*pi*f*t)

# calculate the spectrum
S = np.abs(np.fft.fft(sig))/L
# coefficient corrections
S[1:-2] = 2*S[1:-2]
S_ss = S[0:int(L/2)]
S = np.fft.fftshift(S)

freqs = f_samp*np.arange(int(-L/2), int(L/2))/L
freq_ss = f_samp*np.arange(0, int(L/2))/L

# plot the signal
from matplotlib import pyplot as pl
# plot time signal
pl.figure('Signal in time and frequency domain')
pl.subplot(311)
pl.plot(t, sig)
pl.xlabel('Time (s)')
pl.ylabel('Amplitude (mV)')
#pl.yticks([-0.5, 0, 0.5, 1, 1.5])
pl.show()

# plot double-sided fft
pl.subplot(312)
pl.stem(freqs, S)
pl.axis([-20, 20, -0.2, 1.1])
pl.xlabel('Frequency (Hz)')
pl.ylabel('Amplitude (mV)')
pl.show()

pl.subplot(313)
pl.stem(S_ss)
pl.axis([-2, 10, -0.2, 1.1])
pl.xlabel('Frequency (Hz)')
pl.ylabel('Amplitude (mV)')
pl.show()
