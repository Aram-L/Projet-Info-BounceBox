import pygame
import sys
import math

class Boules:
    def __init__(self, x, y, rayon, couleur):
        self.vitesse = 0
        self.x = x
        self.y = y
        self.r = rayon
        self.c = couleur

class Blanche(Boule):


class Coloree(Boule):
