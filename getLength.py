from CalcLength.src.ExamPic4Length import ExamPic4Length
import os

if __name__ == '__main__':
    rawPicPath = os.getcwd() + "/CalcLength/resources/raw.jpg"
    referencePicPath = os.getcwd() + "/CalcLength/resources/reference_pseudo.png"
    targetPicPath = os.getcwd() + "/CalcLength/resources/target_pseudo.png"
    ep1 = ExamPic4Length(rawPicPath, referencePicPath, targetPicPath, 1700)
    ep1.getLength()
