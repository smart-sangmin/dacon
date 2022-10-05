import cv2
import pandas as pd
# train, val
# vertical = pd.DataFrame({"img_path": [], "text": []})
# horizontal = pd.DataFrame({"img_path": [], "text": []})

# test
vertical = pd.DataFrame({"img_path": []})
horizontal = pd.DataFrame({"img_path": []})

with open('/home/ubuntuking/deep-text-recognition-benchmark/data/test.csv') as data:
    lines = data.readlines()

total_lines_count = len(lines)
for i in range(1, total_lines_count):
    # path, label = lines[i].strip('\n').split(',')
    path = lines[i].strip('\n')
    p = './data/img/' + path
    img = cv2.imread(p)
    imgH, imgW, _ = img.shape

    if imgH > imgW * 1.5:
        vertical.loc[len(vertical)] = [path]
    else:
        horizontal.loc[len(horizontal)] = [path]

vertical.to_csv('./data/only_vertical_test.csv',
                index=False, encoding="utf-8-sig")
horizontal.to_csv('./data/only_horizontal_test.csv',
                  index=False, encoding="utf-8-sig")
