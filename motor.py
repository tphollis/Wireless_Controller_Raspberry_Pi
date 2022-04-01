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
import RPi.GPIO as GPIO # access to pins on Raspberry Pi


#GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor():

    '''...Initializer...'''
    def __init__(self, EN, IN1, IN2):
        
        #Preset variables
        self.EN = EN        #Allows speed control
        self.IN1 = IN1      #IN1 and IN2 determine direction
        self.IN2 = IN2      #   of motor direction.
        
        #GPIO setup
        GPIO.setup(self.EN, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        
        #Define pwm (Pulse Width Modulation)
        self.pwm = GPIO.PWM(self.EN, 100)
        self.pwm.start(0)

    '''...Translates analog stick values to values the motor can use...'''
    def translate_analog_stick(value, center):
        #Motors can only go up to a power of 100.
        #The analog sticks can vary from 0 - 255.
        #Do math that makes it so full throttle up/down/left/right equals 100.
        translation = int((value-center)*0.78)
    
        #Keep number positive
        if translation < 0:
            translation *= -1
    
        #Number can not be gratter than 100. Just a precausion.
        if translation > 100:
            translation = 100
    
        return translation


    '''...Move motor Clockwise...'''
    def clockwise(self, speed, motor = "..."):
        #'speed' is a number used to specify power put into motor.
        #'motor' is a string used to specify which motor is being used.(optional)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)

        #Print which motor is being affected.
        print("Moving {} motor clockwise at speed {}".format(motor, speed))


    '''...Move motor counterclockwise...'''
    def counterclockwise(self, speed, motor = "..."):
        #'speed' is a number used to specify power put into motor.
        #'motor' is a string used to specify which motor is being used.(optional)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)

        #Print which motor is being affected.
        print("Moving {} motor counterclockwise at speed {}".format(motor, speed))


    '''...Stop motor from running...'''
    def stop(self, motor = "..."):
        #'motor' is a string used to specify which motor is being used. (optional)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)

        #Print which motor is being affected.
        print("{} motor at stop".format(motor))