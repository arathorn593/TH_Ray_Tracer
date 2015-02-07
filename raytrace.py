from imports import *

def add_color(color_main, color_to_add, scale):
    for i in xrange(len(color_main):
        color_main[i] += color_to_add * scale

def raytrace_main(incident_ori, incident_dir, dist, obj_list, pixel):
    #maximum distance a ray can travel
    maxDist = 100
    if(dist > maxDist):
        return None

    #calculate the new distance
    (distance, obj) = find_intersection(incident_ori, incident_dir, obj_list)


    if distance:
        dist += distance
        dist_scale = 1.0/(dist)
        
        #add matte color
        add_color(pixel, obj.color, obj.material.matte_scale)

        #add reflected color if necessary
        if obj.is_reflective:
            norm_vect = obj.get_surface_norm(incident_ori, incident_dir, distance)
            refl_vect = incident_ori - (norm_vect * 2 * (np.dot(incident_ori, norm_vect)))
            intersect_point = incident_ori + distance * incident_dir
            refl_color = raytrace_main(intersect_point, refl_vect, dist, obj_list, light_list)
            if(refl_color != None):
                add_color(pixel, refl_color, obj.material.refl_scale)

        if obj.is_refractive:
            pass
