# GPIO_Controller_Raspberry_Pi
This repository contains python code you can use on your raspberry to control GPIO pins with a bluetooth controller. You will most likely need to make some small adjustments to the code for it to work so please be sure to read through through the instructions perfore attempting to run the program. This code is also directed twords those who have an intermediate knowledge of python. 
<br><br>
## Index
* [Requirements](#requirements)
* [Current controllers supported](#current-controllers-supported)
* [Programs and their uses](#programs-and-their-uses)
* [How to use your wireless controller with Raspberry Pi](#how-to-use-your-wireless-controller-with-raspberry-pi)
* [How to support a new controller](#how-to-support-a-new-controller)
<br>

## Requirements
* Raspberry Pi running raspband operating system
* python3 installed
* pip3 install evdev

## Current controllers supported
* Playstation 5 Duelsense<br><br>

## Programs and their uses
* <b>motor.py</b> - A class used to control any motor connectd to Raspberry Pi BPIO pins.
  * <ins><i>motor1 = Motor(EN, IN1, IN2)</i></ins> - Create a motor instance to use its functions. 'EN' is the GPIO number that allows variable speed. 'IN1' and 'IN2' are GPIO numbers that determine the rotation direction of the motor. 
  * <ins><i>motor1.clockwise(speed, motor)</i></ins> - This function tells motor1 to start moving clockwise at a given speed. 'speed' is a number anywhere from 0 to 100 to set motor speed. 'motor' is an optional string that helps identify which motor is being affected. for example, motor = "right drive".
  * <ins><i>motor1.counterclockwise(speed, motor)</i></ins> - The same as the clockwise() function but moves the motor counterclockwise. 
  * <ins><i>motor1.stop(motor)</i></ins> - This function stops the motor from running. It only requires the options input 'motor'.<br><br>
* <b>PS5_read_controller.py</b> - This code allows users to use their Playstation 5 Duelsense for python code inputs on their Raspberry Pi. It uses the Motor class as a way to show how to use this code.<br><br>
* <b>template_read_controller.py</b> - This code is the bare bone of all read_controller programs. It is to be coppied into a new python file then that new file edited to support a new controller type.<br><br>
* <b>view_controller_output.py</b> - This program allows you to view the raw output of your controller. Its intended use is to help map out your controller if it does not yet have supported code.<br><br>

## How to use your wireless controller with Raspberry Pi
Make sure the requirements are satisfied and the files in this repository are downloaded before continuing.

<b>1)</b> Open command prompt and change you directory to /dev/input.
```
$ cd /dev/input
```
View all the inputs currently on your raspberry pi. Keep track of all events listed.
```
$ ls -al
```
![This is an image](/images/events1.png)
<br><br>
<b>2)</b> Connect your wireless controller to the Raspberry Pi via bluetooth. When you have connected your controller, go back to command prompt and once again use the "la -al" command to get a list of events. There should be an event that wasn't there before. Remember this event.
![This is an image](/images/events2.png)

## How to support a new controller
