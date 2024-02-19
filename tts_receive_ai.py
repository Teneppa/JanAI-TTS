import subprocess

from flask import Flask, request

app = Flask(__name__)

import torch
from TTS.api import TTS
import pygame

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait until the music is finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    pygame.quit()

# Specify the path to the audio file you want to play
audio_file_path = "output.wav"

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

print(device)

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/en/ljspeech/glow-tts").to(device)

@app.route('/')
def handle_request():
    # Get the value of the 'message' parameter from the query string
    message = request.args.get('message', default='', type=str)
    
    # Process the message or perform any other actions
    # For now, let's just return the message as a response
    print(message)
    message = message.replace('"', '')
    #subprocess.Popen(f'tts --text "{message}" --pipe_out | aplay', shell=True)

    tts.tts_to_file(text=message, file_path=audio_file_path, speed=1.8)
    play_audio(audio_file_path)

    return f"Received message: {message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
