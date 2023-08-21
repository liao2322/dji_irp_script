import os
import cv2
import numpy as np
from pyexiv2 import Image

tsdk = r'D:\tsdk\tsdk\x64\Debug\tsdk.exe'
path = 'D:/yolov7/runs/detect/exp48/'
savepath = "D:/yolov7/runs/detect/exp48_test"
os.makedirs(savepath, exist_ok=True)

distance = 25.0
emissivity = 0.95
humidity = 45
reflection = 51.8


def use_tsdk(tsdk, path, savepath):
    print('start')
    imgnamelist = os.listdir(path)
    for imgname in imgnamelist:
        if "i" in imgname:
            portion = os.path.splitext(imgname)
            coreimgname = portion[0]
            param = '-s ' + path + imgname + ' -a measure -o ' + savepath + coreimgname + '.raw' + ' --distance ' + str(
                distance) + ' --emissivity ' + str(emissivity) + ' --humidity ' + str(humidity) + ' ' \
                                                                                                  '' \
                                                                                                  '' \
                                                                                                  '--reflection ' + str(
                reflection)
            r_v = os.system(tsdk + ' ' + param)
            print(r_v)




use_tsdk(tsdk, path, savepath)

