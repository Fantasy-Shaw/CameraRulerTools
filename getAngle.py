from CalcAngle.src.ExamPic4Angle import ExamPic4Angle
import os

if __name__ == '__main__':
    rawPicPath = os.getcwd() + "/CalcAngle/resources/raw.jpg"
    processedPicPath = os.getcwd() + "/CalcAngle/resources/pseudo.png"
    ep1 = ExamPic4Angle(rawPicPath, processedPicPath)
    ep1.getAngle()
