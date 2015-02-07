# functions for writing ppm images

import numpy as np
from subprocess import call

def printHeader(imageFile, width, height, intensity=255):
    imageFile.write("P3\n")
    imageFile.write("%s %s\n" % (width, height))
    imageFile.write("%s\n" % (intensity))

def writePPM(array, path="image.ppm"):
    width = array.shape[0]
    height = array.shape[1]

    print width, height

    with open(path, "w") as f:
        printHeader(f, width, height)
        for row in xrange(height):
            for col in xrange(width):
                red = array[row][col][0]
                green = array[row][col][1]
                blue = array[row][col][2]
                f.write("%i %i %i\n" % (red, green, blue))

    #call ('convert %s %s; rm %s' %(path, path[:-4] + '.png', path), shell=False)
