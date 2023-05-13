import math
import functools
from functools import total_ordering


@total_ordering
class color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.distance = 0
        self.closest_color = None

    def set_distance(self, d):
        self.distance = d

    def calculate_distance(self, color):
        self.distance = math.sqrt((color.r - self.r) ** 2 + (color.g - self.g) ** 2 + (color.b - self.b) ** 2)


    def __lt__(self, obj):
        return self.distance < obj.distance

    def __gt__(self, obj):
        return self.distance > obj.distance

    def __le__(self, obj):
        return self.distance <= obj.distance

    def __ge__(self, obj):
        return self.distance >= obj.distance

    def __eq__(self, obj):
        return self.distance == obj.distance

    def __repr__(self):
        return str((self.r, self.g, self.b))
