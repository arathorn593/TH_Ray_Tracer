def raytrace_main(incident_ori, incident_dir, distance_travelled, obj_list, light_list):
        color = 0
        ray = (incident_ori, incident_dir)
        (distance, obj) = find_intersection(incident_ori, incident_dir, obj_list)
        if distance:
            for i in xrange(len(light_list)):
                # calculate lighting contribution
                pass
            
