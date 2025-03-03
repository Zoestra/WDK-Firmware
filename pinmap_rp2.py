from machine import Pin

from MuxDriver import read_mux

# Pin map for Rotomaxetron
# @author Zoestra

######### Rows #########

# Rows are write only
row1 = Pin(0, Pin.OUT, Pin.PULL_DOWN)
row2 = Pin(1, Pin.OUT, Pin.PULL_DOWN)
row3 = Pin(2, Pin.OUT, Pin.PULL_DOWN)
row4 = Pin(3, Pin.OUT, Pin.PULL_DOWN)
row5 = Pin(4, Pin.OUT, Pin.PULL_DOWN)
row6 = Pin(5, Pin.OUT, Pin.PULL_DOWN)
row7 = Pin(6, Pin.OUT, Pin.PULL_DOWN)

######### Columns #########

# Columns are read-only
col1 = read_mux(0)
col2 = read_mux(1)
col3 = read_mux(2)
col4 = read_mux(3)
col5 = read_mux(4)
col6 = read_mux(5)
col7 = read_mux(6)
col8 = read_mux(7)
col9 = read_mux(8)

######### NeoPixel #########

led_out = Pin(7, Pin.OUT, Pin.PULL_DOWN)

######### Encoders #########

# thumb cluster encoder
r1a = Pin(28, Pin.IN, Pin.PULL_DOWN)
r1b = Pin(27, Pin.IN, Pin.PULL_DOWN)

# top inner encoder
r2a = Pin(26, Pin.IN, Pin.PULL_DOWN)
r2b = Pin(17, Pin.IN, Pin.PULL_DOWN)

# top outer encoder
r3a = Pin(19, Pin.IN, Pin.PULL_DOWN)
r3b = Pin(20, Pin.IN, Pin.PULL_DOWN)

######### Communication #########

rx = Pin(17, Pin.IN, Pin.PULL_DOWN)
tx = Pin(16, Pin.IN, Pin.PULL_DOWN)
