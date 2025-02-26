from machine import Pin

class RotaryEncoder:
    def __init__(self, clk_pin, dt_pin):
        self.clk = Pin(clk_pin, Pin.IN, Pin.PULL_UP)
        self.dt = Pin(dt_pin, Pin.IN, Pin.PULL_UP)
        self.counter = 0
        self.last_clk_state = self.clk.value()

        # Attach an interrupt to the CLK pin if it is rising or falling.
        self.clk.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._rotary_interrupt)

    def _rotary_interrupt(self, pin):
        """ Interrupt handler for the rotary encoder """
        clk_state = self.clk.value()
        dt_state = self.dt.value()

        if clk_state != self.last_clk_state:  # A state changed (I think this should always be true?)
            if dt_state != clk_state:
                self.counter += 1  # Clockwise
            else:
                self.counter -= 1  # Counterclockwise

        self.last_clk_state = clk_state  # Update state

    def get_value(self):
        """ Returns the current counter value """
        return self.counter
