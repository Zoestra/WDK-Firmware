from machine import Pin
from time import sleep_us

mux_sig_0 = Pin(21, Pin.OUT, Pin.PULL_DOWN)
mux_sig_1 = Pin(20, Pin.OUT, Pin.PULL_DOWN)
mux_sig_2 = Pin(19, Pin.OUT, Pin.PULL_DOWN)
mux_sig_3 = Pin(18, Pin.OUT, Pin.PULL_DOWN)

mux_com = Pin(22, Pin.OUT, Pin.PULL_DOWN)


def read_mux(target: int):

    mux_com.init(mode=Pin.IN)

    mux_sig_0.value(target & 1)
    mux_sig_1.value((target & 2) >> 1)
    mux_sig_2.value((target & 4) >> 2)
    mux_sig_3.value((target & 8) >> 3)

    sleep_us(1)

    return mux_com.value


def send_mux(target: int, value):

    ### send_mux is not used on the rotomaxetron ###
    ### it is included only for testing purposes ###

    mux_com.init(mode=Pin.OUT)

    mux_sig_0.value(target & 1)
    mux_sig_1.value((target & 2) >> 1)
    mux_sig_2.value((target & 4) >> 2)
    mux_sig_3.value((target & 8) >> 3)

    sleep_us(1)

    mux_com.value(value)
