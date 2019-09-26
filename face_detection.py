import paho.mqtt.client as mqtt
import numpy as np
import cv2

MQTT_HOST="mosquitto"
MQTT_PORT=1883
MQTT_TOPIC="face_detection"

def on_connect(client, userdata, flags, rc):
	print("connected: " + str(rc))

mqttC = mqtt.Client()
mqttC.on_connect = on_connect
mqttC.connect(MQTT_HOST, MQTT_PORT,60)

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # We don't use the color information, so might as well save space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        print("Face identified")
	face = frame[y:y + h, x:x + w]
	rc,faceJpg = cv2.imencode('.png', face) 
	message = faceJpg.tobytes()
	mqttC.publish(MQTT_TOPIC, payload = message, qos=0, retain=False)
	




