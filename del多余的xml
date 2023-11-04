import os

image_folder_path = r'F:\HuoChe\two_stage\Tmodel\images'
label_folder_path = r'F:\HuoChe\two_stage\Tmodel\Annotations'
#
image_files = os.listdir(image_folder_path)
label_files = os.listdir(label_folder_path)

image_set = set([os.path.splitext(filename)[0] for filename in image_files])
label_set = set([os.path.splitext(filename)[0] for filename in label_files])

missing_label_files = label_set - image_set

# 遍历label文件名集合，删除对应的标签文件
for label in label_set:
    if label in missing_label_files:
        label_file = os.path.join(label_folder_path, label + '.xml')
        os.remove(label_file)
