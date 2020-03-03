#!/usr/bin/python
import os, sys
import ctypes
from movement import *
from effectors import *
from wait_for_light import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
sys.stdout = os.fdopen(sys.stdout.fileno(), "w",0)   
LIGHT_SENSOR = 5

KIPR.enable_servos()
    
#START POSITIION
hook_up()
    
wait_for_start(LIGHT_SENSOR)
"""
print("press A to start foo")
while KIPR.a_button() == 0:
	pass
print("Let's go.............")
KIPR.msleep(2000)
"""
#========================================================
#lower_reel()
#raise_reel_full()
#exit()
#line_follow_ticks(1000, 7000)
#KIPR.msleep(10000)


backward_to_black(1000)
backward(1000,300)
left(250,35)
KIPR.msleep(500)
hook_down()
right(750,600)#yank out cup


#Go deliver cup
forward_to_black(1000)
forward(1000,2000)
forward_to_black(1000)
     
right(500,300) #turn to cubes
forward(1000,3000)
left(750, 2200)
hook_up() #cup delivered

#go to ramp
        
forward_to_black(1000)
forward(1000,1000)
forward_to_black(1000)
forward(1000,2900)  #hit pipe at end of table
backward(1000,1000)
right(1000, 1100)
backward(800,3000)  #back up to pipe that runs along ramp
left(750, 950)
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
#forward(750,6900)
line_follow_ticks(1000,7000)
#Test lowering of claw
print("muehehehehehehehehehehehe I win")
lower_reel()
#close_claw()
raise_reel_full()
        
backward(750, 3000)
open_claw()

"""
#go for a second dip
forward(1000,3000)
lower_reel()
#close_claw()
raise_reel_full()
        
backward(750, 3000)
open_claw()
"""

