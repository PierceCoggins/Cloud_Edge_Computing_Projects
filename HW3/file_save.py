import paho.mqtt.client as mqtt

#VM MQTT
MQTT_VM_HOST="mosquitto-vm"
MQTT_VM_PORT=1883
MQTT_VM_TOPIC = "face_detection"

def on_connect_local(client, userdata, flags, rc):
	print("local connection:" + str(rc))
	client.subscribe(MQTT_VM_TOPIC)

def on_message(client, userdata,msg):
	print("message received ", str(msg.payload.decode("utf-8")))
	mv str(msg.payload.decode("utf-8")) /mnt/mybucket

local_mqtt = mqtt.Client()
local_mqtt.on_connect = on_connect_local
local_mqtt.connect(MQTT_VM_HOST, MQTT_VM_PORT, 60)
local_mqtt.on_message = on_message


local_mqtt.loop_forever()
