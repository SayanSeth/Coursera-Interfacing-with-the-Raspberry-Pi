from gpiozero import LED, Button

led = LED(17)
button = Button(2)

while True:
    button.when_pressed = led.on
    button.when_released = led.off
