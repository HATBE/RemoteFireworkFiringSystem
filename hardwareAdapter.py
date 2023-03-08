import RPi.GPIO as GPIO
import sys
import time

# -----------------------------------------
# ----------------------------------------- DEFINE PINS
# -----------------------------------------
firePins = [
        7,  # GPIO 4  || channel 1
        29, # GPIO 5  || channel 2
        31, # GPIO 6  || channel 3
        26  # GPIO 7  || channel 4
]
btnPin = 12 # GPIO 18

# prepare args, remove first arg (script name)
args = sys.argv
args.pop(0)

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

        # configure fire pins
        for pin in firePins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.HIGH)

        # configure button
        GPIO.setup(btnPin, GPIO.IN) 

# fire a single GPIO pin
def firePin(pinNr):
        GPIO.output(pinNr, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(pinNr, GPIO.HIGH)

# fire all GPIO pins at once
def fireAllPins():
        # enable pins
        for pin in firePins:
                GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)
        # disable pins
        for pin in firePins:
                GPIO.output(pin, GPIO.HIGH)

def isHardwareDisabled():
        # this is a security messure! there is a switch on the device. If this switch is on disable, the whole divice can't be armed!
        return(GPIO.input(btnPin) != GPIO.HIGH)

# -----------------------------------------
# ----------------------------------------- SCRIPT
# -----------------------------------------

configureGPIO()

# check the arguments provided
if len(sys.argv) == 1:
        if args[0] == 'fireall':
                # \/ START ----------------------------------------- FIRE ALL \/
                if isHardwareDisabled():
                        print("The device is hardware disabled")
                        exitSave(1) 
                fireAllPins()
                exitSave(0)
                # /\ END ----------------------------------------- FIRE ALL /\
        elif args[0] == 'ishardwaredisabled':
                # \/ START ----------------------------------------- IS HARDWARE DISABLED \/
                print(isHardwareDisabled())
                exitSave(0)
                # /\ END ----------------------------------------- IS HARDWARE DISABLED /\
        else:
                print("Please provide a valid option 'fireall' or 'fire <num>' or 'ishardwaredisabled'")
                exitSave(1)
elif len(sys.argv) == 2:
        if args[0] == 'fire':
                # \/ START ----------------------------------------- FIRE \/
                if isHardwareDisabled():
                        print("The device is hardware disabled")
                        exitSave(1) 

                if not args[1].isdigit():
                        print("Please provide a number between 1 and {}".format(len(firePins)))
                        exitSave(1)
                        
                if int(args[1]) > len(firePins) or int(args[1]) <= 0:
                        print("Please provide a number between 1 and {}".format(len(firePins)))
                        exitSave(1)
                
                pin = firePins[int(args[1]) - 1]

                firePin(pin)

                exitSave(0)
                # /\ END ----------------------------------------- FIRE /\
        else:
                print("Please provide a valid option 'fireall' or 'fire <num>' or 'ishardwaredisabled'")
                exitSave(1)
else:
        print("Please provide a valid option 'fireall' or 'fire <num>' or 'ishardwaredisabled'")
        exitSave(1)