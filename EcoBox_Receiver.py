def on_received_value(name, value):
    global Temperature, Light_level
    if name == "Temperature":
        Temperature = value
    elif name == "Light":
        Light_level = value
radio.on_received_value(on_received_value)

Light_level = 0
Temperature = 0
radio.set_group(121)
serial.set_baud_rate(BaudRate.BAUD_RATE9600)
while True:
    if Temperature != -274 and Light_level != -1:
        dataStreamer.write_number_array([Temperature, Light_level])
        Temperature = -274
        Light_level = -1
