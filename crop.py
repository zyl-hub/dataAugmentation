import glob
import xml.dom.minidom
import cv2

def cropFromXml(xmlPath, imgPath, imgOutPath):
    dom = xml.dom.minidom.parse(xmlPath)
    root = dom.documentElement
    name = root.getElementsByTagName('name')
    bndbox = root.getElementsByTagName('bndbox')
    print(name[0].firstChild.data)
    for i in range(bndbox.length):
        flag = name[i].firstChild.data == 'yellow_back' or name[i].firstChild.data == 'red_stop'
        if flag:
            xmin = bndbox[i].getElementsByTagName('xmin')[0]
            ymin = bndbox[i].getElementsByTagName('ymin')[0]
            xmax = bndbox[i].getElementsByTagName('xmax')[0]
            ymax = bndbox[i].getElementsByTagName('ymax')[0]
            xminValue = int(xmin.firstChild.data)
            yminValue = int(ymin.firstChild.data)
            xmaxValue = int(xmax.firstChild.data)
            ymaxValue = int(ymax.firstChild.data)
            print(xminValue, xmaxValue, yminValue, ymaxValue)
            img = cv2.imread(imgPath)
            # print(imgPath)
            # print(imgPath[14:])
            # print(img.shape)
            cropped = img[yminValue:ymaxValue, xminValue:xmaxValue]
            # print(cropped.shape)
            # cv2.imwrite(imgOutPath + "/" + imgPath[14:], cropped)
            if name[i].firstChild.data == 'yellow_back':
                cv2.imwrite(imgOutPath + '/' + 'yellow_back_' + str(i) + '_' + imgPath[7:], cropped)
            else:
                cv2.imwrite(imgOutPath + '/' + 'red_stop_' + str(i) + '_' + imgPath[7:], cropped)
            # print(imgOutPath + "/" + imgPath[14:])


if __name__ == "__main__":
    xmlPathList = glob.glob(r'cropxml/*.xml')
    imgPathList = glob.glob(r'imgRaw/*.jpg')
    print(imgPathList[10])
    print(xmlPathList[10])
    for i in range(len(imgPathList)):
        cropFromXml(xmlPathList[i], imgPathList[i], 'cropped')
