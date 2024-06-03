import os
import xml.etree.ElementTree as ET

# 指定文件夹路径
folder_path = r'F:\HuoChe\103_test\103\HB\annotations'  # 将路径替换为实际的文件夹路径

# 初始化一个空列表来存储满足条件的文件名
matching_filenames = []

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.xml'):
        xml_path = os.path.join(folder_path, filename)

        # 解析XML文件
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 查找<object>标签中的<name>标签
        for object_elem in root.findall('.//object'):
            name_elem = object_elem.find('name')
            if name_elem is not None and name_elem.text == '1031_5':
                matching_filenames.append(filename)
                break

# 将满足条件的文件名保存在TXT文件中
with open(r'F:\HuoChe\103_test\103\HB\1031_5.txt', 'w') as file:
    for filename in matching_filenames:
        file.write(filename + '\n')
