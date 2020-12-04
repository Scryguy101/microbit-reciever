basic.showString("RECIEVER")
radio.setGroup(125)
serial.writeLine("Acceleration")
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    led.toggle(4, 4)
    serial.writeValue(name, value)
})
