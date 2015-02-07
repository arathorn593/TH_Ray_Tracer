# functions for writing ppm images

import numpy as np

def printHeader(imageFile, width, height, intensity=255):
    imageFile.write("P3\n")
    imageFile.write("%s %s\n" % (width, height))
    imageFile.write("%s\n" % (intensity))

def writePPM(array, path="image.ppm"):
    width = array.shape[0]
    height = array.shape[1]
    with open(path, "w") as f:
        printHeader(f, width, height)
        for row in xrange(width):
            for col in xrange(height):
                red = array[row][width][0]
                green = array[row][width][2]
                blue = array[row][width][3]
                f.write("%i %i %i\n" % (red, green, blue))
