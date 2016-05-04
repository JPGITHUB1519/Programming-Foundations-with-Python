def read_text() :

	quotes = open("C:\Users\user\Desktop\Using Clases - Profanity Editor\movie_quotes.txt")
	content_of_file = quotes.read()
	print content_of_file
	quotes.close()

read_text()