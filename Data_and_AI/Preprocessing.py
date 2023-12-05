import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
from sklearn.decomposition import PCA

y = np.loadtxt("Data/Subject_1_nhammat.txt")
mean = np.mean(y)
std = np.std(y)


# Design the band-pass filter


# Lọc mảng theo phân phối chuẩn
def filter_data(data):
    filtered_data = data[(np.abs(data) <= 256)]
    x = np.arange(len(filtered_data))
    interpolated_data = interp1d(x, filtered_data)(np.linspace(0, len(filtered_data) - 1, len(data)))
    return interpolated_data

# 0.5-50 Hz
# trim = np.where((f >= 0.5) & (f <= 50))[0]
# f = f[trim]
# Zxx = Zxx[trim, :]

plt.figure(0)
plt.plot(y)
#
# plt.figure(1)
# plt.pcolormesh(t, f, np.abs(Zxx), vmin=-1, vmax=10, shading='auto')
# plt.title('STFT Magnitude')
# plt.ylim(0.5, 50)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# print(Zxx.shape)

# plt.show()

def FeatureExtract(y):
    band = [0.5 / (0.5 * 512), 40 / (0.5 * 512)]
    b, a = sp.signal.butter(4, band, btype='band', analog=False, output='ba')
    y = sp.signal.lfilter(b, a, y)

    y = filter_data(y)
    f, t, Zxx = sp.signal.stft(y, 512, nperseg=512 * 10, noverlap=512 * 9)
    plt.figure(1)
    plt.pcolormesh(t, f, np.abs(Zxx), vmin=-1, vmax=10, shading='auto')
    plt.title('STFT Magnitude')
    plt.ylim(0.5, 50)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')

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
    for i in range(0, int(t[-1]) // 1):
        indices = np.where((f >= 0.5) & (f <= 4))[0]
        delta = np.append(delta, np.sum(np.abs(Zxx[indices, i])))

        indices = np.where((f >= 4) & (f <= 8))[0]
        theta = np.append(theta, np.sum(np.abs(Zxx[indices, i])))

        indices = np.where((f >= 8) & (f <= 13))[0]
        alpha = np.append(alpha, np.sum(np.abs(Zxx[indices, i])))

        indices = np.where((f >= 13) & (f <= 30))[0]
        beta = np.append(beta, np.sum(np.abs(Zxx[indices, i])))

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


feature = FeatureExtract(y)
plt.figure(2)
plt.plot(feature['delta'], label="delta")
plt.plot(feature['theta'], label="theta")
plt.plot(feature['alpha'], label="alpha")
plt.plot(feature['beta'], label="beta")
plt.legend()
# plt.show()
# df = pd.DataFrame.from_dict(feature)
# df.to_csv("test.csv")
# print(df)
