import os
from PIL import Image
import cv2
import pandas as pd

for path in os.listdir('./data/not_lmdb/test/'):
    img1 = Image.open('./data/not_lmdb/test/' + path)

    if img1.size[0] * 1.5 < img1.size[1]:

        # print(str(path) + str(img1.size))
        print('./data/not_lmdb/test/' + path)
        img1 = img1.transpose(Image.ROTATE_90)
        save_file_name = './data/not_lmdb/test_rotate/' + path
        img1.save(save_file_name, 'png')
    # test.loc[len(test)] = [save_file_name, text]
