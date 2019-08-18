import tweepy
import time

CONSUMER_KEY=''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

try:
	api = tweepy.API(auth)
	print("Authentication Success")
except:
	print("Authentication Failed")

def usrwtxt():
	for x in range(1,5):
		
		timelines = api.user_timeline(page = x)
			#print(timelines[0])

		for timeline in timelines:
			print(timeline.text+ '    -    ' + timeline.user.name)

while True:
	usrwtxt()
	time.sleep(10)
