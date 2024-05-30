from ultralytics import YOLO

# Load a model
#model = YOLO('yolov8n-pose.yaml')  # build a new model from YAML
# model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)
model = YOLO("C:\\Users\\ssq13\\Desktop\\yolov8_pose_mobilenetv3\\ultralytics\\ultralytics\\cfg\\models\\v8\\yolov8_large_MobileNetV3-pose.yaml").load('C:\\Users\\ssq13\\Desktop\\yolov8_pose_mobilenetv3\\ultralytics\\yolov8n-pose.pt')  # build from YAML and transfer weights
#
# # Train the model
results = model.train(task='pose',
                      data='C:\\Users\\ssq13\\Desktop\\yolov8_pose_mobilenetv3\\ultralytics\\ultralytics\\cfg\\datasets\\coco8-pose.yaml',
                      epochs=1200,
                      imgsz=416,
                      batch=64,
                      device=[0, 1],
                      amp=False,
                      #multi_scale=True,
                      patience=0,
                      save=True,
                      save_period=50,
                      fliplr=0.0,
                      mixup=0.0,
                      pose=15,
                      int8=False,
                      close_mosaic=50)

# Load a model
# model = YOLO('runs/pose/train22/weights/last.pt')  # load a partially trained model
#
# # Resume training
# results = model.train(resume=True)
