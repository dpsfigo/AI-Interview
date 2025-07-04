"""
Author: dpsfigo
Date: 2025-07-04 11:28:01
LastEditors: dpsfigo
LastEditTime: 2025-07-04 11:48:05
Description: 请填写简介
"""

"""
Author: dpsfigo
Date: 2025-07-04 11:28:01
LastEditors: dpsfigo
LastEditTime: 2025-07-04 11:28:02
Description: 请填写简介
"""

from torch.utils.tensorboard import SummaryWriter
import cv2

writter = SummaryWriter("logs")
img_path = "dataset/train/ants/0013035.jpg"
img = cv2.imread(img_path)
writter.add_image("test", img, 1, dataformats="HWC")

for i in range(100):
    writter.add_scalar("y=x", i, i)
# writter.add_scalar()
writter.close()
