import cv2 as cv
import numpy as np
import math
from util.Parallels import Parallels


class ExamPic4Length:
    def __init__(self, rawPicPath: str, referencePicPath: str, targetPicPath: str, referenceLength: float):
        rawPicData = np.fromfile(rawPicPath, dtype=np.uint8)
        self.rawPic = cv.imdecode(rawPicData, cv.IMREAD_COLOR)
        referencePicData = np.fromfile(referencePicPath, dtype=np.uint8)
        self.referencePic = cv.imdecode(referencePicData, cv.IMREAD_COLOR)
        targetPicData = np.fromfile(targetPicPath, dtype=np.uint8)
        self.targetPic = cv.imdecode(targetPicData, cv.IMREAD_COLOR)
        self.referenceLines = []
        self.targetLines = []
        self.referenceLength: float = referenceLength
        self.targetLength: float = 0.0
        self.scale: float = 0.0  # 比例尺=像素/长度

    # 计算比例尺
    def getScale(self, printScale=True):
        drawing = np.zeros(self.referencePic.shape[:], dtype=np.uint8)
        gray = cv.cvtColor(self.referencePic, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 50, 150)
        # 概率统计霍夫变换
        self.referenceLines = cv.HoughLinesP(edges, 0.8, np.pi / 180, 90, minLineLength=50, maxLineGap=150)
        for line in self.referenceLines:
            x1, y1, x2, y2 = line[0]
            cv.line(self.rawPic, (x1, y1), (x2, y2), (0, 0, 255), 3)
        referencePixelLength = -1
        for line in self.referenceLines:
            x1, y1, x2, y2 = line[0]
            _len = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
            if referencePixelLength < _len:
                referencePixelLength = _len
        self.scale = referencePixelLength / self.referenceLength
        if printScale:
            print("PixelDistance / RealDistance =", self.scale)
            print("RealDistance / PixelDistance =", 1 / self.scale)

    def getLength(self, printDistance=True, printScale=True):
        self.getScale(printScale)
        drawing = np.zeros(self.targetPic.shape[:], dtype=np.uint8)
        gray = cv.cvtColor(self.targetPic, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 50, 150)
        # 概率统计霍夫变换
        self.targetLines = cv.HoughLinesP(edges, 0.8, np.pi / 180, 90, minLineLength=50, maxLineGap=150)
        for line in self.targetLines:
            x1, y1, x2, y2 = line[0]
            cv.line(self.rawPic, (x1, y1), (x2, y2), (0, 255, 0), 3)
        targetPixelLength = Parallels.getDistance(self.targetLines)
        self.targetLength = targetPixelLength / self.scale
        if printDistance:
            print("TargetLength = ", self.targetLength)
            cv.imshow("Lines", self.rawPic)
            cv.waitKey()
