import random
import paho.mqtt.publish as publish

while True:
    kWh = round(random.uniform(0.5, 5.0), 2)
    publish.single("sensors/energy", payload=f'{{"kwh": {kWh}}}', hostname="mqtt.broker")
