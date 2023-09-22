def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P0, 180)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.servo_write_pin(AnalogPin.P0, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)
