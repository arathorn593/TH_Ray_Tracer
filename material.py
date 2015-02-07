

class material(object):
    #color is a list of three ints [R, G, B]
    def __init__(self, color, refr_index, refl_index):
        self.color = color
        
        if(refr_index + refl_index > 1):
            print "reflection and refraction sum to greater than one!!!"

        self.refr = refr_index
        self.refl = refl_index

    def get_color():
        return self.color
