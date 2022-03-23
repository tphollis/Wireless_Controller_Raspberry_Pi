"""
Programmer: Preston Hollis
Date: 3/16/2022

Discription: "Class"
    - This file contains a class for mottors run on
      a motor controller with a raspberry pi.
      
Updates:
    - date, programmer_name
     > discription_of_changes
"""

#Libraries
from evdev import InputDevice, categorize, ecodes # access to PS5 controller

class Controller():
    def __init__(self):
        self.gamepad = InputDevice('/dev/input/event2')
        self.buttons = {
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
        
        self.absolutes = {
            0: 'joystick_left_x',           # 0 = left, 255 = right
            1: 'joystick_left_y',           # 0 = up, 255 = down
            2: 'joystick_right_x',          # 0 = left, 255 = right
            3: 'L2_analog',                 # 0 = no press, 255 = full press
            4: 'R2_analog',                 # 0 = no press, 255 = full press
            5: 'joustick_right_y',          # 0 = up, 255 = down
            16: 'dpad_left/right',          # -1 = left, 0 = nothing, 1 = right
            17: 'dpad_up/down'              # -1 = up, 0 = nothing, 1 = down
            }
        
        self.center = 128                        # Joystick center positoin for x and y axis
        self.drift = 6                           # Amount of padding around center to prevent drift