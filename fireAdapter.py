import RPi.GPIO as GPIO
import sys
import time

# DEFINED PINS
pins = [
        3, # GPIO 2
        5, # GPIO 3
        7, # GPIO 4
        11 # GPIO 17
]

args = sys.argv
args.pop(0)

def exitSave(exitCode = 0):
        GPIO.cleanup()
        sys.exit(exitCode)

def configureGPIO():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        for pin in pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.HIGH)

configureGPIO()

if len(sys.argv) != 1:
        print("Please provide a number between 1 and {}".format(len(pins)))
        exitSave(1)
if not args[0].isdigit():
        print("Please provide a number between 1 and {}".format(len(pins)))
        exitSave(1)
if int(args[0]) > len(pins) or int(args[0]) <= 0:
        print("Please provide a number between 1 and {}".format(len(pins)))
        exitSave(1)

pin = pins[int(args[0]) - 1]

GPIO.output(pin, GPIO.LOW)
time.sleep(.5)
GPIO.output(pin, GPIO.HIGH)

exitSave()