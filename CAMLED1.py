from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor
from Adafruit_LED_Backpack import AlphaNum4
import time
import atexit
import threading
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()
display = AlphaNum4.AlphaNum4()
# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
      mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
      mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
      mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
      mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
      print('Shutting off motors')

atexit.register(turnOffMotors)

def stepper_worker(stepper, numsteps, direction, style):
	stepper.step(numsteps, direction, style)


st1 = threading.Thread()
st2 = threading.Thread()


CamMotor = mh.getStepper(200, 2)  # 200 steps/rev, motor port #1
CamMotor.setSpeed(60)             # 30 RPM
display.begin()
Str1 = ("   FORWARDS   ")
Str2 = ("   BACKWARDS   ")
pos = 0

#st1 = threading.Thread(target=stepper_worker, args=(CamMotor, 200, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP))

for i in range (0,5):
		st1 = threading.Thread(target=stepper_worker, args=(CamMotor, 75, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP))   		
		st1.start()
		print ("Forward")
    #Loop for scrolling through title 	
    		while st1.isAlive():
    # Print a 4 character string to the display buffer.
        		display.print_str(Str1[pos:pos+4])
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
        		display.write_display()
    # Increment position. Wrap back to 0 when the end is reached.
        		pos += 1
     			if pos > len(Str1)-4:
				pos = 0
		
    # Delay for 0.15 of a second. This can be changed to speed up or slow down the scroll.
      			time.sleep(0.15)
    	
    		print ("Release")
    		mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    
    		time.sleep(2)
    		print ("Backward")
    		st2 = threading.Thread(target=stepper_worker, args=(CamMotor, 250, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE))
		st2.start()
    #Loop for scrolling through title 	
    		while st2.isAlive():
    # Print a 4 character string to the display buffer.
        		display.print_str(Str2[pos:pos+4])
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
        		display.write_display()
    # Increment position. Wrap back to 0 when the end is reached.
        		pos += 1
     			if pos > len(Str2)-4:
				pos = 0
		
    # Delay for 0.15 of a second. This can be changed to speed up or slow down the scroll.
      			time.sleep(0.15)   
    		mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    		print ("Release")


