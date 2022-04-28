import pygame
from Math.vector import Vector2


class Input:
    K_0 = 48
    K_1 = 49
    K_2 = 50
    K_3 = 51
    K_4 = 52
    K_5 = 53
    K_6 = 54
    K_7 = 55
    K_8 = 56
    K_9 = 57
    K_a = 97

    K_AC_BACK = 1073742094

    K_AMPERSAND = 38
    K_ASTERISK = 42
    K_AT = 64
    K_b = 98
    K_BACKQUOTE = 96
    K_BACKSLASH = 92
    K_BACKSPACE = 8
    K_BREAK = 1073741896
    K_c = 99
    K_CAPSLOCK = 1073741881
    K_CARET = 94
    K_CLEAR = 1073741980
    K_COLON = 58
    K_COMMA = 44
    K_CURRENCYSUBUNIT = 1073742005
    K_CURRENCYUNIT = 1073742004
    K_d = 100
    K_DELETE = 127
    K_DOLLAR = 36
    K_DOWN = 1073741905
    K_e = 101
    K_END = 1073741901
    K_EQUALS = 61
    K_ESCAPE = 27
    K_EURO = 1073742004
    K_EXCLAIM = 33
    K_f = 102
    K_F1 = 1073741882
    K_F10 = 1073741891
    K_F11 = 1073741892
    K_F12 = 1073741893
    K_F13 = 1073741928
    K_F14 = 1073741929
    K_F15 = 1073741930
    K_F2 = 1073741883
    K_F3 = 1073741884
    K_F4 = 1073741885
    K_F5 = 1073741886
    K_F6 = 1073741887
    K_F7 = 1073741888
    K_F8 = 1073741889
    K_F9 = 1073741890
    K_g = 103
    K_GREATER = 62
    K_h = 104
    K_HASH = 35
    K_HELP = 1073741941
    K_HOME = 1073741898
    K_i = 105
    K_INSERT = 1073741897
    K_j = 106
    K_k = 107
    K_KP0 = 1073741922
    K_KP1 = 1073741913
    K_KP2 = 1073741914
    K_KP3 = 1073741915
    K_KP4 = 1073741916
    K_KP5 = 1073741917
    K_KP6 = 1073741918
    K_KP7 = 1073741919
    K_KP8 = 1073741920
    K_KP9 = 1073741921

    K_KP_0 = 1073741922
    K_KP_1 = 1073741913
    K_KP_2 = 1073741914
    K_KP_3 = 1073741915
    K_KP_4 = 1073741916
    K_KP_5 = 1073741917
    K_KP_6 = 1073741918
    K_KP_7 = 1073741919
    K_KP_8 = 1073741920
    K_KP_9 = 1073741921
    K_KP_DIVIDE = 1073741908
    K_KP_ENTER = 1073741912
    K_KP_EQUALS = 1073741927
    K_KP_MINUS = 1073741910
    K_KP_MULTIPLY = 1073741909
    K_KP_PERIOD = 1073741923
    K_KP_PLUS = 1073741911

    K_l = 108
    K_LALT = 1073742050
    K_LCTRL = 1073742048
    K_LEFT = 1073741904
    K_LEFTBRACKET = 91
    K_LEFTPAREN = 40
    K_LESS = 60
    K_LGUI = 1073742051
    K_LMETA = 1073742051
    K_LSHIFT = 1073742049
    K_LSUPER = 1073742051
    K_m = 109
    K_MENU = 1073741942
    K_MINUS = 45
    K_MODE = 1073742081
    K_n = 110
    K_NUMLOCK = 1073741907
    K_NUMLOCKCLEAR = 1073741907
    K_o = 111
    K_p = 112
    K_PAGEDOWN = 1073741902
    K_PAGEUP = 1073741899
    K_PAUSE = 1073741896
    K_PERCENT = 37
    K_PERIOD = 46
    K_PLUS = 43
    K_POWER = 1073741926
    K_PRINT = 1073741894
    K_PRINTSCREEN = 1073741894
    K_q = 113
    K_QUESTION = 63
    K_QUOTE = 39
    K_QUOTEDBL = 34
    K_r = 114
    K_RALT = 1073742054
    K_RCTRL = 1073742052
    K_RETURN = 13
    K_RGUI = 1073742055
    K_RIGHT = 1073741903
    K_RIGHTBRACKET = 93
    K_RIGHTPAREN = 41
    K_RMETA = 1073742055
    K_RSHIFT = 1073742053
    K_RSUPER = 1073742055
    K_s = 115
    K_SCROLLLOCK = 1073741895
    K_SCROLLOCK = 1073741895
    K_SEMICOLON = 59
    K_SLASH = 47
    K_SPACE = 32
    K_SYSREQ = 1073741978
    K_t = 116
    K_TAB = 9
    K_u = 117
    K_UNDERSCORE = 95
    K_UNKNOWN = 0
    K_UP = 1073741906
    K_v = 118
    K_w = 119
    K_x = 120
    K_y = 121
    K_z = 122

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
        return Vector2(*pygame.mouse.get_pos())
