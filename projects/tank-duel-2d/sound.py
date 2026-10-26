"""Âm thanh tổng hợp khi chạy, không cần tải tệp wav."""
import array
import math
import pygame

SOUNDS = {}


def init():
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=22050, size=-16, channels=1)
        for name, frequency, duration in (("shot", 270, .09), ("hit", 120, .16),
                                          ("boom", 85, .25), ("item", 680, .12)):
            count = int(22050 * duration)
            samples = array.array("h", (int(4500 * (1 - i/count) *
                              math.sin(2*math.pi*frequency*i/22050)) for i in range(count)))
            SOUNDS[name] = pygame.mixer.Sound(buffer=samples.tobytes())
    except pygame.error:
        pass  # Máy không có thiết bị âm thanh vẫn chơi được.


def play(name):
    if name in SOUNDS:
        SOUNDS[name].play()
