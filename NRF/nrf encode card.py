# ENCODE ON TO THE CARD, (WRITE) CARD ID AND TEXT CONTENT ON RFID-RC522
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

nfr_encode_card = SimpleMFRC522()
print("scan card on NRF...Tto encode id and text content")
try:
    card_text = input("Enter student id as card text identification")
    nfr_encode_card.write(card_text)
    print("card_text", card_text, "card encoded")
finally:
    GPIO.cleanup()
