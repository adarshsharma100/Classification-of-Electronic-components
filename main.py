import ultralytics 
from ultralytics import YOLO 
model=YOLO("yolov8m.pt")
model.train(data="C:/Users/ADARSH SHARMA/Downloads/electronic/data.yaml",epochs=15)
