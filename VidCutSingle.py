import cv2 as cv
import os
from shutil import rmtree
import glob

imgPerSec = 10

name = raw_input("Enter video name: ")

fileName = os.path.basename(name)
fileName = os.path.splitext(fileName)[0]

print("Processing: {}".format(fileName))

if os.path.exists(fileName):
    rmtree(fileName)
os.mkdir(fileName)

count = 0
working = True

vid = cv.VideoCapture(name)
working, image = vid.read()

while working:
    frames = count * (1000 / imgPerSec)
    vid.set(cv.CAP_PROP_POS_MSEC,(frames))
    working, image = vid.read()

    cv.imwrite(fileName + "/frame{}.png".format(count), image)
    count += 1
    # if count > 500:
    #    working = False

print("Finished: {}".format(fileName))
