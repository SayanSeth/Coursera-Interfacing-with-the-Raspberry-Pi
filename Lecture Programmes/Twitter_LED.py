# Python Programme to light uo a LED if <text> in found


from twython import TwythonStreamer
from gpiozero import LED
from time import sleep

C_key = "<key>"
C_secret = "<key>"
A_token = "<key>"
A_secret = "<key>"

red = LED(17)

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            print("Found It!!")
            red.on()
            sleep(10)
            red.off()


stream = MyStreamer(C_key,C_secret,A_token,A_secret)

stream.statuses.filter(track='<text>')