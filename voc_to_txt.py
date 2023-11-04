# encode=gbk
import os  # os：操作系统相关的信息模块
import random  # 导入随机函数
import copy

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ['355', '359']  # ZCB

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    # in_file = open('/Users/youxinlin/Desktop/datasets/dataset-floats/Annotations/%s.xml'%(image_id))

    # out_file = open('/Users/youxinlin/Desktop/datasets/dataset-floats/%s.txt'%(image_id),'w') #生成txt格式文件

    in_file = open(r'F:\HuoChe\two_stage\Tmodel\annotations\%s.xml' % (image_id), encoding="gb18030", errors='ignore')

    out_file = open(r'F:\HuoChe\two_stage\Tmodel\labels\%s.txt' % (image_id), 'w')  # 生成txt格式文件
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == '__main__':
    # 存放原始图片地址
    data_base_dir = r"F:\HuoChe\two_stage\Tmodel\images"
    file_list = []  # 建立列表，用于保存图片信息
    # 读取图片文件，并将图片地址、图片名和标签写到txt文件中
    # write_file_name =r'E:\HL\HXSN\yolov5-master\data\snd_4track\val\label/test.txt'
    # write_file = open(write_file_name, "w") #以只写方式打开write_file_name文件
    for file in os.listdir(data_base_dir):  # file为current_dir当前目录下图片名
        if file.endswith(".jpg"):  # 如果file以jpg结尾
            write_name = file  # 图片路径 + 图片名 + 标签
            write_name = os.path.splitext(write_name)[0]
            print(write_name)
            file_list.append(write_name)  # 将write_name添加到file_list列表最后
    sorted(file_list)  # 将列表中所有元素随机排列
    number_of_lines = len(file_list)  # 列表中元素个数
    print(number_of_lines)
    # #将图片信息写入txt文件中，逐行写入
    # for current_line in range(number_of_lines):
    #     write_file.write(file_list[current_line] + '\n')
    # #关闭文件
    # write_file.close()
    # print(image_ids_train)
    for image_id in file_list:
        # print(image_id)
        convert_annotation(image_id)
