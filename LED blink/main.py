from gpiozero import LED # imports the required libraries
from time import sleep

led = LED(17)    # sets the var "led" to the gpio pin 17 on the pi

while True:    # a infinate loop
    led.on()    # turns on the led
    sleep(1)    # pauses the code for set time
    led.off()    # turns off the led
