from stepper import StepperMotor
from time import sleep
import signal

first_enable_gpio     = ('/dev/gpiochip4', 0)
first_step_gpio       = ('/dev/gpiochip2', 22)
first_direction_gpio  = ('/dev/gpiochip5', 27)
first_mode_gpio0      = ('/dev/gpiochip5', 28)
first_mode_gpio1      = ('/dev/gpiochip5', 2)
first_mode_gpio2      = ('/dev/gpiochip2', 21)

second_enable_gpio     = ('/dev/gpiochip5', 23)
second_step_gpio       = ('/dev/gpiochip2', 23)
second_direction_gpio  = ('/dev/gpiochip3', 10)
second_mode_gpio0      = ('/dev/gpiochip2', 24)
second_mode_gpio1      = ('/dev/gpiochip3', 12)
second_mode_gpio2      = ('/dev/gpiochip5', 6)

flag = True
selected_motor = None

# create object
first_motor = StepperMotor(first_direction_gpio, first_step_gpio, first_enable_gpio, first_mode_gpio0, first_mode_gpio1, first_mode_gpio2)
second_motor = StepperMotor(second_direction_gpio, second_step_gpio, second_enable_gpio, second_mode_gpio0, second_mode_gpio1, second_mode_gpio2)


def handler(signum, frame):
    print("Terminating, stopping all motors", flush=True)
    first_motor.Stop()
    second_motor.Stop()
    exit(0)


def main():
    while (flag):
        motor_number = input("Choose a motor number [1-2]: ")
    
        if(motor_number == '1'):
            selected_motor = first_motor
        elif(motor_number == '2'):
            selected_motor = second_motor
        else:
            print("Wrong motor number choose between 1 or 2")
            selected_motor = None
    
        if(selected_motor):
            mode = 'hardward'
            step_format = 'fullstep'
    
            selected_motor.SetMicroStep(mode, step_format)
            direction = input("Chose a direction [forward/backward]: ")
            try:
                steps =int(input("Choose number of steps (200 = 360 dgrees) :"))
            except:
                continue
            
            selected_motor.TurnStep(direction, steps)
    
            selected_motor.Stop()

if(__name__ == "__main__"):
    signal.signal(signal.SIGINT, handler)
    main()