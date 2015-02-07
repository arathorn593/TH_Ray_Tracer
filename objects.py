import numpy as np
from numpy import linalg as la
import math

class PrimativeObject:
    def __init__ (self, origin, material):
        self.center = origin.view()
        self.material = material

    def does_intersect (incident_dir, incident_ori): pass
    def get_surface_normal (t): pass
    def get_color (point): pass

class InfinitePlane (PrimativeObject):
    def __init__ (self, origin, surface_normal, material):
        super (InfinitePlane, self).__init__ (origin, material)
        self.surface_normal = surface_normal.view()

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

        self.a = pointA.view()
        self.b = pointB.view()
        self.c = pointC.view()

        self.surface_normal = np.cross (pointB - pointA, pointC - pointA)
        self.surface_normal /= la.norm (self.surface_normal, ord=0)

    def get_surface_normal (incident_dir, incident_ori, distance):
        if (np.inner (self.b - self.a, incident_dir * distance + incident_ori) > EPSILON): return self.surface_normal
        else: return -1. * self.surface_normal

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

        self.axis = axis.view()
        self.axis /= la.norm (self.axis, ori=0)

        self.radius = radius
        self.length = length

    def get_surface_normal (incident_dir, incident_ori, distance):
        intersection_point = incident_dir * distance + incident_ori

        if (abs (intersection_point - self.center), self.axis) < EPSILON): return -1. * self.axis
        elif (abs (np.inner (intersection_point - (self.center + self.axis * self.distance), self.axis)) < EPSILON: return self.axis
        else:
            cyl_norm = self.axis * np.inner (self.center - intersection_point, self.axis) - (self.center - intersection_point)
            return cyl_norm / la.norm (cyl_norm, ori=0)

    def doesIntersect (incidentDir, incidentOri):
        delta_p = incidentOrigin - self.center
        delta_p_dot_axis = np.inner (delta_p, self.axis)

        a = np.sum (la.matrix_power (incident_dir - incident_dot_axis * self.axis, 2))
        b = 2. * np_inner (incident_dir - incident_dot_axis * self.axis, delta_p - delta_p_dot_axis * self.axis)
        c = np.sum (la.matrix_power (delta_p - delta_p_dot_axis * self.axis, 2))

        descriminant = math.pow (b, 2) - 4. * a * c

        if (descriminant > 0.):
            solution = (b > 0.) ? -b + math.sqrt (descriminant) / (2. * a) : -b - math.sqrt (descriminant) / (2. * a)

            if (solution > 0.):
                intersection_point = incident_ori + solution * incident_dir
