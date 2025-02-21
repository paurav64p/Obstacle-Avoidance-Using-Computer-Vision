# object_detection.py
import cv2
import numpy as np
import tensorflow as tf
from yolov4.tf import YOLOv4

# Load YOLOv4 Model
yolo = YOLOv4()
yolo.config.parse_config("yolov4.cfg", "yolov4.weights")
yolo.make_model()
yolo.load_weights("yolov4.weights", weights_type="yolo")

def detect_objects(frame):
    boxes, scores, classes, valid_detections = yolo.predict(frame)
    return boxes, scores, classes

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    boxes, scores, classes = detect_objects(frame)
    
    for i in range(len(boxes)):
        if scores[i] > 0.5:
            x, y, w, h = boxes[i]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, str(classes[i]), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow('Obstacle Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

