from flask_mqtt import Mqtt

mqtt_client = Mqtt()
topic_subscribe = ["mpss_movement_sensor"]
topic_send = "mpss_actuator"