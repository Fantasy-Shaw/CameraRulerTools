import cv2 as cv
import numpy as np
import math
from util.Angle import Angle


class ExamPic4Angle:
    def __init__(self, rawPicPath: str, processedPicPath: str):
        rawPicData = np.fromfile(rawPicPath, dtype=np.uint8)
        self.rawPic = cv.imdecode(rawPicData, cv.IMREAD_COLOR)
        processedPicData = np.fromfile(processedPicPath, dtype=np.uint8)
        self.processedPic = cv.imdecode(processedPicData, cv.IMREAD_COLOR)
        self.lines = []
        self.angle: float = 0.0
        self.angle1: float = 0.0
        self.angle2: float = 0.0

    def getAngle(self):
        drawing = np.zeros(self.processedPic.shape[:], dtype=np.uint8)
        gray = cv.cvtColor(self.processedPic, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 50, 150)
        # 概率统计霍夫变换
        self.lines = cv.HoughLinesP(edges, 0.8, np.pi / 180, 90, minLineLength=50, maxLineGap=150)
        for line in self.lines:
            x1, y1, x2, y2 = line[0]
            cv.line(self.rawPic, (x1, y1), (x2, y2), (0, 0, 255), 3)
        self.calcAngle()
        cv.imshow("Lines", self.rawPic)
        cv.waitKey()

    def calcAngle(self, printAns=True):
        Angles: list = []
        # 不一定检测到两条线，记录最后一条线，lines:list首尾两条线一定是两个杆的向量
        lineofvec2 = None
        # 把检测到的直线两两计算夹角，计算出的接近0度的角度舍弃掉
        for line1 in self.lines:
            lineofvec2 = line1
            for line2 in self.lines[1:]:
                x1, y1, x2, y2 = line1[0]
                x3, y3, x4, y4 = line2[0]
                vec1 = [x2 - x1, y2 - y1]
                vec2 = [x4 - x3, y4 - y3]
                _angle = Angle.getAngle(vec1, vec2)
                Angles.append(_angle)
        for ag in Angles:
            if ag > self.angle:
                self.angle = ag
        # 计算与地面的夹角
        x1, y1, x2, y2 = self.lines[0][0]
        x3, y3, x4, y4 = lineofvec2[0]
        vec1 = [x2 - x1, y2 - y1]
        vec2 = [x4 - x3, y4 - y3]
        self.angle1 = Angle.getAnglewithGround(vec1)
        self.angle2 = Angle.getAnglewithGround(vec2)
        # 输出结果
        if printAns:
            print("rad = " + str(self.angle), "\ndegrees = " + str(math.degrees(self.angle)))
            print("The left with ground:\n" + "rad = " + str(self.angle1),
                  "\ndegrees = " + str(math.degrees(self.angle1)))
            print("The right with ground:\n" + "rad = " + str(self.angle2),
                  "\ndegrees = " + str(math.degrees(self.angle2)))
