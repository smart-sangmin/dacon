import os
import json
import cv2
import matplotlib.pyplot as plt
import pandas as pd

# train = pd.read_csv(
#     '/home/ubuntuking/deep-text-recognition-benchmark/train.csv')

horizontal_val = pd.DataFrame({"img_path": [], "text": []})

count = 0
for path in sorted(os.listdir('./data/val_horizontal_anno')):
    with open('./data/val_horizontal_anno/'+path) as f:
        data = json.load(f)

    filename = './data/val_horizontal_img/' + data['images'][0]['file_name']
    img = cv2.imread(filename)
    if img is None:
        print(path, 'json파일만 있고 이미지가 없음')
        continue
    for d in data['annotations']:
        # csv data
        text = d['text']
        if 'x' in text.lower():
            continue
        # img
        x, y = d['bbox'][0], d['bbox'][1]
        w, h = d['bbox'][2], d['bbox'][3]
        cropped_img = img[y: y + h, x: x + w]
        if cropped_img.size == 0:
            print(
                f'filename: {path}, x:{x}, y:{y}, w:{w}, h:{h} bbox 데이터 잘못 됨')
            continue
        # 이미지 저장
        save_file_name = "./data/val_cropped_horizontal_img/"+str(count)+'.png'
        cv2.imwrite(save_file_name, cropped_img)

        # df에 추가
        horizontal_val.loc[len(horizontal_val)] = [save_file_name, text]
        if count % 1000 == 0:
            print(count, "writing")
        count += 1
horizontal_val.to_csv('./data/val_horizontal.csv',
                      index=False, encoding="utf-8-sig")
