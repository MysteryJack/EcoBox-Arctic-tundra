def on_forever():
    if input.temperature() >= 30:
        pins.digital_write_pin(DigitalPin.P0, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
basic.forever(on_forever)

def on_in_background():
    radio.set_group(121)
    while True:
        radio.send_value("Temperature", input.temperature())
        radio.send_value("Light", input.light_level())
control.in_background(on_in_background)
