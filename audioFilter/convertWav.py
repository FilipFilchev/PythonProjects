from pydub import AudioSegment

# Load mp3 file
audio = AudioSegment.from_mp3("./song.mp3")

# Export as wav
audio.export("./output.wav", format="wav")
