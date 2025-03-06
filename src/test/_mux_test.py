from time import sleep
import MuxDriver as m

while True:
    print("blinking yellow")
    m.send_mux(1, 1)
    sleep(1)
    m.send_mux(1, 0)

    print("blinking blue")
    m.send_mux(5, 1)
    sleep(1)
    m.send_mux(5, 0)

    print("blinking green")
    m.send_mux(9, 1)
    sleep(1)
    m.send_mux(9, 0)

    print("blinking red")
    m.send_mux(13, 1)
    sleep(1)
    m.send_mux(13, 0)
