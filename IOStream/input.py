import pygame
from Math.vector import Vector2f


class Input:
    @staticmethod
    def get_key(keyCode: int) -> bool:
        return pygame.key.get_pressed()[keyCode]

    @staticmethod
    def get_key_down(keyCode: int) -> bool:
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == keyCode:
                return True

    @staticmethod
    def get_key_up(keyCode: int) -> bool:
        for event in pygame.event.get(pygame.KEYUP):
            if event.key == keyCode:
                return True

    @staticmethod
    def get_mouse(keyCode: int) -> bool:
        return pygame.mouse.get_pressed()[keyCode]

    @staticmethod
    def get_mouse_down(keyCode: int) -> bool:
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.key == keyCode:
                return True

    @staticmethod
    def get_mouse_up(keyCode: int) -> bool:
        for event in pygame.event.get(pygame.MOUSEBUTTONUP):
            if event.key == keyCode:
                return True

    @staticmethod
    def get_mouse_position():
        return Vector2f(*pygame.mouse.get_pos())
