#READ CARD CONTENT ON RFID-RC522
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522



#nfc_card = SimpleMFRC522()
#print("scanning ......\n press Ctrl + c to quit the program")
#try:
#    card_id, card_text = nfc_card.read()
#    print("card_id", card_id,"\ncard_text", card_text)
#finally:
#    GPIO.cleanup()
    
    
def readNFC():
    import RPi.GPIO as GPIO
    from mfrc522 import SimpleMFRC522
    nfc_card = SimpleMFRC522()
    print("scanning ......\n press Ctrl + c to quit the program")
    try:
        card_id, card_text = nfc_card.read()
        #print("card_id", card_id,"\ncard_text", card_text)
    finally:
        GPIO.cleanup()
    return card_id

if __name__ == "__main__":
    print(readNFC())