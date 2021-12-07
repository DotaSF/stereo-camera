# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:41:37 2020

@author: 张理官
"""

# filename: camera_configs.py
import cv2
import numpy as np

left_camera_matrix = np.array([[555.3078, 0, 324.3697],
                               [0., 556.2190, 264.5431],
                               [0., 0., 1.]])
left_distortion = np.array([[-0.6281 , 0.7778 , 0.0 , 0.0, 0.00000]])



right_camera_matrix = np.array([[545.3447, 0, 300.0541],
                                [0., 546.3770, 253.4155],
                                [0., 0., 1.]])
right_distortion = np.array([[-0.5805  ,0.4241 , 0. , 0. ,0.00000]])

#om = np.array([-0.05026 , -0.02030, -0.00139]) # 旋转关系向量
R = np.array([[0.9999, 0.0012, -0.0127],
              [-0.0011, 1.0000, 0.0050],
              [0.0127, -0.0050, 0.9999]])
#R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
T = np.array([-15.1468 , 0.0714 ,-3.3802]) # 平移关系向量

size = (640, 480) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)