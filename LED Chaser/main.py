from gpiozero import LED    # imports the required libraries
from time import sleep

led = [
    LED(17),
    LED(27),
    LED(22),
    LED(10),
    led(9),
    led(11),
    LED(5)
    ]    # makes a array called "led" that stores the led GPIO pin numbers

x = 0    # makes a var "x" and sets it to 0

while True:    # a infinite loop
    while x <= len(led):    # if "x" is less or equal to the length of the array "led" the indented code will rin
        led[x].on()    # turns on the led that is at the posios of "x" in the array
        sleep(.5)    # pauses the code for ".5" seconds
        led[x].off()    # turns off the led that is at the position of "x" in the array
        x += 1    # adds 1 to "x"
        if x == len(led):    # if "x" is equal to the length of the "led" array the indented code will be run
            x=0    # sets "x" to 0
    