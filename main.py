basic.show_string("RECIEVER")
radio.set_group(125)
serial.write_line("Acceleration")

def on_received_value(name, value):
    led.toggle(4, 4)
    serial.write_value(name, value)
radio.on_received_value(on_received_value)
