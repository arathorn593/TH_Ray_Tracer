import numpy as np
print "Imported reflect.py"
def find_intersection(incident_ori, incident_dir, obj_list):
    minDist = None
    minDistIndex = 0

    for i in xrange(len(obj_list)):
        dist = obj_list[i].does_intersect(incident_ori, incident_dir)

        if(dist != None and (minDist == None or dist < minDist)):
            minDist = dist
            minDistIndex = i

    return (minDist, obj_list[minDistIndex])


