#servo
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
SERVO_PIN = 11
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm=GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

SLEEP_TIME = 1
print("starting....")

#pwm.ChangeDutyCycle(5) # left -90 deg position
#sleep(SLEEP_TIME)
#print("starting")
#pwm.ChangeDutyCycle(7.5) # neutral position
#sleep(SLEEP_TIME)
#pwm.ChangeDutyCycle(10) # right +90 deg position
#sleep(SLEEP_TIME)

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(SERVO_PIN, GPIO.HIGH) #True
    pwm.ChangeDutyCycle(duty)
    sleep(SLEEP_TIME)
    GPIO.output(SERVO_PIN, GPIO.LOW) #False
    


setAngle(0)
GPIO.cleanup()