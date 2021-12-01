from gpiozero import Button    # imports the required libraries
from gpiozero import LED
from time import sleep

led = LED(17)    # sets the var "led" to the gpio pin 17 on the pi
button = Button(27)    # sets the var "button" to the gpio pin 27 on the pi

while True:    # a infinate loop
    if button.wait_for_press():    # if the button is pressed the indented code will run
        led.on()    # turns the led on
    led.off()    # turns off the led once the button is not being pressed


