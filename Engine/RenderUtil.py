from OpenGL.GL import *


class RenderUtil:
    @staticmethod
    def clear_screen() -> None:
        # TODO: Stencil buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    @staticmethod
    def init_graphics() -> None:
        glClearColor(0, 1, 0, 1)

        glFrontFace(GL_CW)
        glCullFace(GL_BACK)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)

        # TODO: Depth clamp

        glEnable(GL_FRAMEBUFFER_SRGB)