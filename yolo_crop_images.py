import os
import cv2


image_dir = r'F:\HuoChe\two_stage\359rh_L\images'
label_dir = r'F:\HuoChe\yolov5_6.0\runs\detect\1step\359rh_L\labels'
save_dir = r'F:\HuoChe\two_stage\359_2step'
image_path = os.listdir(image_dir)

image = cv2.imread(os.path.join(image_dir, image_path[0]))
print(image.shape)

h, w, c = image.shape

def letterbox(image, size):
    original_h, original_w, original_c = image.shape
    scale = min(original_h / size, original_w / size)
    print(scale)

txt_path = os.listdir(label_dir)
for txt in txt_path:
    with open(os.path.join(label_dir, txt), "r", encoding="utf-8") as file:

        lines = file.readlines()
        numbers = []
        for line in lines:
            line_numbers = line.split()

            # 将数字字符串转换为整数，并添加到 numbers 列表
            numbers.extend([float(num) for num in line_numbers])
        print(numbers)
        # x_center = w * float(numbers[1])  # x中心坐标
        # y_center = h * float(numbers[2])  # y中心坐标
        # width = int(w * float(numbers[3]))  # aa[3]图片width
        # height = int(h * float(numbers[4]))
        #
        # x_left_top = int(x_center - width / 2)
        # y_left_top = int(y_center - height / 2)
        #
        # x_right_bottom = int(x_center + width / 2)
        # y_right_bottom = int(y_center + height / 2)
        #
        # print(f'{x_center=}, {y_center=}, {width=}, {height=}, {x_left_top=}')

        x1 = int(numbers[1])
        y1 = int(numbers[2])
        x2 = int(numbers[3])
        y2 = int(numbers[4])

        img = cv2.imread(os.path.join(image_dir, txt[:-4] + '.jpg'))
        roi = img[y1:y2, x1:x2]


        cv2.imwrite(os.path.join(save_dir,  txt[:-4] + '.jpg'), roi)
