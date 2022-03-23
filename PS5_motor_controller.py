"""
Programmer: Preston Hollis
Date: 3/16/2022

Discription:
    - This Program utilizes a motor controller and a
      PS5 controller. It will allow the user to control
      motors with the PS5 controller via blurtooth.
      
Updates:
    - date, programmer_name
     > discription_of_changes
"""

#Libraries
import motor #class that utilizes motor control
from evdev import InputDevice, categorize, ecodes # access to PS5 controller


#Global Variables
GAMEPAD = InputDevice('/dev/input/event2')   # Location of controller inputs
CENTER = 128                                 # Joystick center positoin for x and y axis
DRIFT = 6                                    # Amount of padding around center to prevent drift

BUTTONS = {
    # 0 = not pressed, 1 = pressed
    304:'square',
    305:'x',
    306:'circle',
    307:'square',
    308:'L1',
    309:'R1',
    310:'L2',
    311:'R2',
    312:'share',
    313:'menu',
    314:'L3',
    315:'R3',
    316:'PS',
    317:'touchpad'
    }

ANALOGS = {
    0: 'joystick_left_x',           # 0 = left, 255 = right 
    1: 'joystick_left_y',           # 0 = up, 255 = down
    2: 'joystick_right_x',          # 0 = left, 255 = right
    3: 'L2_analog',                 # 0 = no press, 255 = full press
    4: 'R2_analog',                 # 0 = no press, 255 = full press
    5: 'joystick_right_y',          # 0 = up, 255 = down
    16: 'dpad_left/right',          # -1 = left, 0 = nothing, 1 = right
    17: 'dpad_up/down'              # -1 = up, 0 = nothing, 1 = down
    }


#Translates analog stick values to values the motor can use
def translate_analog_stick(value):
    translation = int((value-CENTER)*0.78)
    
    #Keep number positive
    if translation < 0:
        translation *= -1
    
    #Number can not be gratter than 100
    if translation > 100:
        translation = 100
    
    return translation


#Runs the infinate loop activating code based on changes.
def main():
    #Create instances of motors
    #pin:GPIO - 3:2, 5:3, 7:4, 8:14, 10:15, 11:17, 12:18, 13:27, 15:22, 16:23
    #           18:24, 19:10, 21:9, 22:25, 23:11, 24:8, 26:7, 29:5, 31:6, 32:12
    #           33:13, 35:19, 36:16, 37:26, 38:20, 40:21
    leftDrive = motor.Motor(21, 20, 26)
    rightDrive = motor.Motor(16, 19, 13)
    
    #Get every event that happens on the controller
    for event in GAMEPAD.read_loop():
        
        #Code if the event is a button type
        if event.type == ecodes.EV_KEY and event.code in BUTTONS:
            if BUTTONS[event.code] == "circle" and event.value == 1:
                quit()
        
        
        #Code if the event is an absolute type
        if event.type == ecodes.EV_ABS and event.code in ANALOGS:
            
            #If left analog stick is up, move left motors forword. 
            if ANALOGS[event.code] == "joystick_left_y":
                if event.value > CENTER+DRIFT:
                    leftDrive.backword(translate_analog_stick(event.value), "left")
                elif event.value < CENTER-DRIFT:
                    leftDrive.forword(translate_analog_stick(event.value), "left")
                else:
                    leftDrive.stop("left")
                    
            #If left analog stick is up, move left motors forword. 
            if ANALOGS[event.code] == "joystick_right_y":
                if event.value > CENTER+DRIFT:
                    rightDrive.backword(translate_analog_stick(event.value), "right")
                elif event.value < CENTER-DRIFT:
                    rightDrive.forword(translate_analog_stick(event.value), "right")
                else:
                    rightDrive.stop("right")


if __name__ == "__main__":
    main()