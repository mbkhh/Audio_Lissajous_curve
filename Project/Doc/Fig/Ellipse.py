import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

duration = 10  
sampling_freq = 44100  
t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)

"""
	--------Elipse--------
"""
signalX = np.cos(2 * np.pi * 20000 * t);
signalY = .3*np.sin(2 * np.pi * 20000 * t);



stereo_signal = np.column_stack(( signalX , signalY))

sd.play(stereo_signal, samplerate=sampling_freq, blocking=True)
