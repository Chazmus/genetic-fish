"""
Utility methods
"""
import math


def vector_to_delta_speed(direction, speed):
    """ Turn speed and direction into dx and dy
    """
    dx = math.sin(direction) * speed
    dy = math.cos(direction) * speed
    return dx, dy

def rads_to_degrees(rads):
    return math.degrees(rads)
