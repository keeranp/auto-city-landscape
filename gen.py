import cv2
import numpy as np
from random import randrange


def random_rectangle(img, depth):
    img_size = img.shape

    pt1 = (randrange(img_size[1]), randrange(
        int(depth * img_size[0]/4), img_size[0]))
    pt2 = (max(pt1[0]+100, randrange(pt1[0], pt1[0] + 200)), img_size[0])

    color = night_filter((randrange(255), randrange(255), randrange(255)), depth)

    cv2.rectangle(img, pt1, pt2, color, -1)


def random_stars(img):
    img_size = img.shape
    x = randrange(img_size[1])
    y = randrange(img_size[0])
    img[y, x] = (255, 255, 255)


def random_moon(img):
    img_size = img.shape
    pt1 = (randrange(img_size[1]), randrange(int(img_size[0]/3)))

    cv2.circle(img, pt1, 120, (250, 250, 250), -1)


def night_filter(color, depth):
    B = 1
    G = .5
    R = .5

    return (color[0] * B/(depth * depth), color[1] * G/(depth * depth), color[2] * R/(depth * depth))


def sky(img):
    BLUE_VALUE = 140
    step = int(img.shape[0]/BLUE_VALUE)
    total = 0

    for i in range(0, BLUE_VALUE):
        for j in range(total, total + step):
            img[j, :] = (i, 0, 0)
        total += step


def crop(img, w, h):
    center = (img.shape[0]/2, img.shape[1]/2)
    x = center[1] - w/2
    y = center[0] - h/2

    return img[int(y):int(y+h), int(x):int(x+w)]


img = np.ones((800, 1300, 3), np.uint8)

sky(img)

for i in range(1000):
    random_stars(img)

random_moon(img)

for i in range(100):
    random_rectangle(img, 1.25)

for i in range(150):
    random_rectangle(img, 2)

for i in range(200):
    random_rectangle(img, 3)

img = crop(img, 1280, 720)

cv2.imshow('test', img)
cv2.waitKey()

cv2.imwrite('test.png', img)
