# Write a program on your Raspberry Pi that searches a
# Twitter stream for tweets containing the string “Ian G. Harris”.
# When 3 or more such tweets are found, your program should print “Ian G. Harris is popular!”



from twython import TwythonStreamer

C_key = "<key>"
C_secret = "<key>"
A_token = "<key>"
A_secret = "<key>"


class MyStreamer(TwythonStreamer):
    i = 0

    def on_success(self, data):
        if 'text' in data:
            print("Found It! {}".format(data['text']))
            MyStreamer.i = MyStreamer.i + 1
            if MyStreamer.i >= 3:
                print("Ian G. Harris is popular!")

stream = MyStreamer(C_key, C_secret, A_token, A_secret)

stream.statuses.filter(track='Ian G. Harris')
