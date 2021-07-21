import numpy as np
import glob
from PIL import Image
import cv2

def imgCut(imgPath, imgOutPath):
    img = cv2.imread(imgPath)
    print(imgPath)
    print(imgPath[14:])
    print(img.shape)
    cropped = img[180:900, 80:1360]
    print(cropped.shape)
    cv2.imwrite(imgOutPath +"/"+ imgPath[14:], cropped)
    print(imgOutPath +"/"+ imgPath[14:])



if __name__=="__main__":
    imgpathList = glob.glob(r"waitingForCut/*.jpg")
    imgOutPath = "cutted"
    for _ in imgpathList:
        imgCut(_, imgOutPath)

