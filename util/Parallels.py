import math


class Parallels:
    def __init__(self):
        return

    @staticmethod
    def getDistance2(lines: list):
        """计算两条平行线距离"""
        lineArray = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            lineArray.append([x1, y1, x2, y2])
        targetPixelLength = math.fabs((lineArray[0][1] + lineArray[0][3]) / 2 - (lineArray[1][1] + lineArray[1][3]) / 2)
        return targetPixelLength

    @staticmethod
    def getDistance(lines: list, vertical=False):
        """计算两条水平线或铅垂线距离,有两条粗线,拟合出了N条线,自适应N"""
        lineArray = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            lineArray.append([x1, y1, x2, y2])
        _lengths = []
        if vertical:
            for l1 in lineArray:
                for l2 in lineArray[1:]:
                    _lengths.append(math.fabs((l1[0] + l1[2]) / 2 - (l2[0] + l2[2]) / 2))
        else:
            for l1 in lineArray:
                for l2 in lineArray[1:]:
                    _lengths.append(math.fabs((l1[1] + l1[3]) / 2 - (l2[1] + l2[3]) / 2))
        # 降序排序
        _lengths.sort(reverse=True)
        if len(_lengths) < 2:
            return 0
        # 计算平均值减小误差，同时舍弃小距离
        eps = _lengths[0] / 2
        _nums: int = 0
        _sum = 0
        for i in range(len(_lengths) - 1):
            if _lengths[i] < eps:
                break
            _nums += 1
            _sum += _lengths[i]
        targetPixelDistance = _sum / _nums
        return targetPixelDistance
