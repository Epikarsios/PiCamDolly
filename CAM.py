from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor

import time
import atexit
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)


atexit.register(turnOffMotors)

CamMotor = mh.getStepper(200, 2)  # 200 steps/rev, motor port #1
CamMotor.setSpeed(30)             # 30 RPM


while (True):
   

    print("Microsteps")
    print('Forward')
    CamMotor.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
    print ("Release")
    turnOffMotors()
    time.sleep(2)
    print ("Backward")
    CamMotor.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
    turnOffMotors()
    print ("Release")
