class Entity:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Food(Entity):

    def __init__(self, x, y, w, h, colour):
        super().__init__(x, y, w, h)
        self.colour = colour