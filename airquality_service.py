import time
import RPi.GPIO as GPIO
import mh_z19
import sys
import sqlite3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

LED_G = 23
LED_Y = 24
LED_R = 25

GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(LED_R, GPIO.OUT)

def set_green():
    GPIO.output(LED_G, GPIO.HIGH)

def set_yellow():
    GPIO.output(LED_Y, GPIO.HIGH)

def set_red():
    GPIO.output(LED_R, GPIO.HIGH)

def set_clear():
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_Y, GPIO.LOW)
    GPIO.output(LED_R, GPIO.LOW)

loopvar = True

while loopvar:
    try:
        co2=mh_z19.read_all()['co2']
        loopvar = False
    except KeyError:
        print("Error reading. Trying again!")

dbcon = sqlite3.connect('/home/pi/airquality.db')
dbcon.execute('''INSERT INTO airquality (date, co2) VALUES (datetime(CURRENT_TIMESTAMP, 'localtime'), ?)''',(co2,))
dbcon.commit()
dbcon.close()

set_clear()


try:
    if co2 < 600:
        set_green()
    elif co2 < 800:
        set_green()
        set_yellow()
    elif co2 < 1000:
        set_yellow()
    elif co2 < 1500:
        set_yellow()
        set_red()
    elif co2 >= 1500:
        set_red()
    else:
        set_clear()
except:
    sys.exit()
sys.exit()
