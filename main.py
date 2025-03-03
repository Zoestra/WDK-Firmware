from machine import Pin
from time import sleep
import MuxDriver

value = True

while True:

    MuxDriver.send_mux(5, 1)
    print("on")
    #
    value = not value
    sleep(2)

    MuxDriver.send_mux(5, 0)

    print("off")

    sleep(1)
