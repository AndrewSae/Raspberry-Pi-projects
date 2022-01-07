# reaction game
## What you will need 
  - Raspberry pi (with a 40pin GPIO)
  - 3x male to female and 3x male to male jumper wires or a GPIO expansion board with 7x male to male jumper wires
  - Any color LED 
  - 2x 4 leg NC button
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
  - Save the [main.py](https://github.com/AndrewSae/Raspberry-Pi-projects/blob/main/Reaction%20Game/main.py) to the pi
## Hardware setup
  Get started by making the circuit:
   - Note that the long leg of the led is the positive and the short leg is the ground
   - The positive leg of the LED to goes GPIO 27(pin 13) with the 220Ω resistor 
   - Then the ground leg goes to the ground bus
   - The button should be placed on the breadboard in the center so that each leg has its own row (do this for both buttons)
   - Use one jumper wire to connect the ground bus to one side on the button legs (do for both button)
   - use a  wire and hook it up to the other side of the button to GPIO 17 (pin 11) 
   - use one more wire to connect the other button to GPIO 22 (pin 15)
   - make sure that the ground and the GPIO wires are not across from each other because then they will always be completing the circuit 
   ![This is an image](https://makeabilitylab.github.io/physcomp/arduino/assets/images/FourLeggedTactileButtons_Overview.png)

 - It should look something like this 

![This is an image](https://github.com/AndrewSae/Raspberry-Pi-projects/blob/main/Reaction%20Game/IMG/breadboard.png?raw=true)

  - Schematic
  
  ![schematic](https://github.com/AndrewSae/Raspberry-Pi-projects/blob/main/Reaction%20Game/IMG/schematic.png?raw=true)

## Run the code
- Open the code in your editor of choice 
- Press the run button
- then the l3ed will randomly turn on and the first press the button when the led turns on wins
