#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

LM = 3

RM = 0

LINE_SENSOR = 0

THRESH = 3000
#define forward
def forward(speed, ticks):
	KIPR.cmpc(LM)
 	KIPR.cmpc(RM)

  	KIPR.mav(LM, speed)
 	KIPR.mav(RM, speed)

  	while KIPR.gmpc(LM) < ticks:
		pass
	KIPR.ao()

#define backward
def backward(speed, ticks):
	KIPR.cmpc(LM)
   	KIPR.cmpc(RM)

  	KIPR.mav(LM, -speed)
  	KIPR.mav(RM, -speed)

  	while KIPR.gmpc(LM) > -ticks:		
		pass
	KIPR.ao()
            
#define left
def left(speed, ticks):
	KIPR.cmpc(LM)
   	KIPR.cmpc(RM)

  	KIPR.mav(LM, -speed)
  	KIPR.mav(RM, speed)

 	while KIPR.gmpc(RM) < ticks:
		pass
	KIPR.ao()

#define right
def right(speed, ticks):
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)

	KIPR.mav(LM, speed)
	KIPR.mav(RM, -speed)

	while KIPR.gmpc(LM) < ticks:
		pass
	KIPR.ao()

#what to do if it hits a bump while moving backwards
def back_to_bump(speed, port):
	KIPR.mav(LM, -speed)
	KIPR.mav(RM, -speed)

	while KIPR.digital(port) == 0:
		pass
	ao()

#what to do if it hits a bump while moving forwards
def forward_to_bump(speed, port):
	KIPR.mav(LM, speed)
	KIPR.mav(RM, speed)

	while KIPR.digital(port) == 0:
		pass
	KIPR.ao()

#line following
def forward_to_black(speed):
	KIPR.mav(LM, speed)
	KIPR.mav(RM, speed)
            
	while KIPR.analog(LINE_SENSOR) < THRESH:
		pass
	KIPR.ao()
            
def backward_to_black(speed):
	KIPR.mav(LM, -speed)
	KIPR.mav(RM, -speed)
            
	while KIPR.analog(LINE_SENSOR) < THRESH:
		pass
	KIPR.ao()

def line_follow_ticks(speed, ticks):
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)
        
	while KIPR.gmpc(LM) < ticks:
		reading = KIPR.analog(LINE_SENSOR)
		if reading < THRESH:
			KIPR.mav(LM, speed+300)
			KIPR.mav(RM, speed)
		elif reading > THRESH:
			KIPR.mav(LM, speed-300)
			KIPR.mav(RM, speed+300)
	ao()
        
        
        
        
        

            
