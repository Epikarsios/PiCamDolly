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
FWD = ("Adafruit_MotorHAT.FORWARD")
BWD = ("Adafruit_MotorHAT.BACKWARD")
Fwd = ("   FORWARDS   ")
Bwd = ("   BACKWARDS   ")



def ChooseSteps(stepper):
	AmtSteps = input('How many steps?')
	WhcWay =raw_input('press f for forwards b for backwards')
	if WhcWay =="f":
		direction = FWD
		WriteLed(Fwd)
		for i in range(0,AmtSteps):
			stepper.oneStep(Adafruit_MotorHAT.FORWARD,Adafruit_MotorHAT.MICROSTEP)
#			stepper.oneStep(direction, Adafruit_MotorHAT.MICROSTEP)
		turnOffMotors()
	else:
		direction = BWD
		WriteLed(Bwd)
		print (direction)
		WriteLed(str(AmtSteps))
		for i in range(0, AmtSteps):
			stepper.oneStep(Adafruit_MotorHAT.BACKWARD,Adafruit_MotorHAT.MICROSTEP)
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

ChooseSteps(CamMotor)
turnOffMotors()
