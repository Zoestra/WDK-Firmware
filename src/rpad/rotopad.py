import pinmap_rpad as p

def profile():

    rows = [p.row1, p.row2, p.row3, p.row4, p.row5] 
    cols = [p.col1, p.col2, p.col3, p.col4, p.col5]
    buttons    = [p.enc_sw]
    neopixels  = [p.led_out]
    encoders = [["rgb", p.enc_sw, [p.enc_led_r, p.enc_led_g, p.enc_led_b]] #[[enc1-identifier, button pin / [row, col], np addr / [r,g,b]], [enc2....]]

    return [rows, cols, buttons, neopixels, encoders]
