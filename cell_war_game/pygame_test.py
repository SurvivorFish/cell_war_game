import math
import time

import pygame
import gif_pygame
from screeninfo import get_monitors
import random

WIDTH = 800
HEIGHT = 600
use_small_resolution = True
if not use_small_resolution:
    for m in get_monitors():  # finding resolution of primary monitor
        if m.is_primary:
            WIDTH = m.width
            HEIGHT = m.height
fps = 60

pygame.init()
pygame.mixer.init()  # for music
Playlist = ['resources/Minecraft Volume Alpha - 3 - Subwoofer Lullaby.ogg',
            'resources/Minecraft Volume Alpha - 18 - Sweden.ogg',
            'resources/Minecraft Volume Alpha - 20 - Dog.ogg',
            'resources/Minecraft Volume Alpha - 21 - Danny.ogg']

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cell war game")
pygame.display.set_icon(pygame.image.load('resources/moai_icon.png'))
clock = pygame.time.Clock()

# pygame.mixer.music.load('resources/Highfleet radio_missile_02.wav')  # fast test of music queue
pygame.mixer.music.load(Playlist[len(Playlist)-1])
pygame.mixer.music.play()

gif = gif_pygame.load("resources/dogs.gif")


running = True
screen.fill((21, 52, 0))
while running:
    clock.tick(fps)

    screen.fill((0, 0, 0))
    screen.fill((127+int(127*math.sin(time.time()/1)),
                 127+int(127*math.sin(time.time()/1+math.pi/3)),
                 127+int(127*math.sin(time.time()/1+math.pi*2/3))))
    gif.render(screen, (screen.width/2-gif.get_width()/2, screen.height/2-gif.get_height()/2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('resources/ГООООЛ!.ogg')
            pygame.mixer.music.play()
            clock.tick(0.2)
            running = False
        if pygame.mixer.music.get_busy():
            if len(Playlist) > 0:
                for music in Playlist[::-1]:
                    pygame.mixer.music.queue(music)

    pygame.display.update()

pygame.quit()
