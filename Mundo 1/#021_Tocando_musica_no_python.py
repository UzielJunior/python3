
# chamando biblioteca de games (pygame) se n possuir é possivel baixar dentro do Python
import pygame
pygame.init()
pygame.mixer.music.load('../blues.mp3')
pygame.mixer.music.play()
pygame.event.wait()

