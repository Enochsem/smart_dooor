#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522

from buzzer import *


#PIN OBJECT
SERVO_PIN = 11

RELAY_PIN = 12


#SETING BOARD MODE
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#PINS CONFIG
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(RELAY_PIN, GPIO.OUT)

#CLASS OBJECTS
nfc_card = SimpleMFRC522()
pwm=GPIO.PWM(SERVO_PIN, 50)


nfc_list = [{"card_id":"926375418169", "card_text":"PS/CSC/18/0090"},
            {"card_id":"925604332359", "card_text":"cPsNCvKPHX8dTXEug9eYqek2SAjiNnd39TqMU2Gqe9ypxstv"},
            {"card_id":"661667388157", "card_text":"to56Ur48kU29wCMJs8Pm0ozED3WVffmVoJvXIK8e7Bnnr6Qt"}
           ]

#ultrasonic
TRIGER_PIN = 32
GPIO.setup(TRIGER_PIN, GPIO.OUT)
ECHO_PIN = 31
GPIO.setup(ECHO_PIN, GPIO.IN)

  
DELAY = 0.5
OPEN_DOOR = 150
CLOSE_DOOR = 0

def nfcInitPrompt ():return "Ready to scan\nscanning ......"

def readNFC():
    card_id, card_text = nfc_card.read()
    return card_id, card_text

def nfcDetails():
    card_id, card_text = readNFC()
    print("card_id", card_id,"\ncard_text", card_text)
    
def authenticateNFC(card_id):
    for i in range(len(nfc_list)):
        for element in nfc_list[i]:
            if nfc_list[i][element] == card_id :
                #print("yes")
                return True
    return False
                

    
def doorState(angle):
    pwm.start(0)
    duty = angle / 18 + 3
    GPIO.output(SERVO_PIN, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    sleep(DELAY)
    GPIO.output(SERVO_PIN, GPIO.FALSE)   


def relayLock(state):
    if state == True: #"open"
        GPIO.output(RELAY_PIN, GPIO.HIGH) #1 or True  #This Turns Relay Off. Brings Voltage to Max GPIO can output ~3.3V
    else:
        GPIO.output(RELAY_PIN, GPIO.FALSE) #Turns Relay On. Brings Voltage to Min GPIO can output ~0V. 





def distanceToOpenDoor():
    try:
        GPIO.output(TRIGER_PIN, GPIO.LOW)

        print ("sensor settling....")
        time.sleep(1)

        GPIO.output(TRIGER_PIN, GPIO.HIGH)
        
        micro_seconds10 = 0.00001
        time.sleep(micro_seconds10)

        GPIO.output(TRIGER_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN)==0:
            pulse_start_time = time.time()
        while GPIO.input(ECHO_PIN)==1:
            pulse_end_time = time.time()
        
        print ("Calculating distance")
        
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        #print ("Distance: ",distance,"cm")
        return distance
    
    finally:
        GPIO.cleanup()
        



def main():
    LIMIT = 15  #50cm
    STAY_OPEN_FOR = 8
    while True:
        nfcInitPrompt()
        card_id, card_text = readNFC()
        status = authenticateNFC(card_id)
        if status == True:
            # camera
            relayLock(status) #unlock
            buzz("green")
            doorState(OPEN_DOOR)
            sleep(STAY_OPEN_FOR)
            #close the door
            doorState(CLOSE_DOOR)
            sleep(STAY_OPEN_FOR)
            relayLock(False)
        else:
            continue
        
        



try:
    main() #process
    #pass
except KeyboardInterrupt:
    print("ended")
finally:
    GPIO.cleanup()
