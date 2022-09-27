import pyaudio
import wave

#setting up some parameters.
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt32
CHANNELS = 1
RATE = 16000 # you can use different rates and play arround whit this.

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print ("start recording")

seconds = 5 # this is the second number of we want to record.
frames = [] # a list object that where we store the frames.

for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)): # this will record for 5 seconds.
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

# closing everything.
stream.stop_stream()
stream.close()
p.terminate()

# saving the frames object in a wave file.
obj = wave.open("output.wav", "wb") # wb means write binary.
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)

# we need to write this in binary. b"" creates a binary string.
obj.writeframes(b"".join(frames)) # this will combine all the elements in our "frames" list into a binary string.
obj.close()
