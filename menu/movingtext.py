# @author: Nicolas Drufin <nicolas.drufin@ensc.fr>
import pygame
from pygame.locals import *

class MovingText:
    def __init__(self, surface, text, size=80, freq=15):
        self._surface = surface
        self._text = text
        self._freq = freq
        self._hmin = 0
        self._hmax= 50
        self._color = 255, 255, 255
        self._font = pygame.font.Font(None, size)
        self._hpositions = [i*10 for i in range(len(self._text))]
        self._hways = [1 for i in range(len(self._text))]
        self._ticks = 0

    def on_loop(self):
        ticks = pygame.time.get_ticks()
        if not self._ticks:
            move = 1
        else:
            move = int((ticks - self._ticks)/self._freq)

        for m in range(move):
            for i in range(len(self._text)):
                self._hpositions[i] += self._hways[i]
                if self._hpositions[i] in [self._hmin, self._hmax]:
                    self._hways[i] *= -1

        self._ticks = self._ticks + move * self._freq

    def on_render(self):
        width = 0
        for i in range(len(self._text)):
            renderer = self._font.render(self._text[i], 0, self._color)
            self._surface.blit(renderer, (width, self._hpositions[i]))
            width += renderer.get_width()
