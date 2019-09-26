import paho.mqtt.client as mqtt

#Local MQTT
MQTT_LOCAL_HOST="mosquitto"
MQTT_LOCAL_PORT=1883
MQTT_LOCAL_TOPIC = "face_detection"

#Remote MQTT

MQTT_REMOTE_HOST="172.17.0.2"
MQTT_REMOTE_PORT=1883
MQTT_REMOTE_TOPIC = "face_detection"

def on_connect_local(client, userdata, flags, rc):
	print("local connection:" + str(rc))
	client.subscribe(MQTT_LOCAL_TOPIC)

def on_connect_remote(client, userdata, flags, rc):
	print("remote connection:" + str(rc))

def on_message(client, userdata,msg):
	client.publish(MQTT_REMOTE_TOPIC, payload=msg.payload, qos=0, retain=False)

local_mqtt = mqtt.Client()
local_mqtt.on_connect = on_connect_local
local_mqtt.connect(MQTT_LOCAL_HOST, MQTT_LOCAL_PORT, 60)

remote_mqtt = mqtt.Client()
remote_mqtt.on_connect = on_connect_remote
remote_mqtt.connect(MQTT_REMOTE_HOST, MQTT_REMOTE_PORT, 60)

local_mqtt.loop_forever()
