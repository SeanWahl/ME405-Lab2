"""!@file motor_driver.py
@brief
@details
@author
@author
@author
@date
"""

import time, pyb

class MotorDriver:
    """!@brief"""
    
    def __init__(self, enPin, pin1, pin2, timer):
        """!
        self.pin1 = pyb.Pin(pin1, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(pin2, pyb.Pin.OUT_PP)
        self.enPin = pyb.Pin(enPin, pyb.Pin.OUT_PP)
        self.timer = pyb.Timer(timer, freq = 20000)
        self.ch1 = self.timer.channel(1, pyb.Timer.PWM, pin=self.pin1)
        self.ch2 = self.timer.channel(2, pyb.Timer.PWM, pin=self.pin2)
        self.ch1.pulse_width_percent(0)
        self.ch2.pulse_width_percent(0)
        self.enPin.high()
        
    def set_duty_cycle(self, percent):
        if percent > 100:
            percent = 100
        elif percent < -100:
            percent = -100
        
        if percent > 0:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(percent)
            
        else:
            self.ch2.pulse_width_percent(0)
            self.ch1.pulse_width_percent(-percent)
            
    def disable(self):
        self.enPin.low()
                
        
        
if __name__ == "__main__":
    my_motor = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    motor_percents = [0, 25, 50, 75, 100, 50, 0, -25, -50, -75, -100, -50, 0]
    for percent in motor_percents:
        my_motor.set_duty_cycle(percent)
        time.sleep(1)