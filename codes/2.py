import os
import random
import playsound
    
# Set the directory path where your audio files are located
audio_directory = 'playlist'

# Get a list of all audio files in the directory
audio_files = [file for file in os.listdir(audio_directory) if file.endswith('.mp3')]

# Shuffle the audio files randomly
random.shuffle(audio_files)
   
# Play each audio file one after the other
for audio_file in audio_files:
    audio_path = os.path.join(audio_directory, audio_file)
    playsound.playsound(audio_path)


