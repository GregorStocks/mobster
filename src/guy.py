from weapon import Weapon
from sprites import load_png

class Guy:
    def __init__(self, filename, x, y):
        self.x = x
        self.y = y
        self.weapon = Weapon(5)
        self.image, _ = load_png(filename)

