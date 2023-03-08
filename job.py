import RPi.GPIO as GPIO
from os.path import exists
import sys
import json
import time

# -----------------------------------------
# ----------------------------------------- DEFINE PINS
# -----------------------------------------

ledPin = 16 # GPIO 23
btnPin = 12 # GPIO 18

# -----------------------------------------
# ----------------------------------------- FUNCTIONS
# -----------------------------------------

# cleanup GPIO pins && exit script with defined error code
def exitSave(exitCode = 0):
        GPIO.cleanup()
        sys.exit(exitCode)

# setup GPIO pins
def configureGPIO():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        # configure led
        GPIO.setup(ledPin, GPIO.OUT) 

         # configure button
        GPIO.setup(btnPin, GPIO.IN) 

# -----------------------------------------
# ----------------------------------------- SCRIPT
# -----------------------------------------

configureGPIO()

lastState = GPIO.input(btnPin)

GPIO.output(ledPin, lastState)

while True:
    currentState = GPIO.input(btnPin)

    if(lastState != currentState):
        lastState = currentState
        # if the switch is on, red led indicates the device is armed
        GPIO.output(ledPin, currentState)
            
    time.sleep(0.1)

exitSave()