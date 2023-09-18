import board


def pins_rp2040(input_string):
    match input_string:
        case '__class__':
            return board.__class__
        case '__name__':
            return board.__name__
        case 'A0':
            return board.A0
        case 'A1':
            return board.A1
        case 'A2':
            return board.A2
        case 'A3':
            return board.A3
        case 'GP0':
            return board.GP0
        case 'GP1':
            return board.GP1
        case 'GP10':
            return board.GP10
        case 'GP11':
            return board.GP11
        case 'GP12':
            return board.GP12
        case 'GP13':
            return board.GP13
        case 'GP14':
            return board.GP14
        case 'GP15':
            return board.GP15
        case 'GP16':
            return board.GP16
        case 'GP17':
            return board.GP17
        case 'GP18':
            return board.GP18
        case 'GP19':
            return board.GP19
        case 'GP2':
            return board.GP2
        case 'GP20':
            return board.GP20
        case 'GP21':
            return board.GP21
        case 'GP22':
            return board.GP22
        case 'GP23':
            return board.GP23
        case 'GP24':
            return board.GP24
        case 'GP25':
            return board.GP25
        case 'GP26':
            return board.GP26
        case 'GP26_A0':
            return board.GP26_A0
        case 'GP27':
            return board.GP27
        case 'GP27_A1':
            return board.GP27_A1
        case 'GP28':
            return board.GP28
        case 'GP28_A2':
            return board.GP28_A2
        case 'GP3':
            return board.GP3
        case 'GP4':
            return board.GP4
        case 'GP5':
            return board.GP5
        case 'GP6':
            return board.GP6
        case 'GP7':
            return board.GP7
        case 'GP8':
            return board.GP8
        case 'GP9':
            return board.GP9
        case 'LED':
            return board.LED
        case 'SMPS_MODE':
            return board.SMPS_MODE
        case 'STEMMA_I2C':
            return board.STEMMA_I2C
        case 'VBUS_SENSE':
            return board.VBUS_SENSE
        case 'VOLTAGE_MONITOR':
            return board.VOLTAGE_MONITOR
        case 'board_id':
            return board.board_id
        case _:
            return None
