from machine import Pin

mux_sig_0 = Pin(21, Pin.OUT, Pin.PULL_DOWN)
mux_sig_1 = Pin(20, Pin.OUT, Pin.PULL_DOWN)
mux_sig_2 = Pin(19, Pin.OUT, Pin.PULL_DOWN)
mux_sig_3 = Pin(18, Pin.OUT, Pin.PULL_DOWN)

mux_com = Pin(22, Pin.OUT, Pin.PULL_DOWN)


def read_mux(target: int):

    mux_sig_0.value(target & 1)
    mux_sig_1.value((target & 2) >> 1)
    mux_sig_2.value((target & 4) >> 2)
    mux_sig_3.value((target & 8) >> 3)

    return mux_com.value


def send_mux(target: int, value: bool):

    mux_sig_0.value(target & 1)
    mux_sig_1.value((target & 2) >> 1)
    mux_sig_2.value((target & 4) >> 2)
    mux_sig_3.value((target & 8) >> 3)

    mux_com.value(value)
