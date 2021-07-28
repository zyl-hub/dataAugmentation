## 图片大小压缩

compress.py可以将imgFromPhoto文件夹中的图片压缩大小之后输出到compress文件夹

## 数据增强

把要增强的图片放到imgRaw文件夹，运行dataAugmentation.py，输出的增强后图片位置在Augmentation文件夹

## 数据选择

imageSelect.py可以根据Selected文件夹中的图片在annotations文件夹中选出其对应的标注xml文件，并将xml文件输出到selectedAnno文件夹

## 图片裁剪

shape.py可以将拍摄的图像大小转换为1280x720，不过只限于对于1440x1080的图片处理，将待处理的图片放到waitingForCut文件夹，处理后的图片会输出到cutted文件夹



test
