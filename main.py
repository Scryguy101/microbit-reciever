basic.show_string("RECIEVER")
radio.set_group(125)
serial.write_line("Acceleration")

def on_received_number(receivedNumber):
    led.toggle(4, 4)
    serial.write_value("z", receivedNumber)
    serial.write_value("y", receivedNumber)
    serial.write_value("x", receivedNumber)
    serial.write_value("zx", receivedNumber)
    serial.write_value("xy", receivedNumber)

radio.on_received_number(on_received_number)
 
def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)


