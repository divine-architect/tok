import pygame
from pynput import keyboard

pygame.init()
def on_press(key):
    try:

        sound = pygame.mixer.Sound("22.mp3")
        sound.play()
       
    except AttributeError:
        print('e')

def on_release(key):

    if key == keyboard.Key.num_lock:
        
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()