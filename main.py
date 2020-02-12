#!/usr/bin/python
import os, sys
import ctypes
from movement import *
from effectors import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

KIPR.enable_servos()
    
#START POSITIION
hook_up()
print("press A to start foo")
while KIPR.a_button() == 0:
	pass
print("Let's go.............")
KIPR.msleep(2000)

#========================================================
#lower_reel()
#raise_reel_full()
#exit()
line_follow_ticks(1000, 7000)
KIPR.msleep(10000)
        
backward_to_black(1000)
backward(750,400)
left(750,450)

hook_down()
right(750,900)#yank out cup

forward_to_black(1000)
forward(1000,2000)
forward_to_black(1000)
        
right(500,300) # turn to cubes
forward(1000,3000)
left(750, 2200)
hook_up()
        
forward_to_black(1000)
forward(1000,1000)
forward_to_black(1000)
forward(1000, 3500)  #hit pipe at end of table
backward(1000, 700)
right(1000, 1100)
backward(1000,2000)  #back up to pipe that runs along ramp
left(750, 900)
forward(750, 2000)

#backward(1000,9500)
KIPR.mav(LM,-1200)
KIPR.mav(RM, -1200)
while KIPR.digital(0)==0:
	pass
KIPR.ao()

#UP ON THE RAMP!!!

right(750,1000)
forward(750,500)
right(600,200)
forward(750,6750)

#Test lowering of claw

lower_reel()
#close_claw()
raise_reel_full()
        
backward(750, 3000)
open_claw()

