import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

y = np.loadtxt("Dat_1.txt")

# STFT
f, t, Zxx = sp.signal.stft(y, 512, nperseg=512 * 10, noverlap=512 * 9)
# 0.5-50 Hz
min_freq_index = np.argmax(f > 0.5)
max_freq_index = np.argmax(f > 50)
f = f[min_freq_index:max_freq_index]
Zxx = Zxx[min_freq_index:max_freq_index, :]

plt.figure(1)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=-1, vmax=10, shading='auto')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()


def FeatureExtract(t, f, Zxx):
    delta = np.array([], dtype=float)
    theta = np.array([], dtype=float)
    alpha = np.array([], dtype=float)
    beta = np.array([], dtype=float)
    abr = np.array([], dtype=float)
    tbr = np.array([], dtype=float)
    dbr = np.array([], dtype=float)
    tar = np.array([], dtype=float)
    dar = np.array([], dtype=float)
    dtabr = np.array([], dtype=float)
    for i in t:
        indices = np.where((f >= 0.5) & (f <= 4))[0]
        delta = np.append(delta, np.sum(Zxx[indices]))

        indices = np.where((f >= 4) & (f <= 8))[0]
        theta = np.append(theta, np.sum(Zxx[indices]))

        indices = np.where((f >= 8) & (f <= 13))[0]
        alpha = np.append(alpha, np.sum(Zxx[indices]))

        indices = np.where((f >= 13) & (f <= 30))[0]
        beta = np.append(beta, np.sum(Zxx[indices]))

        abr = alpha / beta
        tbr = theta / beta
        dbr = delta / beta
        tar = theta / alpha
        dar = delta / alpha
        dtabr = (alpha + beta) / (delta + theta)

    diction = {"delta": delta,
               "theta": theta,
               "alpha": alpha,
               "beta": beta,
               "abr": abr,
               "tbr": tbr,
               "dbr": dbr,
               "tar": tar,
               "dar": dar,
               "dtabr": dtabr
               }
    return diction


# feature = FeatureExtract(t, f, Zxx)
# plt.plot(feature['delta'])
# plt.show()
