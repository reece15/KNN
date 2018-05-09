#coding:utf-8



from PIL import Image,ImageDraw, ImageFilter,ImageEnhance

import os
import config


def clean_point_by_rgb(im, point):
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pix=im.getpixel((i,j))
            if pix not in point:
                 im.putpixel((i,j),255)
            else:
               im.putpixel((i,j),0)


def most_pix(im, white_point = 200):

    point_mapping = {}

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pix=im.getpixel((i,j))

            if pix > white_point:
                continue
            p = point_mapping.get(pix)
            if p is None:
                point_mapping[pix] = 0
                p = 0
            p += 1
            point_mapping[pix] = p

    return sorted(point_mapping.items(), key=lambda x:x[1], reverse=True)


def is_alone(im, i, j, w,h, white_point, threshod):

    if im.getpixel((i, j)) > white_point:
        return True

    else:
        index = 0
        if i-1 >= 0 and im.getpixel((i-1, j)) < white_point:
            index += 1
        if i-1 >= 0 and j-1>=0 and im.getpixel((i-1, j-1)) < white_point:
            index += 1
        if i-1 >= 0 and j+1<h and  im.getpixel((i-1, j+1)) < white_point:
            index += 1
        if j-1>=0 and  im.getpixel((i, j-1)) < white_point:
            index += 1
        if j+1<h and  im.getpixel((i, j+1)) < white_point:
            index += 1
        if i+1 < w and  im.getpixel((i+1, j)) < white_point:
            index += 1

        if i+1 < w and j+1<h and  im.getpixel((i+1, j+1)) < white_point:
            index += 1
        if i+1 < w and j-1>=0 and  im.getpixel((i+1, j-1)) < white_point:
            index += 1

    if index >= threshod:
        print(index)
    return index <= threshod



def get_alone(im, white_point = 200, threshod=3):
    alone_point = set()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if is_alone(im, i, j, im.size[0], im.size[1], white_point, threshod):
                alone_point.add((i,j))
    return alone_point

def clean_alone(im, alone_point):
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if (i,j) in alone_point:
                im.putpixel((i,j), 255)
            else:
                im.putpixel((i,j), 0)

def clean_point(im):

    alone_point = get_alone(im, threshod=4)

    clean_alone(im, alone_point)


def get_first_col(im, reverse=False):


    if reverse:
        a = range(im.size[0]-1,-1, -1)
    else:
        a = range(im.size[0])

    for i in a:
        for j in range(im.size[1]):
            if im.getpixel((i,j)) == 0:
                return i


if __name__ == "__main__":
    import random

    files = os.listdir(config.DATA_PATH)
    data = [random.choice(files) for i in range(10)]

    img = None

    ls = []
    rs = []

    for i in data:
        p = os.path.join(config.DATA_PATH, i)
        im=Image.open(p)
        clean_point(im)
        l = get_first_col(im)
        r = get_first_col(im, reverse=True)

        ls.append(l)
        rs.append(r)

        region = (0,0,56,im.size[1])
        cropImg = im.crop(region)
        cropImg.show()
        input()
    print(min(ls), max(rs))