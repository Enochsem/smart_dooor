#lock system
import RPi.GPIO as GPIO
from time import sleep

def relay ():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    RELAY_PIN = 12
    DELAY = 3
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    #This Turns Relay Off. Brings Voltage to Max GPIO can output ~3.3V
    GPIO.output(RELAY_PIN, 1)
    print("state1")
    sleep(DELAY)
    #Turns Relay On. Brings Voltage to Min GPIO can output ~0V.
    GPIO.output(RELAY_PIN, 0)
    print("state2")
    sleep(DELAY)
    GPIO.cleanup()


#while (True):    
#    try:
#        GPIO.setwarnings(False)
#        GPIO.setmode(GPIO.BOARD)
#        RELAY_PIN = 12
#        DELAY = 1
#        GPIO.setup(RELAY_PIN, GPIO.OUT)
#        #This Turns Relay Off. Brings Voltage to Max GPIO can output ~3.3V
#        
#        GPIO.output(RELAY_PIN, 1)
#        print("off")
#        sleep(DELAY)
#        #Turns Relay On. Brings Voltage to Min GPIO can output ~0V.
#        GPIO.output(RELAY_PIN, 0)
#        print("on")
#        sleep(DELAY)
#    except KeyboardInterrupt:
#        print("Ctrl + c")
#        GPIO.output(RELAY_PIN, 0)
#    finally:
#        GPIO.cleanup()

relay()