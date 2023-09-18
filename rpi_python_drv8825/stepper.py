from periphery import GPIO
from time import sleep

MotorDir = [
    'forward',
    'backward',
]

ControlMode = [
    'hardward',
    'softward',
]

class StepperMotor:
    def __init__(self, dir_pin, step_pin, enable_pin, mode_pin0, mode_pin1, mode_pin2):  
        self.enable_pin = GPIO(enable_pin[0], enable_pin[1], "out")
        self.step_pin   = GPIO(step_pin[0],   step_pin[1],   "out")
        self.dir_pin    = GPIO(dir_pin[0],    dir_pin[1],    "out")
        self.mode_pin0  = GPIO(mode_pin0[0],  mode_pin0[1],  "out")
        self.mode_pin1  = GPIO(mode_pin1[0],  mode_pin1[1],  "out")
        self.mode_pin2  = GPIO(mode_pin2[0],  mode_pin2[1],  "out")

    def __digital_write(self, pin: GPIO, level: int):
        _level = level > 0
        pin.write(_level)

    def Stop(self):
        self.__digital_write(self.enable_pin, False)
        
    def SetMicroStep(self, mode, stepFormat):
        microstep = {'fullstep': (0, 0, 0),
                     'halfstep': (1, 0, 0),
                     '1/4step': (0, 1, 0),
                     '1/8step': (1, 1, 0),
                     '1/16step': (0, 0, 1),
                     '1/32step': (1, 0, 1)}
        
        if(mode == ControlMode[1]):
            cfg = microstep[stepFormat]
            self.__digital_write(self.mode_pin0, cfg[0])
            self.__digital_write(self.mode_pin1, cfg[1])
            self.__digital_write(self.mode_pin2, cfg[2])
    
    def TurnStep(self, direction, steps, stepDelay=0.005):
        if(direction == MotorDir[0]):
            self.__digital_write(self.enable_pin, True)
            self.__digital_write(self.dir_pin, False)
        elif(direction != MotorDir[0] and direction in MotorDir):
            self.__digital_write(self.enable_pin, True)
            self.__digital_write(self.dir_pin, True)
        else:
            print("Direction must be 'forward' or 'backward'")
            self.__digital_write(self.enable_pin, False)

        if(steps <= 0):
            return
        
        for i in range(steps):
            self.__digital_write(self.step_pin, True)
            sleep(stepDelay)
            self.__digital_write(self.step_pin, False)
            sleep(stepDelay)
