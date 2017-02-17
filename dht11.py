#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def restart():
    channel = 17
    data = []
    j = 0
    time.sleep(0.5)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(channel, GPIO.HIGH)
    GPIO.setup(channel, GPIO.IN)

    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        continue
    while j < 40:
        k = 0
        while GPIO.input(channel) == GPIO.LOW:
            continue  
        while GPIO.input(channel) == GPIO.HIGH:
            k += 1
            if k > 100:
                break   
        if k < 14:
            data.append(0)
        else:
            data.append(1)
        j += 1

#    print "sensor is working."
#    print data
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]
    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0
    for i in range(8):
        humidity += humidity_bit[i] * 2 ** (7 - i)
        humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
        temperature += temperature_bit[i] * 2 ** (7 - i)
        temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
        check += check_bit[i] * 2 ** (7 - i)
    tmp = humidity + humidity_point + temperature + temperature_point
    if check == tmp:
        return temperature,humidity
        #print "temperature : %d  humidity : %d"%(temperature,humidity)
    else:
        return '11','11'#若有连接DHT11温湿度传感器将此处改为'0'可正确获取温湿度
       # print "wrong"

def start():
    temperatureshow,humidityshow=restart()
    while temperatureshow and humidityshow =='0':
        temperatureshow,humidityshow=restart()
  #  print "temperature : %s  humidity : %s"%(temperature,humidity)
    return temperatureshow,humidityshow

if __name__=='__main__':
    start()
