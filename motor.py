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
    def __init__(self, EN, IN1, IN2):
        
        #Preset variables
        self.EN = EN
        self.IN1 = IN1
        self.IN2 = IN2
        
        #GPIO setup
        GPIO.setup(self.EN, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        
        #Define pwm (Pulse Width Modulation)
        self.pwm = GPIO.PWM(self.EN, 100)
        self.pwm.start(0)
        
    def forword(self, speed, side):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
        print("Moving {} side forword at speed {}".format(side, speed))
        
    def backword(self, speed, side):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)
        print("Moving {} side back at speed {}".format(side, speed))
        
    def stop(self, side):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
        print("{} side at stop".format(side))