"""
Author: dpsfigo
Date: 2025-07-04 11:28:15
LastEditors: dpsfigo
LastEditTime: 2025-07-04 11:37:39
Description: 请填写简介
"""

from torchvision import transforms
import cv2

img_path = "./dataset/train/ants/0013035.jpg"
img = cv2.imread(img_path)
tensor_trans = transforms.ToTensor()
img_tensor = tensor_trans(img)
print(img_tensor)

transforms.ToPILImage(img_tensor)
