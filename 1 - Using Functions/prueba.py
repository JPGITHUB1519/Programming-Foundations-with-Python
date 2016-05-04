import webbrowser  
import time

cont = 0

print "This program started on : " + time.ctime()

while cont < 3 :

	time.sleep(5)
	webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
	#put the counter or the program will run infinely, virus XDDDDDD
	cont = cont + 1
