"""!@file encoder_reader.py
@brief
@details
@author
@author
@author
@date
"""

import time

class encoder:
    """@brief"""
    
    def __init__(self, pin1, pin2, timer):
        self.pin1 = pyb.Pin(pin1, pyb.Pin.IN)
        self.pin2 = pyb.Pin(pin2, pyb.Pin.IN)
        self.timer = pyb.Timer (timer, period = 0xFFFF, prescaler = 0)
        self.ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin=self.pin1)
        self.ch2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin=self.pin2)
        self.count = 0
        self.prev = 0
        
    def read_encoder(self):
        self.current = self.timer.counter()
        self.delta = self.current-self.prev
        if abs(self.delta) > 0xFFFF/2:
            if self.delta > 0:
                self.count += self.delta - 0xFFFF
            else:
                self.count += self.delta + 0xFFFF
        else:
            self.count += self.delta
            
        self.prev = self.current
        return self.count
        
    def zero(self):
        self.count = 0
        
if __name__ == "__main__":
    my_encoder = encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    while True:
        for n in range(10):
            print(my_encoder.read_encoder())
            if n == 9:
                my_encoder.zero()
            time.sleep(0.5)