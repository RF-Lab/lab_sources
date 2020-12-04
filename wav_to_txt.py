# -*- coding: utf-8 -*-
"""
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy import signal

fs, x = wavfile.read('./v21_tmp3.wav')

print('x fs is {} Hz, x.shape= {}'.format( fs, x.shape ))

f = signal.resample(x, len(x)*int(16000/fs))

print('f.shape= {}'.format( f.shape ))

np.savetxt( 'x_modem_16000.txt', f, fmt='%d' )

frex,Pxx     = signal.welch( f )
plt.semilogy( frex,Pxx )