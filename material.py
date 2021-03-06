

class Material(object):
    #color is a list of three ints [R, G, B]
    def __init__(self, color):
        self.color = color
        self.matte_scale = 1.0

    def get_color(self):
        pass

class Matte (Material):
    def __init__ (self, color):
        self.is_reflective = False
        self.is_refractvie = False
        super (Matte, self).__init__ (color)

    def get_color (self):
        return self.color
