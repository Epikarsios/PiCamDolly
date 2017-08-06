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

CamMotor = mh.getStepper(200, 2)  # 200 steps/rev, motor port #1
CamMotor.setSpeed(60)             # 30 RPM
display.begin()
F = ('Adafruit_MotorHAT.FORWARD')
Fwd = ("   FORWARDS   ")
Bwd = ("   BACKWARDS   ")

AmtSteps = input('How many Steps?')

def ForwardSteps(stepper, numberSteps,direction):
	for i in range(0, numberSteps):
		stepper.oneStep(direction,Adafruit_MotorHAT.MICROSTEP)
		print("this is step number %s") %  i 
	turnOffMotors()

def WriteLed(Message):	

	Message = "   " + Message + "   "    		
	pos = 0
    #Loop for scrolling through title 	
	for x in range(0,len(Message)-4):
           
		display.print_str(Message[pos:pos+4])
   	     	display.write_display()
  		pos += 1
     		if pos > len(Message)-4:
			pos = 0
		
    		time.sleep(0.15)  
	display.clear()
	display.write_display()

ForwardSteps(CamMotor, AmtSteps,F)
WriteLed(Fwd)
turnOffMotors()
