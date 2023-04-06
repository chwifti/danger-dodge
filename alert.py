import pyttsx3
import pygame
import time

file_path = "dangers.txt"

engine = pyttsx3.init()

# Set voice to French (assuming it's available on your system)
engine.setProperty('voice', 'fr')

# Initialize pygame mixer and load siren sound file
pygame.mixer.init()
siren_sound = pygame.mixer.Sound("siren.mp3")

while True:
    with open("dangers.txt", "r") as file:
        for line in file:
            if "person" in line:
                # Play siren sound before message
                siren_sound.play()
                time.sleep(5)  # Wait for 5 seconds
                siren_sound.stop()  # Stop siren sound
                # Speak message in French
                message = "Il y a un risque élevé de blessure dans cette zone. Pour votre sécurité, veuillez vous éloigner."
                engine.say(message)
                engine.runAndWait()
