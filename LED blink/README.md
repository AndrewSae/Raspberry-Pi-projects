# LED blink tutorial

## What you will need 
  - Raspberry pi (with a 40pin GPIO)
  - 2x male to female jumper wires or a GPIO expansion board with 2x male to male jumper wires
  - Any color LED 
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
  - Save the [main.py](https://github.com/AndrewSae/Raspberry-Pi-projects/blob/main/LED%20blink/main.py) to the pi
## Hardware setup
  Get started by making the circuit:
   - Note that the long leg of the led is the positive and the short leg is the ground
   - The positive leg of the LED to goes GPIO 17(pin 11) with the 220Ω resistor 
   - Then the ground leg to the ground bus of the Breadboard 

 - It should look something like this 

![This is an image](https://github.com/AndrewSae/Raspberry-Pi-projects/blob/main/LED%20blink/IMG/breadboard.png?raw=true)![144140417-10fb5ef9-5c42-4202-babd-3441df9cd872](https://user-images.githubusercontent.com/84029016/144144140-b44f721c-2e9b-4812-ae64-de293fd85a9b.png)


  - Schematic
  
  ![schematic](https://user-images.githubusercontent.com/84029016/144140417-10fb5ef9-5c42-4202-babd-3441df9cd872.png)

## Run the code
- Open the code in your editor of choice 
- Press the run button
- Now you should see the LED blinking 
