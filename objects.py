import numpy as np
from numpy import linalg as la
import math

class PrimativeObject (object):
    def __init__ (self, origin, material):
        self.center = np.array(origin)
        self.material = material

    def does_intersect (incident_dir, incident_ori): pass
    def get_surface_normal (incident_dir, incident_ori, distance): pass
    def get_color (point): pass

class InfinitePlane (PrimativeObject):
    def __init__ (self, origin, surface_normal, material):
        super (InfinitePlane, self).__init__ (origin, material)
        self.surface_normal = np.array(surface_normal)

    def does_intersect (incident_dir, incident_ori):
        incident_dot_normal = np.inner (incident_dir, self.surface_normal)

        if (abs (incident_dot_normal) > 0.):
            return (self.center - incident_ori) * self.surface_normal / incident_dot_normal
        else:
            return None

    def get_surface_normal (point):
        return self.surface_normal

class Triangle (PrimativeObject):
    def __init__ (self, pointA, pointB, pointC):
        super (Triangle, self).__init__ (a, material)

        self.a = np.array(pointA)
        self.b = np.array(pointB)
        self.c = np.array(pointC)

        self.surface_normal = np.cross (pointB - pointA, pointC - pointA)
        self.surface_normal /= la.norm (self.surface_normal, ord=0)

    def get_surface_normal (incident_dir, incident_ori, distance):
        if (np.inner (self.b - self.a, incident_dir * distance + incident_ori) > EPSILON): return self.surface_normal
        else: return -self.surface_normal

    def does_intersect (incident_dir, incident_ori):
        p = np.cross (incident_dir, c - a)
        determinant = np.inner (b - a, p)

        if (abs (determinant) < EPSILON): return None

        t = incident_ori - a
        u = np.inner (t, p) / determinant

        if (abs (u) > 1.): return None

        q = np.cross (t, b - a)
        v = (incident_dir * q) / determinant

        if (abs (v) < 0. or u + v > 1.): return None

        return (c - a) * q / determinant

class Cylinder (PrimativeObject):
    def __init__ (self, center, axis, radius, length, material):
        super (Cylinder, self).__init__ (center, material)

        self.axis = np.array(axis)
        self.axis /= la.norm (self.axis, ori=0)

        self.radius = radius
        self.length = length

    def get_surface_normal (incident_dir, incident_ori, distance):
        intersection_point = incident_dir * distance + incident_ori

        if (abs (np.inner (intersection_point - self.center, self.axis)) < EPSILON): return -self.axis
        elif (abs (np.inner (intersection_point - (self.center + self.axis * self.distance), self.axis)) < EPSILON): return self.axis
        else:
            cyl_norm = self.axis * np.inner (self.center - intersection_point, self.axis) - (self.center - intersection_point)
            return cyl_norm / la.norm (cyl_norm, ord=0)

    def doesIntersect (incidentDir, incidentOri):
        delta_p = incidentOrigin - self.center
        delta_p_dot_axis = np.inner (delta_p, self.axis)

        a = np.sum (la.matrix_power (incident_dir - incident_dot_axis * self.axis, 2))
        b = 2. * np_inner (incident_dir - incident_dot_axis * self.axis, delta_p - delta_p_dot_axis * self.axis)
        c = np.sum (la.matrix_power (delta_p - delta_p_dot_axis * self.axis, 2))

        descriminant = math.pow (b, 2) - 4. * a * c

        if (descriminant > 0.):
            solution = -b + math.sqrt (descriminant) / (2. * a) if (b > 0.) else -b - math.sqrt (descriminant) / (2. * a)

            if (solution > 0.):
                intersection_point = incident_ori + solution * incident_dir - (self.center + self.length * self.axis)

                if (np.inner (self.axis, intersection_point) < 0.):
                    intersection_point = incident_ori + solution * incident_dir - self.center

                    if (np.inner (self.axis, intersection_point) > 0.): shortest_distance = solution

        if (abs (incident_dot_axis) > EPSILON):
            solution = delta_p_dot_axis / incident_dot_axis

            if (solution > 0. and solution < shortest_distance and np.sum (la.matrix_power (incident_ori + solution * incident_dir - self.center)) < math.pow (self.radius, 2)): shortest_distance = solution

            delta_p = incident_ori - (self.center + length * self.axis)
            solution = np.inner (delta_p * self.axis) / incident_dot_axis

            if (solution > 0. and solution < shortest_distance and np.sum (la.matrix_power (incident_ori + solution * incident_dir - self.center)) < math.pow (self.radius, 2)): shortest_distance = solution

class Sphere (PrimativeObject):
    def __init__ (self, center, radius, material):
        super (Sphere, self).__init__ (center, material)
        self.radius = radius

    def get_surface_normal (incident_ori, incident_dir, distance):
        surface_normal = incident_ori + distance * incident_dir - self.center

        return surface_normal / la.norm (surface_normal, ord=0)

    def doesIntersect (incident_ori, incident_dir):
        solution = None
        delta_p = incident_ori - self.center

        a = np.inner (incident_dir, incident_dir)
        b = 2. * np.inner (incident_dir, delta_p)
        c = np.inner (delta_p, delta_p) - math.pow (self.radius, 2)
        descriminant = math.pow (b, 2) - 4. * a * c

        if (descriminant > 0.):
            solution = -b + math.sqrt (descriminant) / (2. * a) if (b > 0.) else -b - math.sqrt (descriminant) / (2. * a)

        return solution
