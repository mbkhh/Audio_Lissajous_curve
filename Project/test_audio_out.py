# import winsound
# winsound.Beep(18000, 5000)

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

duration = 10  
sampling_freq = 44100  
t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)

# Generate the left channel signal



"""
	--------Circle--------
"""
signalX = np.cos(2 * np.pi * 20000 * t);
signalY = np.sin(2 * np.pi * 20000 * t);


"""
	--------Elipse--------
"""
signalX = np.cos(2 * np.pi * 20000 * t);
signalY = .3*np.sin(2 * np.pi * 20000 * t);


#signalX = 5*(np.sin(2 * np.pi * 400 * t)**3)
#signal1 = 2*np.cos(2 * np.pi * 400 * t)
#signal2 = -1.3*np.cos(2 * np.pi * 800 * t)
#signal3 = -0.6*np.cos(2 * np.pi * 1200 * t)
#signal4 = -0.4*np.cos(2 * np.pi * 1600 * t)
#
#signalY = signal1 + signal2 + signal3 + signal4
#signalY /= np.max(np.abs(signalY))
#
#signalX /= np.max(np.abs(signalX))


"""
	--------Heart--------
"""
#signalX = 16*(np.sin(2 * np.pi * 1000 * t)**3)
#signal1 = 13*np.cos(2 * np.pi * 1000 * t)
#signal2 = -5*np.cos(2 * np.pi * 2000 * t)
#signal3 = -2*np.cos(2 * np.pi * 3000 * t)
#signal4 = -1*np.cos(2 * np.pi * 4000 * t)
#signalY = signal1 + signal2 + signal3 + signal4
#signalY /= np.max(np.abs(signalY))
#signalX /= np.max(np.abs(signalX))


"""
	--------Square--------
"""
#cycle_duration = .001
#amplitude = 1.0
#signalY = np.zeros_like(t)
#signalX = np.zeros_like(t)
#num_samples = int(duration * sampling_freq)
#for i in range(num_samples):
#    time_in_cycle = t[i] % cycle_duration
#    if time_in_cycle < cycle_duration / 4:
#        signalY[i] = 1
#    elif time_in_cycle < 2*cycle_duration / 4:
#        signalY[i] = 0
#    elif time_in_cycle < 3*cycle_duration / 4:
#        signalY[i] = -1
#    else :
#        signalY[i] = 0
#for i in range(num_samples):
#    time_in_cycle = t[i] % cycle_duration
#    if time_in_cycle < cycle_duration / 4:
#        signalX[i] = 0
#    elif time_in_cycle < 2*cycle_duration / 4:
#        signalX[i] = -1
#    elif time_in_cycle < 3*cycle_duration / 4:
#        signalX[i] = 0
#    else :
#        signalX[i] = 1
#signalY = np.zeros_like(t)
#sign = 1;
#for x in range(1,100):
#	if(x%2 == 1):
#		signalY += (sign*np.cos(2 * np.pi * 100 *x* t))/x**2
#		sign*=-1;

#signalX = np.cos(2 * np.pi * 20000 * t);




stereo_signal = np.column_stack(( signalX , signalY))

# Play the stereo signal

#plt.plot(t, signalY)
#plt.xlabel('f')
#plt.ylabel('y')
#plt.title('Parametric Curve: y = g(t), f = h(t)')
#plt.grid(True)
#plt.show()
#
sd.play(stereo_signal, samplerate=sampling_freq, blocking=True)
