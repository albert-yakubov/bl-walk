def on_bluetooth_connected():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
    TobbieII.vibrate(5)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_leds("""
        # # . # #
        # # . # #
        . . . . .
        . # # # .
        . # # # .
        """)
    TobbieII.shake_head(2)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global RX_Data
    RX_Data = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    if RX_Data.char_at(0) == "C" and len(RX_Data) == 11:
        basic.clear_screen()
        TobbieII.drawface(RX_Data)
    else:
        if RX_Data.char_at(0) == "Z":
            RX_Data = RX_Data.substr(1, len(RX_Data))
            basic.show_string(RX_Data)
            led.plot(0, 1)
            led.plot(0, 2)
            led.plot(0, 3)
            led.plot(1, 0)
            led.plot(1, 4)
            led.plot(2, 0)
            led.plot(2, 4)
            led.plot(3, 0)
            led.plot(3, 4)
            led.plot(4, 1)
            led.plot(4, 2)
            led.plot(4, 3)
        else:
            if len(RX_Data) == 2:
                if RX_Data.compare("A4") == 0:
                    basic.clear_screen()
                    TobbieII.stopturn()
                    TobbieII.stopwalk()
                    led.plot(0, 1)
                    led.plot(0, 2)
                    led.plot(0, 3)
                    led.plot(1, 0)
                    led.plot(1, 4)
                    led.plot(2, 0)
                    led.plot(2, 4)
                    led.plot(3, 0)
                    led.plot(3, 4)
                    led.plot(4, 1)
                    led.plot(4, 2)
                    led.plot(4, 3)
                elif RX_Data.compare("A5") == 0:
                    basic.clear_screen()
                    TobbieII.stopwalk()
                    TobbieII.rightward()
                    led.plot(0, 2)
                    led.plot(1, 1)
                    led.plot(1, 3)
                    led.plot(2, 0)
                    led.plot(2, 4)
                elif RX_Data.compare("A3") == 0:
                    basic.clear_screen()
                    TobbieII.stopwalk()
                    TobbieII.leftward()
                    led.plot(2, 0)
                    led.plot(2, 4)
                    led.plot(3, 1)
                    led.plot(3, 3)
                    led.plot(4, 2)
                elif RX_Data.compare("B00") == 0:
                    basic.clear_screen()
                    led.plot(2, 1)
                    led.plot(0, 2)
                    led.plot(1, 2)
                    led.plot(2, 2)
                    led.plot(3, 2)
                    led.plot(4, 2)
                    led.plot(2, 3)
                elif RX_Data.compare("A7") == 0:
                    TobbieII.backward()
                    TobbieII.stopturn()
                    basic.clear_screen()
                    led.plot(0, 2)
                    led.plot(1, 1)
                    led.plot(2, 0)
                    led.plot(3, 1)
                    led.plot(4, 2)
                elif RX_Data.compare("A1") == 0:
                    TobbieII.forward()
                    TobbieII.stopturn()
                    basic.clear_screen()
                    led.plot(0, 2)
                    led.plot(1, 3)
                    led.plot(2, 4)
                    led.plot(3, 3)
                    led.plot(4, 2)
                elif RX_Data.compare("A8") == 0:
                    TobbieII.backward()
                    TobbieII.leftward()
                    basic.clear_screen()
                    led.plot(0, 0)
                    led.plot(1, 0)
                    led.plot(2, 0)
                    led.plot(3, 0)
                    led.plot(0, 1)
                    led.plot(1, 1)
                    led.plot(0, 2)
                    led.plot(2, 2)
                    led.plot(0, 3)
                    led.plot(3, 3)
                elif RX_Data.compare("A6") == 0:
                    TobbieII.backward()
                    TobbieII.rightward()
                    basic.clear_screen()
                    led.plot(1, 0)
                    led.plot(2, 0)
                    led.plot(3, 0)
                    led.plot(4, 0)
                    led.plot(3, 1)
                    led.plot(4, 1)
                    led.plot(2, 2)
                    led.plot(4, 2)
                    led.plot(1, 3)
                    led.plot(4, 3)
                elif RX_Data.compare("A0") == 0:
                    TobbieII.forward()
                    TobbieII.leftward()
                    basic.clear_screen()
                    led.plot(0, 1)
                    led.plot(3, 1)
                    led.plot(0, 2)
                    led.plot(2, 2)
                    led.plot(0, 3)
                    led.plot(1, 3)
                    led.plot(0, 4)
                    led.plot(1, 4)
                    led.plot(2, 4)
                    led.plot(3, 4)
                elif RX_Data.compare("A2") == 0:
                    TobbieII.forward()
                    TobbieII.rightward()
                    basic.clear_screen()
                    led.plot(1, 1)
                    led.plot(4, 1)
                    led.plot(2, 2)
                    led.plot(4, 2)
                    led.plot(3, 3)
                    led.plot(4, 3)
                    led.plot(1, 4)
                    led.plot(2, 4)
                    led.plot(3, 4)
                    led.plot(4, 4)
                else:
                    TobbieII.stopwalk()
                    TobbieII.stopturn()
                    basic.clear_screen()
                    led.plot(0, 1)
                    led.plot(0, 2)
                    led.plot(0, 3)
                    led.plot(1, 0)
                    led.plot(1, 4)
                    led.plot(2, 0)
                    led.plot(2, 4)
                    led.plot(3, 0)
                    led.plot(3, 4)
                    led.plot(4, 1)
                    led.plot(4, 2)
                    led.plot(4, 3)
            elif len(RX_Data) == 3:
                if RX_Data.compare("C01") == 0:
                    basic.clear_screen()
                    led.plot(1, 1)
                    led.plot(3, 1)
                    led.plot(0, 3)
                    led.plot(1, 4)
                    led.plot(2, 4)
                    led.plot(3, 4)
                    led.plot(4, 3)
                elif RX_Data.compare("C02") == 0:
                    basic.clear_screen()
                    led.plot(1, 1)
                    led.plot(3, 1)
                    led.plot(0, 4)
                    led.plot(1, 3)
                    led.plot(2, 3)
                    led.plot(3, 3)
                    led.plot(4, 4)
                elif RX_Data.compare("C03") == 0:
                    basic.clear_screen()
                    led.plot(1, 1)
                    led.plot(3, 1)
                    led.plot(0, 4)
                    led.plot(3, 1)
                    led.plot(1, 3)
                    led.plot(2, 4)
                    led.plot(3, 3)
                    led.plot(4, 4)
                elif RX_Data.compare("C04") == 0:
                    basic.clear_screen()
                    led.plot(0, 0)
                    led.plot(4, 0)
                    led.plot(1, 1)
                    led.plot(3, 1)
                    led.plot(0, 3)
                    led.plot(1, 3)
                    led.plot(2, 3)
                    led.plot(3, 3)
                    led.plot(4, 3)
                    led.plot(0, 4)
                    led.plot(2, 4)
                    led.plot(4, 4)
                elif RX_Data.compare("C05") == 0:
                    basic.clear_screen()
                    led.plot(0, 1)
                    led.plot(1, 1)
                    led.plot(3, 1)
                    led.plot(4, 1)
                    led.plot(1, 3)
                    led.plot(2, 3)
                    led.plot(3, 3)
                elif RX_Data.compare("C06") == 0:
                    basic.clear_screen()
                    led.plot(1, 0)
                    led.plot(3, 0)
                    led.plot(2, 2)
                    led.plot(1, 3)
                    led.plot(3, 3)
                    led.plot(2, 4)
                elif RX_Data.compare("C07") == 0:
                    basic.clear_screen()
                    led.plot(0, 0)
                    led.plot(4, 0)
                    led.plot(0, 2)
                    led.plot(1, 2)
                    led.plot(2, 2)
                    led.plot(3, 2)
                    led.plot(4, 2)
                    led.plot(3, 3)
                    led.plot(4, 3)
                    led.plot(3, 4)
                    led.plot(4, 4)
                elif RX_Data.compare("C08") == 0:
                    basic.clear_screen()
                    led.plot(1, 0)
                    led.plot(3, 0)
                    led.plot(0, 1)
                    led.plot(1, 1)
                    led.plot(2, 1)
                    led.plot(3, 1)
                    led.plot(4, 1)
                    led.plot(0, 2)
                    led.plot(1, 2)
                    led.plot(2, 2)
                    led.plot(3, 2)
                    led.plot(4, 2)
                    led.plot(1, 3)
                    led.plot(2, 3)
                    led.plot(3, 3)
                    led.plot(2, 4)
                else:
                    basic.clear_screen()
                    led.plot(1, 0)
                    led.plot(2, 0)
                    led.plot(3, 0)
                    led.plot(0, 1)
                    led.plot(2, 1)
                    led.plot(4, 1)
                    led.plot(0, 2)
                    led.plot(1, 2)
                    led.plot(2, 2)
                    led.plot(3, 2)
                    led.plot(4, 2)
                    led.plot(1, 3)
                    led.plot(2, 3)
                    led.plot(3, 3)
                    led.plot(1, 4)
                    led.plot(2, 4)
                    led.plot(3, 4)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

RX_Data = ""
bluetooth.start_uart_service()
TobbieII.stopwalk()
TobbieII.stopturn()
RX_Data = ""
basic.show_leds("""
    # # . # #
    # # . # #
    . . . . .
    . # # # .
    . # # # .
    """)