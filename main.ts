basic.showString("RECIEVER")
radio.setGroup(125)
serial.writeLine("Acceleration")
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    led.toggle(4, 4)
    serial.writeValue("z", receivedNumber)
    serial.writeValue("y", receivedNumber)
    serial.writeValue("x", receivedNumber)
})
basic.forever(function on_forever() {
    
})
