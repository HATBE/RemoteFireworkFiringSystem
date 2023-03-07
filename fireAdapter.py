import RPi.GPIO as GPIO
import sys
import time

# DEFINED PINS
pins = [
        3, # GPIO 2  || channel 1
        5, # GPIO 3  || channel 2
        7, # GPIO 4  || channel 3
        11 # GPIO 17 || channel 4
]

args = sys.argv
args.pop(0)

# -----------------------------------------
# ----------------------------------------- FUNCTIONS
# -----------------------------------------

# cleanup GPIO pins &% exit script with defined error code
def exitSave(exitCode = 0):
        GPIO.cleanup()
        sys.exit(exitCode)

# setup GPIO pins
def configureGPIO():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        for pin in pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.HIGH)

# fire a single GPIO pin
def firePin(pinNr):
        GPIO.output(pinNr, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(pinNr, GPIO.HIGH)

# fire all GPIO pins at once
def fireAllPins():
        # enable pins
        for pin in pins:
                GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)
        # disable pins
        for pin in pins:
                GPIO.output(pin, GPIO.HIGH)

# -----------------------------------------
# ----------------------------------------- SCRIPT
# -----------------------------------------

configureGPIO()

if len(sys.argv) == 1:
        # \/ START ----------------------------------------- FIRE ALL \/
        fireAllPins()

        exitSave(0)
        # /\ END ----------------------------------------- FIRE ALL /\
elif len(sys.argv) == 2:
        # \/ START ----------------------------------------- FIRE \/
        if not args[1].isdigit():
                print("Please provide a number between 1 and {}".format(len(pins)))
                exitSave(1)
                
        if int(args[1]) > len(pins) or int(args[1]) <= 0:
                print("Please provide a number between 1 and {}".format(len(pins)))
                exitSave(1)
        
        pin = pins[int(args[0]) - 1]

        firePin(pin)

        exitSave(0)
        # /\ END ----------------------------------------- FIRE /\
else:
        print("Please provide a valid option 'fireall' or 'fire <num>'")
        exitSave(1)