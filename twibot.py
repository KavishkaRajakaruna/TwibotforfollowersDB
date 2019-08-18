import tweepy
import time
import mysql.connector


CONSUMER_KEY='yd93UC5uCzySNKQWN5HqRHn3b'
CONSUMER_SECRET = 'ERX01c6IDIG1loMxHa2XPi3p6g8SViruXwoek5ZgOnKalQkSlq'
ACCESS_KEY = '1040889328069697536-cAZLhTDH8C70PuruHME5Vfo8r6zrY1'
ACCESS_SECRET = 'L2kZLJIGBJI3qHbI2JLLnRDd5PDcYOQgTTlQRCxxmD0NJ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

try:
	api = tweepy.API(auth)
	print("Authentication Success")
except:
	print("Authentication Failed")

db = mysql.connector.connect(
	host ="localhost",
	user ="usradmin",
	passwd ="abc@123",
	database ="twitusers"
	)
mycursor = db.cursor()

sql="insert into users (UID,Name) values (%s,%s)"


def usrwtxt():
	for x in range(1,5):
		
		timelines = api.home_timeline(page = x)
			#print(timelines[0])

		for timeline in timelines:
			#print(timeline.text+ '    -    ' + timeline.user.name)
			val=(timeline.user.id,timeline.user.name)
			print(val)
			try:
				mycursor.execute(sql,val)
				db.commit()
			except Exception:
				print("database push error")


while True:
	usrwtxt()
	time.sleep(10)