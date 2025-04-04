from time import sleep_us
from rpad import rotopad
from machine import Pin

board = rotopad.profile()
rows = board[0]
cols = board[1]
buttons = board[2]


def scan_matrix():
    """Scans through every input and returns a array of activated inputs
    returns: array of integers representing row/column location of activated input.
    row 1, column 5 will be indicated as 15
    10s position is the row, 1s position is column
    buttons are represented as values < 10
    """
    inputs = []

    for i in range(len(rows)):
        rows[i].value(1)
        for j in range(len(cols)):
            if cols[j].value() == 1:
                inputs.append((i + 1) * 10 + (j + 1))
    for k in range(len(buttons)):
        if buttons[k] == 1:
            inputs.append(k + 1)

    return inputs
