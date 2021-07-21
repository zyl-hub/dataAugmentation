import glob
import os

if __name__ == "__main__":
    imgpathList = glob.glob(r"Selected/*.jpg")
    for _ in imgpathList:
        xmlPath = "annotations\\\\" + _[9:-4] + ".xml"
        os.popen('copy '+ xmlPath + ' ' + 'selectedAnno\\' + xmlPath[12:])
        print('copy '+ xmlPath + ' ' + 'selectedAnno\\' + xmlPath[12:])