import os
from glob import glob
import json


root_path = "/SSD/ILSVRC_2012_ImageFolder/train"  # 디렉토리 시작은 /, 디렉토리 끝은 아무것도 없는것으로 지정해줘야함

labels = os.listdir(root_path)
print(labels)
num_labels = len(labels)
print(num_labels)
label_check_split = len(root_path.split('/'))
print(label_check_split)

init_data = {"labels": []}

result = [y for x in os.walk(root_path) for y in glob(os.path.join(x[0], '*'))]
for i in result:
    if '.jpg' in i or '.JPG' in i or '.png' in i or '.PNG' in i or '.jpeg' in i or '.JPEG' in i:
        for j in range(num_labels):
            if i.split('/')[label_check_split] == labels[j]:
                init_data["labels"].append([i.replace(root_path+'/', ''), j])

with open (root_path+"/dataset.json", 'w') as json_file:
    json.dump(init_data, json_file)