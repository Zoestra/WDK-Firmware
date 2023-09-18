import board
import json 
import digitalio as dio

rp2040 = {
    '__class__': board.__class__,
    '__name__': board.__name__,
    'A0': board.A0,
    'A1': board.A1,
    'A2': board.A2,
    'A3': board.A3,
    'GP0': board.GP0,
    'GP1': board.GP1,
    'GP10': board.GP10,
    'GP11': board.GP11,
    'GP12': board.GP12,
    'GP13': board.GP13,
    'GP14': board.GP14,
    'GP15': board.GP15,
    'GP16': board.GP16,
    'GP17': board.GP17,
    'GP18': board.GP18,
    'GP19': board.GP19,
    'GP2': board.GP2,
    'GP20': board.GP20,
    'GP21': board.GP21,
    'GP22': board.GP22,
    'GP23': board.GP23,
    'GP24': board.GP24,
    'GP25': board.GP25,
    'GP26': board.GP26,
    'GP26_A0': board.GP26_A0,
    'GP27': board.GP27,
    'GP27_A1': board.GP27_A1,
    'GP28': board.GP28,
    'GP28_A2': board.GP28_A2,
    'GP3': board.GP3,
    'GP4': board.GP4,
    'GP5': board.GP5,
    'GP6': board.GP6,
    'GP7': board.GP7,
    'GP8': board.GP8,
    'GP9': board.GP9,
    'LED': board.LED,
    'SMPS_MODE': board.SMPS_MODE,
    'STEMMA_I2C': board.STEMMA_I2C,
    'VBUS_SENSE': board.VBUS_SENSE,
    'VOLTAGE_MONITOR': board.VOLTAGE_MONITOR,
}

def pins_init():
    #Get Configuration from TOML
    with open('keyboard.json') as file:
        config = json.load(file)
        print(config)
        #Mux 
        dio.DigitalInOut(rp2040[config['mux']['com']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['mux']['s_0']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['mux']['s_1']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['mux']['s_2']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['mux']['s_3']]).direction = dio.Direction.OUTPUT

        #Rows
        dio.DigitalInOut(rp2040[config['rows']['row_1']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['rows']['row_2']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['rows']['row_3']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['rows']['row_4']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['rows']['row_5']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['rows']['row_6']]).direction = dio.Direction.OUTPUT
        dio.DigitalInOut(rp2040[config['rows']['row_7']]).direction = dio.Direction.OUTPUT

        #Rotary Encoders 
        dio.DigitalInOut(rp2040[config['encoder_0']['pin_A']]).direction = dio.Direction.INPUT
        dio.DigitalInOut(rp2040[config['encoder_0']['pin_B']]).direction = dio.Direction.INPUT

        dio.DigitalInOut(rp2040[config['encoder_1']['pin_A']]).direction = dio.Direction.INPUT
        dio.DigitalInOut(rp2040[config['encoder_1']['pin_B']]).direction = dio.Direction.INPUT

        dio.DigitalInOut(rp2040[config['encoder_2']['pin_A']]).direction = dio.Direction.INPUT
        dio.DigitalInOut(rp2040[config['encoder_2']['pin_B']]).direction = dio.Direction.INPUT
pins_init()