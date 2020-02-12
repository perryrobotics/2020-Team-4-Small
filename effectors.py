#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")



CLAW = 1
REEL = 2
HOOK = 0
    
REEL_TICKS = 5000
CLAW_TICKS = 9800
HOOK_UP = 1660
HOOK_DOWN = 250
    
def lower_reel():
	KIPR.cmpc(REEL)
	KIPR.mav(REEL, 500)
	while KIPR.gmpc(REEL) < REEL_TICKS:
		pass
	KIPR.ao()

                
            
def raise_reel():
	KIPR.cmpc(REEL)
	KIPR.mav(REEL, -200)
	while KIPR.gmpc(REEL) > -REEL_TICKS:
		pass
	KIPR.ao()

def open_claw():
	KIPR.cmpc(CLAW)
	KIPR.mav(CLAW, -1200)
	while KIPR.gmpc(CLAW) > -CLAW_TICKS:
		pass
	KIPR.ao()

def close_claw():
	KIPR.cmpc(CLAW)
	KIPR.mav(CLAW, 1200)
	while KIPR.gmpc(CLAW) < CLAW_TICKS:
		pass
	KIPR.ao()
            
def hook_up():
	KIPR.set_servo_position(HOOK, HOOK_UP)
	KIPR.msleep(750)
        
def hook_down():
	KIPR.set_servo_position(HOOK, HOOK_DOWN)
	KIPR.msleep(750)

def raise_reel_full():

	for pos in range(13):
		print (pos)
		KIPR.cmpc(REEL)
		KIPR.cmpc(CLAW)
		print(KIPR.gmpc(REEL), KIPR.gmpc(CLAW))
		KIPR.msleep(100)
            
		KIPR.mav(CLAW, 1200)
		while KIPR.gmpc(CLAW) < 445:
			pass
		KIPR.mav(CLAW,0)

		KIPR.mav(REEL, -200)
		while KIPR.gmpc(REEL) > -75:
			pass
		KIPR.mav(REEL,0)
   
	KIPR.cmpc(CLAW)
	KIPR.mav(CLAW, 1200)
	while KIPR.gmpc(CLAW) < (CLAW_TICKS-pos*445):
		pass
	KIPR.ao()
                
	KIPR.cmpc(REEL)
	KIPR.mav(REEL, -200)
	while KIPR.gmpc(REEL) > -(REEL_TICKS-(pos*75)):
		pass
	KIPR.mav(REEL, 0)
	



            
            
            
            
            
            