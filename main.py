basic.show_string("RECIEVER")
radio.set_group(125)
serial.write_line("Acceleration")

# def on_received_number(receivedNumber):
#     led.toggle(4, 4)
#     serial.write_value("z", receivedNumber)
#     serial.write_value("y", receivedNumber)
#     serial.write_value("x", receivedNumber)
#     serial.write_value("zx", receivedNumber)
#     serial.write_value("xy", receivedNumber)
#     serial.write_line(str(input.compass_heading()))
# radio.on_received_number(on_received_number)
 


def on_received_value(name, value):
    led.toggle(4, 4)
    serial.write_value(name, value)
radio.on_received_value(on_received_value)
