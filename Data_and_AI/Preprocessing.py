import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def filter_data(data):
    # Bandpass filter
    band = [0.5 / (0.5 * 512), 40 / (0.5 * 512)]
    b, a = sp.signal.butter(4, band, btype='band', analog=False, output='ba')
    data = sp.signal.lfilter(b, a, data)

    plt.hist(data, bins=10, edgecolor='black')
    # filter for EMG by interpolated
    filtered_data = data[(np.abs(data) <= 256)]
    x = np.arange(len(filtered_data))
    interpolated_data = interp1d(x, filtered_data)(np.linspace(0, len(filtered_data) - 1, len(data)))
    return interpolated_data


def FeatureExtract(data, plot):
    f, t, Zxx = sp.signal.stft(data, 512, nperseg=512 * 10, noverlap=512 * 9)
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
    for i in range(0, int(t[-1])):
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
    # if plot == 1:
    #     # Tạo hình ảnh chính và các hình ảnh con
    #     fig = plt.figure(figsize=(12, 6))
    #
    #     # Plot raw
    #     ax1 = fig.add_subplot(2, 2, 1)
    #     ax1.plot(data)
    #     ax1.set_title('EEG Raw Values')
    #     ax1.set_xlabel('Samples')
    #     ax1.set_ylabel('RawValue')
    #
    #     # Plot STFT
    #     ax2 = fig.add_subplot(1, 2, 2)
    #     ax2.pcolormesh(t, f, np.abs(Zxx), vmin=-1, vmax=10, shading='auto')
    #     ax2.set_title('STFT Magnitude')
    #     ax2.set_xlabel('Time [sec]')
    #     ax2.set_ylabel('Frequency [Hz]')
    #     ax2.set_ylim(0.5, 40)
    #
    #     # Plot brainwave
    #     ax3 = fig.add_subplot(2, 2, 3)
    #     ax3.plot(diction['delta'], label="delta")
    #     ax3.plot(diction['theta'], label="theta")
    #     ax3.plot(diction['alpha'], label="alpha")
    #     ax3.plot(diction['beta'], label="beta")
    #     ax3.set_title('Frequency Bands')
    #     ax3.set_xlabel('Power')
    #     ax3.set_ylabel('Time [sec]')
    #     ax3.legend()
    #
    #     # Hiển thị hình ảnh
    #     plt.tight_layout()
    #     # plt.show()
    return diction


# y = np.loadtxt("Data_Iso/Subject_1_nm_15Hz.txt")
# y = filter_data(y)
# FeatureExtract(y, plot=1)
#
# y1 = np.loadtxt("Data_Iso/Subject_1_nm_30Hz.txt")
# y1 = filter_data(y1)
# FeatureExtract(y1, plot=1)
# plt.show()