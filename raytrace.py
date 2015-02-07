raytrace_main(incident_ori, incident_dir, distance_travelled, obj_list):
    gridWidth = 0
    gridHeight = 0

    for x in xrange(gridWidth):
        for y in xrange(gridHeight):
            color = 0
            ray = (incident_ori, incident_dir)
            distance = find_intersection(incident_ori, incident_dir)
            if distance:
                pass
