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

# Function to move forward the number of steps passed
def ForStep(stepper,numberSteps):
	for i in range (0,numberSteps):
		stepper.oneStep(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
	

def BackStep(stepper,numberSteps):
	for i in range (0,numberSteps):
		stepper.oneStep(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
	turnOffMotors()

def ChooseSteps(stepper):
	AmtSteps = input('How many steps?')
	WhcWay =raw_input('press f for forwards b for backwards')
	if WhcWay =="f":
		print ('Moving forward %s steps')% AmtSteps
		ForStep(stepper,AmtSteps)
	else:
		
		print ('Moving backwars %s steps')% AmtSteps
		BackStep(stepper, AmtSteps)	


def TimeLapse(stepper):
	ActTime = input('How Long will this take? Enter in minutes Eg. 2 hours = 120')
	DelayPic = input('How Long inbetween Shots? enter in seconds Eg. 10 min = 600 ')
	AmtSteps = input('How many steps')
	NumberPics = (ActTime * 60)/ DelayPic
	print ('This will take  minutes and create %s shots') % NumberPics
	for i in range (0,NumberPics):
		ForStep(stepper,AmtSteps)
		time.sleep(1)
		print ('Take pic!')
		turnOffMotors()
		time.sleep((DelayPic)-1)




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



while True:
	ChooseSteps(CamMotor)
	turnOffMotors()
#TimeLapse(CamMotor)
