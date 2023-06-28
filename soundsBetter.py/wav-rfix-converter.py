from pydub import AudioSegment

# Load the MP3 file
mp3_file = AudioSegment.from_mp3('song.mp3')

# Save the wave file
mp3_file.export('output.wav', format='wav')


#RIFF TO RIFX

# import wavepi

# # Open te wave file in read-only mode
# with wave.open('song.wav', 'rb') as wav_file:
#     # Get the number of channels, sample width, and frame rate
#     num_channels = wav_file.getnchannels()
#     sample_width = wav_file.getsampwidth()
#     frame_rate = wav_file.getframerate()

#     # Read the entire wave file into a byte array
#     data = wav_file.readframes(wav_file.getnframes())

# # Create a new wave file in write-only mode using the RIFX format
# with wave.open('output.wav', 'wb') as wav_file:
#     # Set the number of channels, sample width, and frame rate
#     wav_file.setnchannels(num_channels)
#     wav_file.setsampwidth(sample_width)
#     wav_file.setframerate(frame_rate)

#     # Write the data to the wave file
#     wav_file.writeframes(data)

#CHECKS FILE TYPE

# import wave

# # Open the wave file in read-only mode
# with wave.open('song.wav', 'rb') as wav_file:
#     # Get the file format
#     file_format = wav_file.getcomptype()

# # Check the file format
# if file_format == 'NONE':
#     print('The wave file is in the RIFF format.')
# elif file_format == 'RIFX':
#     print('The wave file is in the RIFX format.')
# else:
#     print('The wave file is in an unknown format.')
