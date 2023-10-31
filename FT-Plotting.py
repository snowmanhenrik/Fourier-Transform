import scipy as sp
import numpy as np
from scipy.io import *
from scipy import fftpack
from matplotlib import pyplot as plt
from decimal import Decimal
sample_rate,data = wavfile.read("")
raw_fft = fftpack.fft(data)
FFT = abs(raw_fft)


PSD = raw_fft * np.conj(raw_fft) / (len(raw_fft)/sample_rate)
freq_vector = fftpack.fftfreq(len(FFT),(1.0/sample_rate))

plt.plot(freq_vector[range(len(FFT)//2)],FFT[range(len(FFT)//2)])
plt.title("Frequency-Domain Plot")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Fourier Coefficient Modulus")
plt.show
