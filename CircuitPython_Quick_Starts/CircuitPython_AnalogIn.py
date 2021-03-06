# CircuitPython AnalogIn Demo

import time
from analogio import AnalogIn
import board

analog1in = AnalogIn(board.A1)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    print("A1: %f" % (get_voltage(analog1in)))
    time.sleep(0.1)
