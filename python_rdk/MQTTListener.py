import paho.mqtt.client as mqtt
import RobotController as rc

# Configuracion MQTT
broker = "mqtt.dsic.upv.es"
port = 1883
user = "giirob"
passwd = "UPV2024"

# Sirve para los topics derivados de este
topic_commands = "pr2/sahuquillers/#"

# Cuando reciba mensaje
def on_message(mqttc, obj, msg):
    payload = msg.payload.decode("utf-8")
    topic = msg.topic
    rc.handle_message(mqttc, topic, payload)

# Conexion a MQTT
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_message = on_message

mqttc.username_pw_set(username=user, password=passwd)
mqttc.connect(broker, port, 60)

mqttc.subscribe(topic_commands, 0)

mqttc.loop_forever()
