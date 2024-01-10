cycle_duration = .005
duration = 10
sampling_freq = 44100  

elif(self.arg1=="square"):
            signalY = np.sign(np.sin(2 * np.pi * 500 * t))
            signalX = np.sign(np.sin(2 * np.pi * 500 * t + np.pi/2))