# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:13:20 2019

@author: 18367
"""
import numpy as np
 
import wave
 
import struct
 
import matplotlib.pyplot as plt

# frequency is the number of times a wave repeats a second
 
frequency = 2000
 
noisy_freq = 200
 
num_samples = 48000
 
# The sampling rate of the analog to digital convert
 
sampling_rate = 48000.0

#Create the sine wave and noise
 
sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]
 
sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/  sampling_rate) for x1 in range(num_samples)]
 
#Convert them to numpy arrays
 
sine_wave = np.array(sine_wave)
 
sine_noise = np.array(sine_noise)

# Add them to create a noisy signal
 
combined_signal = sine_wave + sine_noise

plt.subplot(3,1,1)
 
plt.title("Original sine wave")
 
# Need to add empty space, else everything looks scrunched up!
 
plt.subplots_adjust(hspace=.5)
 
plt.plot(sine_wave[:500])
 
plt.subplot(3,1,2)
 
plt.title("Noisy wave")
 
plt.plot(sine_noise[:4000])
 
plt.subplot(3,1,3)
 
plt.title("Original + Noise")
 
plt.plot(combined_signal[:3000])
 
plt.show()

data_fft = np.fft.fft(combined_signal)
 
freq = (np.abs(data_fft[:len(data_fft)]))

filtered_freq = []
 
index = 0
 
filtered_freq = [f if (1950 < index < 2050 and f > 1) else 0 for index, f in enumerate(freq)]

recovered_signal = np.fft.ifft(filtered_freq)

plt.subplot(3,1,1)
 
plt.title("Original sine wave")
 
# Need to add empty space, else everything looks scrunched up!
 
plt.subplots_adjust(hspace=.5)
 
plt.plot(sine_wave[:500])
 
plt.subplot(3,1,2)
 
plt.title("Noisy wave")
 
plt.plot(combined_signal[:4000])
 
plt.subplot(3,1,3)
 
plt.title("Sine wave after clean up")
 
plt.plot((recovered_signal[:500]))
 
plt.show()

