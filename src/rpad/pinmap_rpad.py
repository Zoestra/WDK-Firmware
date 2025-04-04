from machine import Pin

# Pin map for Rotomaxetron
# @author Zoestra

######### Rows #########

# Rows are write only
row1 = Pin(0, Pin.OUT, Pin.PULL_UP)
row2 = Pin(1, Pin.OUT, Pin.PULL_UP)
row3 = Pin(2, Pin.OUT, Pin.PULL_UP)
row4 = Pin(3, Pin.OUT, Pin.PULL_UP)
row5 = Pin(4, Pin.OUT, Pin.PULL_UP)

######### Columns #########

# Columns are read-only
col1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
col2 = Pin(6, Pin.IN, Pin.PULL_DOWN)
col3 = Pin(7, Pin.IN, Pin.PULL_DOWN)
col4 = Pin(13, Pin.IN, Pin.PULL_DOWN)
col5 = Pin(14, Pin.IN, Pin.PULL_DOWN)


######### NeoPixel #########

led_out = Pin(22, Pin.OUT, Pin.PULL_DOWN)

######### Encoders #########

# RGB Encoder
enc_sw = Pin(21, Pin.IN, Pin.PULL_DOWN)
enc_a = Pin(24, Pin.IN, Pin.PULL_DOWN)
enc_b = Pin(17, Pin.IN, Pin.PULL_DOWN)
enc_led_r = Pin(27, Pin.IN, Pin.PULL_DOWN)  ## dobule check pulldown
enc_led_g = Pin(26, Pin.IN, Pin.PULL_DOWN)
enc_led_b = Pin(25, Pin.IN, Pin.PULL_DOWN)
