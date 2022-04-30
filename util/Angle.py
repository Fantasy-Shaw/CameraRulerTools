import math


class Angle:
    def __init__(self):
        return

    @staticmethod
    def getAngle(vec1: list, vec2: list):
        _angle_cos = (vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (
                math.sqrt(vec1[0] * vec1[0] + vec1[1] * vec1[1]) * math.sqrt(
            vec2[0] * vec2[0] + vec2[1] * vec2[1]))
        _angle = math.acos(_angle_cos)
        if _angle > math.pi / 2:
            _angle = math.pi - _angle
        return _angle

    @staticmethod
    def getAnglewithGround(vec: list):
        return Angle.getAngle(vec, [1, 0])
