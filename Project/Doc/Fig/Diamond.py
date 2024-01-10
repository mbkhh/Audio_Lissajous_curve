import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

duration = 10  
sampling_freq = 44100  
t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)


"""
	--------Diamond--------
"""
cycle_duration = .001
amplitude = 1.0
signalY = np.zeros_like(t)
signalX = np.zeros_like(t)
num_samples = int(duration * sampling_freq)
for i in range(num_samples):
    time_in_cycle = t[i] % cycle_duration
    if time_in_cycle < cycle_duration / 4:
        signalY[i] = 1
    elif time_in_cycle < 2*cycle_duration / 4:
        signalY[i] = 0
    elif time_in_cycle < 3*cycle_duration / 4:
        signalY[i] = -1
    else :
        signalY[i] = 0
for i in range(num_samples):
    time_in_cycle = t[i] % cycle_duration
    if time_in_cycle < cycle_duration / 4:
        signalX[i] = 0
    elif time_in_cycle < 2*cycle_duration / 4:
        signalX[i] = -1
    elif time_in_cycle < 3*cycle_duration / 4:
        signalX[i] = 0
    else :
        signalX[i] = 1


stereo_signal = np.column_stack(( signalX , signalY))

sd.play(stereo_signal, samplerate=sampling_freq, blocking=True)
