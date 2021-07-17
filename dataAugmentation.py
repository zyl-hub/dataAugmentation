import numpy as np
import glob
from PIL import Image


def dataAugmentation(imgPath, imgOutPath):
    img = Image.open(imgPath)
    img = np.array(img)
    WIDTH, HEIGHT, DEPTH = img.shape
    print("\033[0;32;40m1/6: Flipping\033[0m")
    flipped_img = np.fliplr(img)
    Leftimg = img.copy()
    Rightimg = img.copy()
    Upimg = img.copy()
    Downimg = img.copy()
    noiseimg = img.copy()
    print("\033[0;32;40m2/6: Left Shifting\033[0m")
    for i in range(HEIGHT, 1, -1):
        for j in range(WIDTH):
            if (i < HEIGHT - 20):
                Leftimg[j][i] = Leftimg[j][i - 20]
            elif (i < HEIGHT - 1):
                Leftimg[j][i] = 0
    print("\033[0;32;40m3/6: Right Shifting\033[0m")
    for j in range(WIDTH):
        for i in range(HEIGHT):
            if (i < HEIGHT - 20):
                Rightimg[j][i] = Rightimg[j][i + 20]
    print("\033[0;32;40m4/6: Up Shifting\033[0m")
    for j in range(WIDTH):
        for i in range(HEIGHT):
            if (j < WIDTH - 20 and j > 20):
                Upimg[j][i] = Upimg[j + 20][i]
            else:
                Upimg[j][i] = 0
    print("\033[0;32;40m5/6: Down Shifting\033[0m")
    for j in range(WIDTH, 1, -1):
        for i in range(278):
            if (j < 144 and j > 20):
                Downimg[j][i] = Downimg[j - 20][i]

    print("\033[0;32;40m6/6: Noise\033[0m")
    noisePower = 5
    noise = np.random.randint(noisePower, size=(WIDTH, HEIGHT, DEPTH), dtype='uint8')
    for i in range(WIDTH):
        for j in range(HEIGHT):
            for k in range(DEPTH):
                if (noiseimg[i][j][k] <= 255 - noisePower + 1):
                    noiseimg[i][j][k] += noise[i][j][k]


    imFlipped = Image.fromarray(flipped_img)
    imLeftimg = Image.fromarray(Leftimg)
    imRightimg = Image.fromarray(Rightimg)
    imUpimg = Image.fromarray(Upimg)
    imDownimg = Image.fromarray(Downimg)
    imnoise = Image.fromarray(noiseimg)
    imFlipped.save(imgOutPath + "/" + "Flipped" + imgPath[7:])
    imLeftimg.save(imgOutPath + "/" + "Left" + imgPath[7:])
    imRightimg.save(imgOutPath + "/" + "Right" + imgPath[7:])
    imUpimg.save(imgOutPath + "/" + "Up" + imgPath[7:])
    imDownimg.save(imgOutPath + "/" + "Down" + imgPath[7:])
    imnoise.save(imgOutPath + "/" + "Noise" + imgPath[7:])

if __name__=="__main__":
    imgpathList = glob.glob(r"imgRaw/*.jpg")
    image_out_path = "Augmentation"
    datasize = len(imgpathList)

    for i in range(datasize):
        print("\033[0;32;40mProcessing file " + str(i+1) + "/" + str(datasize) + ": " + imgpathList[i][7:]+"\033[0m")
        dataAugmentation(imgpathList[i], image_out_path)

