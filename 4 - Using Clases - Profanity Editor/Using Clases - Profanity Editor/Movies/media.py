
import webbrowser

#it is a good practice have each class in a different file

# creating the class movie

class Movie() :

	#this is the docstring or documentation string. we start it with """ 
	"""This class provides a way to Store movie relate information"""


	# creating the constructor -> create a instance of the object
	def __init__ (self, movie_title, movie_story_line, poster_image_url,trailer_youtube_url) :

		# this is a class variable
		# we put it in upper case because this is a constant

		VALID_RATINGS = ["G", "PG", "PG-13", "R"]

		# self refers to the object that we will initialize but not is a reserved - word
		# self can be whatever nameses
		# initilizing data
		self.title = movie_title
		self.movie_story_line = movie_story_line
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	# creating method to see the trailer

	def show_trailer(self) :

		webbrowser.open(self.trailer_youtube_url)

