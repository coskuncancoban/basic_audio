# Audio file formats
# .mp3 (most popular. it is a lossy compression format. this means it compresses the data. and during this procces we can lose information.)
# .flac (it is a loss less compression format but it also compresses the data but it allows us to perfectly reconstruct the original data.)
# .wav (it is an uncompressed format. it stores data in an uncompressed way. audio quality is the best but also the file size is the largest. it is the standart for CD audio quality.)

import wave

# Audio signal parameters
# - number of channels (this is the number of independent audio channels. usually 1 or 2. 1 is mono, 2 is stereo.)
# - sample width (this is the number of bytes for each sample.)
# - framerate/sample_rate (this means the number of samples for each sacond. for example 44,100 Hz (44,100 hertz or 44.1 kilohertz is standart sampling rate for CD quality.))
# - number of frames (this is the total number of frames we get.)
# - values of a frame (values of each frame. when we load this, it will be in a binary format but we can convert it to integer values later.)

obj = wave.open("audio_processing_basics/poznan.wav", "rb") # "rb" means read binary.

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1) # you can give to function "the number of frames" or with "-1" it will read all frames.
print(type(frames), type(frames[0]))
print(len(frames))

obj.close()

obj_new = wave.open("audio_processing_basics/poznan_new.wav", "wb") # "wb" means write binary.

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)

obj_new.writeframes(frames)

obj_new.close()
print("done")