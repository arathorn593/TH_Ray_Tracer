import numpy as np
from imports import *

def get_object_list():
    object_list = [Sphere ([5., 0., 5.], 1., Matte ([255, 0, 0])), Sphere([0., 5., 5.], 0.5, Matte([0, 255, 0]))]

    return object_list

def raytrace_init ():
    camera_coors = np.array([0, 0, 0,])
    screenZ = 1.

    image_dims = (500, 500)
    image = np.ndarray((*image_dims, 3), np.uint8)

    object_list = get_object_list()

    for row in xrange (image_dims[0]):
        for col in xrange (image_dims[1]):
            camera_ray_dir = np.array ([col / image_dims[0] - camera_coors[0], row / image_dims[1] - camera_cols[1], screenZ - camera_coors[2]])

            raytrace_main (camera_coors, camera_ray_dir, 0., object_list, image[row][col])

    writePPM (image)

if (__name__ == '__main__'): raytrace_init()
