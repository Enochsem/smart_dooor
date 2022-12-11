import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
BUZZER_PIN = 40
GPIO.setup(BUZZER_PIN, GPIO.OUT)
RED_LED_PIN = 38
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GREEN_LED_PIN = 36
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

FREQUENCY = 100
pwm = GPIO.PWM(BUZZER_PIN, FREQUENCY)
pwm.start(0)

delay = 1

def buzz(led_state):
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    pwm.ChangeDutyCycle(10)
    ledState(led_state)
    sleep(delay)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.cleanup()


def ledState(state):
    if state == "error":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        sleep(delay)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
    else:
        GPIO.output(GREEN_LED_PIN,GPIO.LOW)
        GPIO.output(GREEN_LED_PIN,GPIO.HIGH)
        sleep(delay)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    
if __name__ == "__main__":
    #buzz("error")
    pass