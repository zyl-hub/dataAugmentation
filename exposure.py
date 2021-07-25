from skimage import exposure
from PIL import Image
import numpy as np
import glob

def imgExposure(imgPath, image_out_path, gamma):
    img = Image.open(imgPath)
    img = np.array(img)
    exposureArray = exposure.adjust_gamma(img, gamma)
    exposurePhoto = Image.fromarray(exposureArray)
    exposurePhoto.save(image_out_path + '/' + imgPath[7:])


if __name__=="__main__":
    imgpathList = glob.glob(r"imgRaw/*.jpg")
    image_out_path = "exposure"
    datasize = len(imgpathList)

    for i in range(datasize):
        print("\033[0;32;40mProcessing file " + str(i+1) + "/" + str(datasize) + ": " + imgpathList[i][7:]+"\033[0m")
        imgExposure(imgpathList[i], image_out_path, 3)

