# LED with button tutorial

## What you will need 
  - Raspberry pi (with a 40pin GPIO)
  - 3x male to female and 1x male to male jumper wires or a GPIO expansion board with 4x male to male jumper wires
  - Any color LED 
  - A 4 leg NC button
  - 220Ω resistor 
  - Breadboard
  
## Software setup
  Get started by:
   - Updating the pi
  ```bash
sudo apt update
```
- Now install the gpiozero library
 ```bash
sudo apt install python3-gpiozero
```
  - Save the [main.py](https://github.com/AndrewSae/Raspberry-Pi-projects/blob/main/LED%20with%20button/main.py) to the pi
## Hardware setup
  Get started by making the circuit:
   - Note that the long leg of the led is the positive and the short leg is the ground
   - The positive leg of the LED to goes GPIO 17(pin 11) with the 220Ω resistor 
   - Then the ground leg goes to the ground bus of the Breadboard 
   - The button should be placed on the breadboard in the center so that each leg has its own row 
   - Use one jumper wire to connect the ground bus to one side on the button legs
   - Then use one more wire and hook it up to the other side of the button to GPIO 27 (pin 13) (if you used the leg pin on one side you should use the right leg on the other side of the button) 

 - It should look something like this 

![This is an image](https://github.com/AndrewSae/Raspberry-Pi-projects/blob/main/LED%20with%20button/IMG/breadboard.png?raw=true)

  - Schematic
  
  ![schematic](https://github.com/AndrewSae/Raspberry-Pi-projects/blob/main/LED%20with%20button/IMG/schematic.png?raw=true)

## Run the code
- Open the code in your editor of choice 
- Press the run button
- Now when you press the button the led should turn on
