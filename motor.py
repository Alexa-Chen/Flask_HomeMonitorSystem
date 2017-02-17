#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def motorstart(turn):
    INT1=06
    INT2=13
    INT3=19
    INT4=26
    GPIO.setup(INT1, GPIO.OUT)
    GPIO.setup(INT2, GPIO.OUT)
    GPIO.setup(INT3, GPIO.OUT)
    GPIO.setup(INT4, GPIO.OUT)
    time.sleep(1)
    for ii in range(512/12):
        if turn =='r':
            GPIO.output(INT1, GPIO.HIGH)
            GPIO.output(INT2, GPIO.LOW)
            GPIO.output(INT3, GPIO.LOW)
            GPIO.output(INT4, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(INT1, GPIO.LOW)
            GPIO.output(INT2, GPIO.HIGH)
            GPIO.output(INT3, GPIO.LOW)
            GPIO.output(INT4, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(INT1, GPIO.LOW)
            GPIO.output(INT2, GPIO.LOW)
            GPIO.output(INT3, GPIO.HIGH)
            GPIO.output(INT4, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(INT1, GPIO.LOW)
            GPIO.output(INT2, GPIO.LOW)
            GPIO.output(INT3, GPIO.LOW)
            GPIO.output(INT4, GPIO.HIGH)
            time.sleep(0.01)
        else:
            GPIO.output(INT1, GPIO.LOW)
            GPIO.output(INT2, GPIO.LOW)
            GPIO.output(INT3, GPIO.LOW)
            GPIO.output(INT4, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(INT1, GPIO.LOW)
            GPIO.output(INT2, GPIO.LOW)
            GPIO.output(INT3, GPIO.HIGH)
            GPIO.output(INT4, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(INT1, GPIO.LOW)
            GPIO.output(INT2, GPIO.HIGH)
            GPIO.output(INT3, GPIO.LOW)
            GPIO.output(INT4, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(INT1, GPIO.HIGH)
            GPIO.output(INT2, GPIO.LOW)
            GPIO.output(INT3, GPIO.LOW)
            GPIO.output(INT4, GPIO.LOW)
            time.sleep(0.01)
    return 0
  #  GPIO.cleanup()

if __name__=='__main__':
    motorstart('l')
