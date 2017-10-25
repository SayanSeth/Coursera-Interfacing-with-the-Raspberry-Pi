# This programme tweets <text>

from twython import Twython

C_key = "<key>"
C_secret = "<key>"
A_token = "<key>"
A_secret = "<key>"

my_twitter = Twython(C_key,C_secret,A_token,A_secret)
my_twitter.update_status(status="<Text>")
