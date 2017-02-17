import RPi.GPIO as GPIO
import time

def webstart():
    startled=05
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(startled, GPIO.OUT)
    return 0

def ledstart():
    startled=05
    GPIO.output(startled, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(startled, GPIO.LOW)
    return 0

if __name__=='__main__':
    webstart()
