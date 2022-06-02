#%%

import numpy as np
import scipy.signal as ss
from matplotlib import pyplot as plt

plt.close('all')

# guit inline plotting
# %matplotlib qt

def example_plot(ax, fontsize=8):
    ax.set_xticklabels('')
    ax.set_yticklabels('')
    ax.axis([-0.005, 0.24, -2.3, 2.9])

    
# generate original signal
step = 0.0005
t = np.arange(0, 0.5, step)
dc = 0
f1 = 34
f2 = 200


L = len(t)
sig = dc + np.sin(2*np.pi*f1*t) 
sig_plus_noise = sig + np.sin(2*np.pi*f2*t)

# iir low-pass filtering

#sos = ss.butter(8, 100, btype='low', output='sos', fs=1/step)
#lowpassed_sig = ss.sosfilt(sos, sig_plus_noise)
#
#sos = ss.butter(8, 100, btype='high', output='sos', fs=1/step)
#highpassed_sig = ss.sosfilt(sos, sig_plus_noise)

# alternatives
b_l, a_l = ss.butter(8, 150, btype='low', output='ba', fs=1/step)
lowpassed_sig = ss.lfilter(b_l, a_l, sig_plus_noise)

# frequency response
w_l, h_l = ss.freqz(b_l, a_l, fs=1/step)
mag_l = 20 * np.log10(abs(h_l))
angle_l = np.angle(h_l)
#angle_l = np.unwrap(np.angle(h_l))

# iir high-pass filtering
b_h, a_h = ss.butter(8, 70, btype='high', output='ba', fs=1/step)
highpassed_sig = ss.lfilter(b_h, a_h, sig_plus_noise)

# frequency response
w_h, h_h = ss.freqz(b_h, a_h, fs=1/step)
mag_h = 20 * np.log10(abs(h_h)) # magnitude
angle_h = np.angle(h_h)         # phase 

# plots of frequency responses
fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 8), constrained_layout=True)
ax1.plot(w_l, mag_l, 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax1.set_title('IIR Butterworth low-pass filters')
ax1_1 = ax1.twinx()
ax1_1.plot(w_l, angle_l, 'g')
ax1_1.set_ylabel('Angle (radians)', color='g')
ax1_1.axis('tight')
ax1_1.grid()

ax2.plot(w_h, 20 * np.log10(abs(h_h)), 'b')
ax2.set_ylabel('Amplitude [dB]', color='b')
ax2.set_xlabel('Frequency [rad/sample]')
ax2.set_title('IIR Butterworth low-pass filters')
ax2_1 = ax2.twinx()
ax2_1.plot(w_l, angle_l, 'g')
ax2_1.set_ylabel('Angle (radians)', color='g')
ax2_1.axis('tight')
ax2_1.grid()

# fir low-pass filtering
b_lfir = ss.firwin(20, 150, window='hamming', pass_zero='lowpass', fs=1/step)
lfir_sig = ss.lfilter(b_lfir, 1, sig_plus_noise)

w_lfir, h_lfir = ss.freqz(b_lfir, a=1, fs=1/step)
mag_lfir = 20 * np.log10(abs(h_lfir))
phase_lfir = np.angle(h_lfir)


# fir high-pass filtering
# you need odd number of points for high-pass filtering
b_hfir = ss.firwin(21, 70, window='hamming', pass_zero='highpass', fs=1/step)
hfir_sig = ss.lfilter(b_hfir, 1, sig_plus_noise)

w_hfir, h_hfir = ss.freqz(b_hfir, a=1, fs=1/step)
mag_hfir = 20 * np.log10(abs(h_hfir))
phase_hfir = np.angle(h_hfir)


fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 8), constrained_layout=True)
ax1.plot(w_lfir, mag_lfir, 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax1.set_title('FIR low-pass filters (Hamming window)')
ax1_1 = ax1.twinx()
ax1_1.plot(w_l, angle_l, 'g')
ax1_1.set_ylabel('Angle (radians)', color='g')
ax1_1.axis('tight')
ax1_1.grid()

ax2.plot(w_hfir, mag_hfir, 'b')
ax2.set_ylabel('Amplitude [dB]', color='b')
ax2.set_xlabel('Frequency [rad/sample]')
ax2.set_title('FIR high-pass filters (Hamming window)')
ax2_1 = ax2.twinx()
ax2_1.plot(w_hfir, phase_hfir, 'g')
ax2_1.set_ylabel('Angle (radians)', color='g')
ax2_1.axis('tight')
ax2_1.grid()


#%% plotting

# filter response

fig, axs = plt.subplots(4,1, constrained_layout = True)

axs[0].plot(t, sig, label='original_sig')
axs[1].plot(t, sig_plus_noise, label='noisy_sig')
axs[1].set_ylabel('Amplitude ($\mu$V)')

axs[2].plot(t, lowpassed_sig, label='noisy_sig')

axs[3].plot(t, highpassed_sig, label='noisy_sig')
axs[3].set_xlabel('Time (ms)')


for ax in axs:
    example_plot(ax)

plt.show()


