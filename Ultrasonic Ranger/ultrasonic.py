import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

TRIGER_PIN = 32
GPIO.setup(TRIGER_PIN, GPIO.OUT)
ECHO_PIN = 31
GPIO.setup(ECHO_PIN, GPIO.IN)


def distanceToOpenDoor():
    try:
        GPIO.output(TRIGER_PIN, GPIO.LOW)

        print ("Waiting for sensor to settle")

        time.sleep(2)

        print ("Calculating distance")

        GPIO.output(TRIGER_PIN, GPIO.HIGH)
        
        micro_seconds10 = 0.00001
        time.sleep(micro_seconds10)

        GPIO.output(TRIGER_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN)==0:
            pulse_start_time = time.time()
        while GPIO.input(ECHO_PIN)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        #print ("Distance: ",distance,"cm")
        return distance
    
    finally:
        GPIO.cleanup()
        
value = distanceToOpenDoor()
print ("Distance: ",value,"cm")