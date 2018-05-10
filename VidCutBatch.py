import cv2 as cv
import os
from shutil import rmtree
import glob

imgPerSec = 10

dir = "videos/"

data = glob.glob(dir + '*.mp4')

for video in data:
    fileName = os.path.basename(video)
    fileName = os.path.splitext(fileName)[0]

    print("Processing: {}".format(fileName))

    if os.path.exists(dir + fileName):
        rmtree(dir + fileName)
    os.mkdir(dir + fileName)

    count = 0
    working = True

    vid = cv.VideoCapture(video)
    working, image = vid.read()

    while working:
        frames = count * (1000 / imgPerSec)
        vid.set(cv.CAP_PROP_POS_MSEC,(frames))
        working, image = vid.read()

        cv.imwrite(dir + fileName + "/frame{}.png".format(count), image)
        count += 1
        # if count > 500:
        #    working = False

    print("Finished: {}".format(fileName))
