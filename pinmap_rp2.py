from machine import Pin

# Pin map for Rotomaxetron
# @author Zoestra

######### Rows #########

row1 = Pin(0, Pin.OUT, Pin.PULL_DOWN)
row2 = Pin(1, Pin.OUT, Pin.PULL_DOWN)
row3 = Pin(2, Pin.OUT, Pin.PULL_DOWN)
row4 = Pin(3, Pin.OUT, Pin.PULL_DOWN)
row5 = Pin(4, Pin.OUT, Pin.PULL_DOWN)
row6 = Pin(5, Pin.OUT, Pin.PULL_DOWN)
row7 = Pin(6, Pin.OUT, Pin.PULL_DOWN)

######### NeoPixel #########

led_out = Pin(7, Pin.OUT, Pin.PULL_DOWN)

######### Encoders #########

r1a = Pin(28, Pin.IN, Pin.PULL_DOWN)
r1b = Pin(27, Pin.IN, Pin.PULL_DOWN)

r2a = Pin(26, Pin.IN, Pin.PULL_DOWN)
r2b = Pin(17, Pin.IN, Pin.PULL_DOWN)

r3a = Pin(19, Pin.IN, Pin.PULL_DOWN)
r3b = Pin(20, Pin.IN, Pin.PULL_DOWN)

######### Communication #########

rx = Pin(17, Pin.IN, Pin.PULL_DOWN)
tx = Pin(16, Pin.IN, Pin.PULL_DOWN)
