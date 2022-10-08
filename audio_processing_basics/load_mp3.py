# To load mp3 files we need an additional third party library such as pydup (with ffmpeg).

from pydub import AudioSegment

audio = AudioSegment.from_wav("poznan.wav")

# increase the volume by 6dB.
audio = audio + 6

audio = audio * 2

audio = audio.fade_in(2000) # 2000 miliseconds equals 2 seconds.

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")