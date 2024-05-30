from ultralytics import YOLO

# Load a model
model = YOLO('')  # load an of your model
# model = YOLO('')  # load a custom trained model

# Export the model
model.export(format='openvino',
             dynamic=False,
             imgsz=416,
             int8=True,
             data= ''# your .yaml file 

             )
