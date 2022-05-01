import pygame
from pygame.locals import *


class Window:
    @staticmethod
    def create_window(width: int, height: int, title: str) -> None:
        pygame.init()
        display = (width, height)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        pygame.display.set_caption(title)


    @staticmethod
    def render() -> None:
        pygame.display.flip()

    @staticmethod
    def dispose() -> None:
        pygame.display.quit()

    @staticmethod
    def is_closed() -> bool:
        for _ in pygame.event.get(pygame.QUIT):
            return True

    @property
    def width(self) -> int:
        return pygame.display.get_window_size()[0]

    @property
    def height(self) -> int:
        return pygame.display.get_window_size()[1]

    @property
    def title(self) -> (str, str):
        return pygame.display.get_caption()
