#批量重命名文件
import os

path = "VOCdevkit/VOC2007/JPEGImages" #放图片的文件夹
index_no = 1
for file in os.listdir(path):
    imagepath = os.path.join(path, file)
    newname = str(index_no) + '.jpg'
    newimagename = os.path.join(path, newname)
    os.rename(imagepath, newimagename)
    print("以前的文件名和对应现在的序号", file + '---' + str(index_no))
    index_no += 1
