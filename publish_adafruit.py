
import time
from umqtt.robust import MQTTClient
import os
import gc
import sys


# create a random MQTT clientID 
def mqtt_connect_and_publish(username, key,message,id = 1,):
    mqtt_client_id = bytes('client_'+str(id), 'utf-8')

    # connect to Adafruit IO MQTT broker using unsecure TCP (port 1883)
    # 
    # To use a secure connection (encrypted) with TLS: 
    #   set MQTTClient initializer parameter to "ssl=True"
    #   Caveat: a secure connection uses about 9k bytes of the heap
    #         (about 1/4 of the micropython heap on the ESP8266 platform)
    ADAFRUIT_IO_URL = b'io.adafruit.com' 
    ADAFRUIT_USERNAME = bytes(username, 'utf-8')
    ADAFRUIT_IO_KEY = bytes(key, 'utf-8')
    ADAFRUIT_IO_FEEDNAME = b'baby_monitor'

    client = MQTTClient(client_id=mqtt_client_id, 
                        server=ADAFRUIT_IO_URL, 
                        user=ADAFRUIT_USERNAME, 
                        password=ADAFRUIT_IO_KEY,
                        ssl=False)
    try:            
        client.connect()
    except Exception as e:
        print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
        sys.exit()

    mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
    PUBLISH_PERIOD_IN_SEC = 10 
    while True:
        try:
            client.publish(mqtt_feedname,    
                    bytes(str(message), 'utf-8'), 
                    qos=0)  
            time.sleep(PUBLISH_PERIOD_IN_SEC)
        except KeyboardInterrupt:
            print('Ctrl-C pressed...exiting')
            client.disconnect()
            sys.exit()