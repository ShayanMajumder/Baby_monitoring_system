# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep
import dht 

def connect_dht11(pin = 14):
    sensor = dht.DHT11(Pin(pin))
    return sensor

def alarm_dht11(sensor, temp_thereshold = 30, humidity_thereshold = 95):
  try:
    temp_alarm = False
    humidity_alarm = False
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    if temp > temp_thereshold:
      temp_alarm = True
    if hum > humidity_thereshold:
      humidity_alarm = True
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    return (temp_alarm or humidity_alarm)
  except OSError as e:
    print('Failed to read sensor.')
    return False