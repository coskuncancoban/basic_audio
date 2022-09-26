import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("audio_processing_basics/poznan.wav", "rb") # opens and reads binary.

sample_freq = obj.getframerate() # freq is for frequency.
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1) # this is in binary format.

obj.close()

t_audio = n_samples / sample_freq # this will gives us the duration.

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int32) # this is a numpy array with signal wave. !!! np.int16 wasn't enough as dtype, it gave error as "... must have same first dimension, but..."

times = np.linspace(0, t_audio, num=n_samples) # this is object for the "x" axis, from 0 to lenght of the signal.

# creating audio signal graphic with matplotlib.
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()













