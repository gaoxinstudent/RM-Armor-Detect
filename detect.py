from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("")#.pt路径
# 接受所有格式-image/dir/Path/URL/video/PIL/ndarray。0用于网络摄像头
#results = model.predict(source="0",show=True)
results = model.predict(source="", show=True,save_txt=False) # 展示预测结果
