#coding:utf-8
import os
from PIL import Image
import struct
import config
from numpy import array

def read_image(filename="train-images.idx3-ubyte"):

    p = os.path.join(config.DATA_PATH, filename)

    with open(p, "rb") as f:
        index = 0
        buf = f.read()
        magic, images, rows, columns = struct.unpack_from('>IIII' , buf , 0)
        index += struct.calcsize('>IIII')

        s = columns * rows # 每个图片占据空间大小
        fmt = '>{}B'.format(s)
        for i in range(images):
            """
            image = Image.new('L', (columns, rows))
            for x in range(rows):
                for y in range(columns):
                    image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
                    index += struct.calcsize('>B')
            #image.save( os.path.join(config.IMAGE_PATH, str(i) + '.png'))
            """
            arr = struct.unpack_from(fmt, buf, index)
            index += struct.calcsize(fmt)
            yield arr


def read_labels(filename="train-labels.idx1-ubyte"):

    p = os.path.join(config.DATA_PATH, filename)

    with open(p, "rb") as f:
        index = 0
        buf = f.read()
        magic, labels = struct.unpack_from('>II' , buf , index)
        index += struct.calcsize('>II')

        for x in range(labels):
            label = int(struct.unpack_from('>B', buf, index)[0])
            index += struct.calcsize('>B')
            yield label


def save_image():
    index = 0
    columns = 0
    rows = 0

    for image, label in zip(read_image(), read_labels()):

        if columns == 0 or rows == 0:
            columns = rows = int(len(image)**0.5)  # 初始化长宽
        image = Image.new('L', (columns, rows))   # 生成一张图片

        p = 0
        for x in range(rows):
            for y in range(columns):
                image.putpixel((y, x), image[p])   # 绘制像素点
        image.save( os.path.join(config.IMAGE_PATH, '{name}_{index}.png'.format(name=label, index=index)))   # 保存
        print(index, label)  # 显示进度 （绘制图片部分为三层循环，有些耗时）
        index += 1

def loadAll():
    for image, label in zip(read_image(), read_labels()):
        yield (image, label)


def init_all(name="train", labels=True, tras_arr=False):

    image_file = "train-images.idx3-ubyte"
    label_file = "train-labels.idx1-ubyte"

    if name != "train":
        image_file = "t10k-images.idx3-ubyte"
        label_file = "t10k-labels.idx1-ubyte"

    if labels:
        images = list(read_image(image_file))
        labels = list(read_labels(label_file))
        if tras_arr:
            images = array(images)
            labels = array(labels)
        return images, labels

    return list(zip(read_image(image_file), read_labels(label_file)))


if __name__ == "__main__":
    import time
    t = time.time()
    images = init_all()
    t2 = time.time()
    print(len(images), images[0], len(images[0][0]), t2-t)