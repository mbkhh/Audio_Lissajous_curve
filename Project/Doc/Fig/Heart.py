import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

duration = 10  
sampling_freq = 44100  
t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)

"""
	--------Heart--------
"""

signalX = 16*(np.sin(2 * np.pi * 1000 * t)**3)
signal1 = 13*np.cos(2 * np.pi * 1000 * t)
signal2 = -5*np.cos(2 * np.pi * 2000 * t)
signal3 = -2*np.cos(2 * np.pi * 3000 * t)
signal4 = -1*np.cos(2 * np.pi * 4000 * t)
signalY = signal1 + signal2 + signal3 + signal4
signalY /= np.max(np.abs(signalY))
signalX /= np.max(np.abs(signalX))

stereo_signal = np.column_stack(( signalX , signalY))

sd.play(stereo_signal, samplerate=sampling_freq, blocking=True)

