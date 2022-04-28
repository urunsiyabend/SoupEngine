import pygame


class Window:
    @staticmethod
    def create_window(width: int, height: int, title: str) -> None:
        pygame.init()
        pygame.display.set_mode([width, height])
        pygame.display.set_caption(title)

    @staticmethod
    def render() -> None:
        pygame.display.update()

    @staticmethod
    def dispose() -> None:
        pygame.display.quit()

    @staticmethod
    def is_closed() -> bool:
        for event in pygame.event.get(pygame.QUIT):
            return True

    @staticmethod
    def get_width() -> int:
        return pygame.display.get_window_size()[0]

    @staticmethod
    def get_height() -> int:
        return pygame.display.get_window_size()[1]

    @staticmethod
    def get_title() -> (str, str):
        return pygame.display.get_caption()
