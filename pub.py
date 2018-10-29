from time import sleep
import paho.mqtt.client as mqtt

host = '153.126.197.42'
port = 1883
topic = 'topicA'

client = mqtt.Client(protocol=mqtt.MQTTv311)

client.connect(host, port=port, keepalive=60)

client.publish(topic, 'マクロス！')

client.disconnect()
