#420_NAME_BOT

from datetime import datetime
import random

NUMBER_OF_NAMES = 1 #change this value for more outputs

for x in range(NUMBER_OF_NAMES):

	paint = file('_assets/paint.txt').readlines()
	suffix = file('_assets/suffix.txt').readlines()

	writeme = "%s %s \n" % (random.choice(paint).rstrip(), random.choice(suffix).rstrip() )

	with open("tweet_" + datetime.now().strftime("%H:%M:%S").replace(':','.') + ".txt",'a') as output:
	    output.write(writeme)
	

