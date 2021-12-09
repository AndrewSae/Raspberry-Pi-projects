from gpiozero import Button, LED    # imports the required libraries
from time import sleep
import random

led = LED(27)    # sets the var "led" to the gpio pin 27 on the pi

player_1 = Button(17)    # sets "player_1" button to gpio 17
player_2 = Button(22)    # sets "player_2" button to gpio 22

time = random.uniform(5, 10)    # generates a random num in range 5-10 nand saves it in a var
sleep(time)    # stops the code for the amount of time that was made by the "time" var
led.on()    # turns on the LED

while True:    # a infinite loop
    if player_1.is_pressed:    # if player_1's button is pressed first the indented code will run
        print("Player 1 wins!")    # will print "Player 1 wins!"
        break    # excites the while loop
    if player_2.is_pressed:
        print("Player 2 wins!")
        break

led.off()    # turns off the LED