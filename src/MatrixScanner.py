import MuxDriver as m
import pinmap_rp2 as p
from time import sleep

### imports for test
from machine import Pin
import MatrixScanner as mx
from time import sleep_us as speep

# rows 3-7 will be included later
rows = [p.row1, p.row2]


def scan_matrix():
    inputs = []
    for i in range(len(rows)):
        rows[i].value(1)
        print("reading row", end=":")
        print(i)
        for j in range(2):  # TODO range(8) in final
            print("  reading col", end=":")
            print(j)  # TODO remove
            sleep(1)

            results = m.read_mux(j)
            print("is this thing on?")
            print(results)
            if results == 1:
                inputs.append([i, j])
                print("    key pressed: ", end="")
                print(((i + 1) * 10) + j + 1)

        rows[i].value(0)

    return inputs
