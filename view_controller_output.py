"""
Programmer: Preston Hollis
Date: 3/31/2022

Discription:
    - This Program will display the raw code your 
      controller is outputting. This is so you can
      figure out the maping of your controller. much 
      like the BUTTONS and ANALOGS strings found in 
      PS5_motor_controller.py.
      
Updates:
    - date, programmer_name
     > discription_of_changes
"""

#Libraries
from evdev import InputDevice, categorize, ecodes # access to PS5 controller

#Global Variables
GAMEPAD = InputDevice('/dev/input/event4')   # Location of controller inputs ("cd /dev/input" then "ls -al")

def main():
    for event in GAMEPAD.read_loop():
        print(event)


if __name__ == "__main__":
    main()