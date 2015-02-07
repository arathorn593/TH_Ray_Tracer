import random

width = 1000
height = 500

def printHeader(imageFile, width, height, intensity=255):
    imageFile.write("P3\n")
    imageFile.write("%s %s \n" % (str(width), str(height)))
    imageFile.write("%s\n" % (str(intensity)))


path = "image.ppm"
f = open(path, "w")

printHeader(f, width, height)

for row in xrange(width):
    for col in xrange(height):
        green = random.randint(0, 255);
        other = random.randint(0, green);
        f.write("%s %s %s \n" % (str(other), str(green), str(other)))

f.close();
