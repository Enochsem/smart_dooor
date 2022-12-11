#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
from ultrasonic import distanceToOpenDoor
from nfc import *
from lcd import lcd_display
#from buzzer import *
#from servo import setAngle

#SETING BOARD MODE
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


def buzz(state):
    GPIO.setmode(GPIO.BOARD)
    BUZZER_PIN = 40
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    FREQUENCY = 100
    pwm = GPIO.PWM(BUZZER_PIN, FREQUENCY)
    pwm.start(0)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    pwm.ChangeDutyCycle(10)
    led(state)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    
    
def led(state):
    delay = 1
    if state == True:
        GREEN_LED_PIN = 36
        GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

        GPIO.output(GREEN_LED_PIN,GPIO.HIGH)
        sleep(delay)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    else:                
        RED_LED_PIN = 38
        GPIO.setup(RED_LED_PIN, GPIO.OUT)
        
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        sleep(delay)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        

def authenticateNFC(card_id):
    for i in range(len(nfc_list)):
        for element in nfc_list[i]:
            if nfc_list[i][element] == str(card_id) :
                #print("yes")
                return True
    return False


def relayLock(state):
    GPIO.setmode(GPIO.BOARD)
    RELAY_PIN = 12
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    if state == True: #"open"
        GPIO.output(RELAY_PIN, GPIO.HIGH) 
    else:
        GPIO.output(RELAY_PIN, GPIO.LOW) 

def setAngle(angle):
    SERVO_PIN = 11
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    pwm=GPIO.PWM(SERVO_PIN, 50)
    pwm.start(0)
    duty = angle / 18 + 3
    GPIO.output(SERVO_PIN, GPIO.HIGH) #True
    pwm.ChangeDutyCycle(duty)
    sleep(0.5)
    GPIO.output(SERVO_PIN, GPIO.LOW) #False
    


nfc_list = [{"card_id":"926375418169", "card_text":"PS/CSC/18/0090"},
            {"card_id":"925604332359", "card_text":"cPsNCvKPHX8dTXEug9eYqek2SAjiNnd39TqMU2Gqe9ypxstv"},
            {"card_id":"661667388157", "card_text":"to56Ur48kU29wCMJs8Pm0ozED3WVffmVoJvXIK8e7Bnnr6Qt"}
           ]

def open_door():
    print("opening ...")
    relayLock(True)
    setAngle(150)
    
def close_door():
    print("clossing ...")
    setAngle(0)
    sleep(1)
    relayLock(False)

def main ():
    distance = distanceToOpenDoor()
    print(distance)
    if distance >= 20:
        open_door()
        sleep(2)
        close_door()
        
    card_id = readNFC()
    lcd_display(card_id,"",1)
    print(card_id)
    isValid = authenticateNFC(card_id)
    print(isValid)
    if isValid == True:
        buzz(isValid)
        lcd_display("Please Step back","Opening Door",2)
        #relayLock(isValid)
        #setAngle(150)
        open_door()
        #wait for the person to enter
        sleep(2)
        close_door()
        #setAngle(0)
        #sleep(1)
        #relayLock(False)


try:
    main() #process
    #pass
except KeyboardInterrupt:
    print("ended")
finally:
    GPIO.cleanup()