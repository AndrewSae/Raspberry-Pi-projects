# LED blink tutorial

## What you will need 
  - Raspberry pi (with a 40pin GPIO)
  - 2x male to female jumber wires or a GPIO expansion board
  - Any color LED 
  - 220Ω resistor 
  - Breadboard
  
## Software setup
  Get started by:
   - Updateing your pi
  ```bash
sudo apt update
```
 - Then install the gpiozero library  ![breadboard](https://user-images.githubusercontent.com/84029016/144133338-40bc1878-0f1d-40c9-b100-388023b21d91.png)

 ```bash
sudo apt install python3-gpiozero
```
  - Install the [main.py](link HERE) 
## Hardware setup
  Get started by making the circuit:
   - Note thet the long leg of the led it the postive and the short leg is the ground
   - The positive leg of the LED to GPIO 17(pin 11) with the 220Ω resistor 
   - 
   - Then the ground leg to the ground bus of the Breadboard 

 - It should look something like this 

![This is an image](link HERE)

  - Schematic
  ![This is an image](link HERE)
