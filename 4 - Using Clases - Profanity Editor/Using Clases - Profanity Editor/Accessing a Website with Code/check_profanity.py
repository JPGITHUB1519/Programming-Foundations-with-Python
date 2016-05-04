import urllib

# read the text from a file
def read_text() :

	quotes = open("C:\Users\user\Desktop\Using Clases - Profanity Editor\movie_quotes.txt")
	content_of_file = quotes.read()
	quotes.close()
	check_profanity(content_of_file)


# check if there is a curse word in the test using the wdylike appspot
def check_profanity(text_to_check) :

	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	connection.close()

	if "true" in output :

		print "Profanity alert"

	elif "false" in output :

		print "This document Has no Curse Words"

	else :

		print "Could  not Scan The document Properly "

read_text()