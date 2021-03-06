from window import Window
from TimeUtil.time import Time
from Engine.RenderUtil import RenderUtil
from game import Game
from OpenGL.GL import glClearColor

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Soup Engine"
FRAME_C = 5000


class Main:
    def __init__(self):
        self.isRunning = False
        self.game = Game()

    def start(self) -> None:
        if self.isRunning:
            return
        self.run()

    def stop(self) -> None:
        if not self.isRunning:
            return

        self.isRunning = False

    def run(self) -> None:
        self.isRunning = True

        frames = 0
        frameCounter = 0

        FRAME_TIME: float = 1 / FRAME_C

        lastTime = Time.get_time()
        unprocessedTime = 0

        while self.isRunning:
            render = False

            startTime = Time.get_time()
            elapsedTime = startTime - lastTime
            lastTime = startTime

            unprocessedTime += (elapsedTime / Time.SECOND)
            frameCounter += elapsedTime

            while unprocessedTime > FRAME_TIME:
                render = True
                unprocessedTime -= FRAME_TIME

                if Window.is_closed():
                    self.stop()

                Time.set_delta(FRAME_TIME)

                self.game.input()
                self.game.update()

                if frameCounter >= Time.SECOND:
                    print(frames)
                    frames = 0
                    frameCounter = 0

            if render:
                self.__render()
                frames += 1
            else:
                Time.sleep_thread(1 / 1000)

        self.__clean()

    def __render(self) -> None:
        RenderUtil.clear_screen()
        self.game.render()
        Window.render()

    def __clean(self) -> None:
        Window.dispose()

    @staticmethod
    def main() -> None:
        Window.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        RenderUtil.init_graphics()
        Main().start()


if __name__ == '__main__':
    Main.main()
