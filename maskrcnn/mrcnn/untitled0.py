# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:46:20 2024

@author: comyn
"""

import numpy as np
from pycocotools.coco import COCO
import cv2

# Load COCO annotations
coco = COCO("C:/Users/comyn/Downloads/INSTR metric test.v2i.coco-segmentation/test/_annotations.coco.json")  # Provide the path to your COCO annotations file

# Iterate over images
for img_id in coco.imgs:
    img_info = coco.loadImgs(img_id)[0]
    image = cv2.imread("C:/Users/comyn/Downloads/INSTR metric test.v2i.coco-segmentation/test/20240314_095219_jpg.rf.04f812bb8d6c99e31c543890818b8404.jpg")  # Load image

    ann_ids = coco.getAnnIds(imgIds=img_id)
    anns = coco.loadAnns(ann_ids)

    # Initialize an empty mask
    mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    # Convert annotations to pixel-wise mask
    for ann in anns:
        if 'segmentation' in ann:
            mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
            mask += coco.annToMask(ann)

    # Find indices where mask equals 1
            indices = np.where(mask == 1)
            
            test = []
            for i in range(len(indices[0])):
                test.append(indices[0][i]*640+indices[1][i])
            
            # Print or use indices as needed
            print(indices)