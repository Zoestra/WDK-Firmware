import re
from machine import Pin
import MatrixScanner as mx
from time import sleep
from time import sleep_us as speep


def _matrix_test():
    bluLED = Pin(2, Pin.OUT, Pin.PULL_DOWN)
    ylwLED = Pin(4, Pin.OUT, Pin.PULL_DOWN)
    grnLED = Pin(6, Pin.OUT, Pin.PULL_DOWN)
    redLED = Pin(8, Pin.OUT, Pin.PULL_DOWN)

    print("starting matrix test")
    bluLED.value(1)
    ylwLED.value(1)
    grnLED.value(1)
    redLED.value(1)

    sleep(2)

    bluLED.value(0)
    ylwLED.value(0)
    grnLED.value(0)
    redLED.value(0)

    while True:

        print("scanning...")
        inputs = mx.scan_matrix()
        print(inputs)
        print("~~~~~")

        keyValues = (
            inputs.count(11),
            inputs.count(12),
            inputs.count(21),
            inputs.count(22),
        )

        bluLED.value(keyValues[0])
        ylwLED.value(keyValues[1])
        grnLED.value(keyValues[2])
        redLED.value(keyValues[3])

        speep(1)


def main():
    while True:
        _matrix_test()


main()
