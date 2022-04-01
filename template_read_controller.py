"""
Programmer: Preston Hollis
Date: 3/16/2022

Discription:
    - This code is the bare bone of all read_controller programs. It is to act as a template for any
      new controller you wish to support. If you chose to do this, copy this code to a new file and 
      name it read_controller.py with the controller type at the beginning. Example "xboxOne_read_controller.py".
      From there you can edit the code all you want. 

      If you are able to get your controller working, please consider sharing that code so that others may
      utilize it. Thanks!
      
Updates:
    - date, programmer_name
     > discription_of_changes
"""

#Libraries
from evdev import InputDevice, categorize, ecodes # access to PS5 controller


#Global Variables
GAMEPAD = InputDevice('/dev/input/event0')   # Location of controller inputs ("cd /dev/input" then "ls -al")
CENTER = 0                                   # Joystick center positoin for x and y axis
DRIFT = 0                                    # Amount of padding around center to prevent drift


#Fill in these lists. See supported read_controller.py files for examples.
BUTTONS = {
    # values:
    # 0 = not pressed, 1 = pressed
    
    }

ANALOGS = {                         # values:
    
    }


'''...Runs the infinate loop activating code based on changes...'''
def main():
    
    #Get every event that happens on the controller. (Infinate loop)
    for event in GAMEPAD.read_loop():
        # event.code gives you the number representing the controllers buttons/joysticks/triggers.
        # event.value gives you the value of what is used on the controller.
        # event.type tells you if buttons or analogs are being used. (Least likely to use)
        
        #Code for button types go here inside this IF statement.
        if event.type == ecodes.EV_KEY and event.code in BUTTONS:
            print(BUTTONS[event.code])

        
        
        #Code for analog types go there inside this IF statement
        if event.type == ecodes.EV_ABS and event.code in ANALOGS:
            print(ANALOGS[event.code])


#Initiate the program with main().
if __name__ == "__main__":
    main()
