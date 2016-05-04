import webbrowser  
import time

cont = 0

print "This program started on : " + time.ctime
while cont < 3 :

	# 7200 second =  2 hours
	time.sleep(7200)
	webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
	#put the counter or the program will run infinely, virus XDDDDDD
	cont = cont + 1