# Connect an LED to your Raspberry Pi and
# write a program to gradually increase brightness,
# and then gradually decrease brightness.



import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 1000)
pwm.start(0)

while True:
    try:
        for i in range(100):
            pwm.ChangeDutyCycle(i)
            time.sleep(.01)
    except KeyboardInterrupt:
        pwm.stop()  # stop PWM
        print("\n Stopped")
        GPIO.cleanup()  # cleanup all GPIO
        print("\n Cleaned Up GPIO")
        exit()
