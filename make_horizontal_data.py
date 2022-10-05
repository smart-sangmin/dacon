import os
import json
import cv2
import pandas as pd

train = pd.read_csv(
    '/home/ubuntuking/deep-text-recognition-benchmark/s.csv')

count = 0
for path in sorted(os.listdir('/home/ubuntuking/deep-text-recognition-benchmark/horizontal_label')):
    # if count > 20000:
    # break
    with open('/home/ubuntuking/deep-text-recognition-benchmark/horizontal_label/'+path) as f:
        data = json.load(f)
    filename = './horizontal_img/' + data['images'][0]['file_name']
    img = cv2.imread(filename)
    if img is None:
        print(path, 'json파일만 있고 이미지가 없음')
        continue
    for d in data['annotations']:
        # csv data
        text = d['text']
        if text.lower() == 'xxx':
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
        save_file_name = "./cropped_horizontal_img/"+str(count)+'.png'
        cv2.imwrite(save_file_name, cropped_img)

        # df에 추가
        train.loc[len(train)] = [save_file_name, text]
        if count % 1000 == 0:
            print(count, "writing")

        count += 1
train.to_csv('./train_custom.csv', index=False, encoding="utf-8-sig")
