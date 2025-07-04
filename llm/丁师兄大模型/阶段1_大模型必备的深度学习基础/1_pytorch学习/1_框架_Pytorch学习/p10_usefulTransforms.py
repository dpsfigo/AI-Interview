"""
Author: dpsfigo
Date: 2025-07-04 13:57:27
LastEditors: dpsfigo
LastEditTime: 2025-07-04 17:52:37
Description: 请填写简介
"""

"""
Author: dpsfigo
Date: 2025-07-04 13:57:27
LastEditors: dpsfigo
LastEditTime: 2025-07-04 13:57:27
Description: 请填写简介
"""

import torchvision
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader

test_data = torchvision.datasets.CIFAR10(
    "./dataset", download=True, train=False, transform=torchvision.transforms.ToTensor()
)

test_loader = DataLoader(
    dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=True
)

writer = SummaryWriter("dataloader")
for epoch in range(2):
    step = 0
    for data in test_loader:
        imgs, targets = data
        writer.add_images("Epoch:{}".format(epoch), imgs, step)
        step += 1

writer.close()
