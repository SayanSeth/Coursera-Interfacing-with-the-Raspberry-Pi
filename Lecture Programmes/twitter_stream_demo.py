# Print 'Found It' if <text> is found

from twython import TwythonStreamer

C_key = "<Consumer Key (API Key)>"
C_secret = "<Consumer Secret (API Secret)>"
A_token = "<Access Token>"
A_secret = "<Access Token Secret>"

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            print("Found It!!")

stream = MyStreamer(C_key,C_secret,A_token,A_secret)

stream.statuses.filter(track='<text>')