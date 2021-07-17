from PIL import Image
import glob


# 只可接收 jpg 和 png 的图片
# 图片不加绝对路径会在当前文件下的目录下找图片
def zip_img_size(img_path, img_quality):
    img = Image.open(img_path)

    img_suffix = img_path[-3:]

    changed_img_name = img_path[:-4] + '.' + img_suffix

    if img_suffix == 'jpg':
        img_suffix = "JPEG"
    else:
        img_suffix = 'PNG'
    # quality 范围在 0-100, 0为最差的
    img.save("compress/"+changed_img_name[13:],  img_suffix, quality=img_quality)
    print("Image saved in " + changed_img_name)


if __name__ == "__main__":
    imgpathList = glob.glob(r"imgFromPhoto/*.jpg")
    for _ in imgpathList:
        zip_img_size(_, 0)

