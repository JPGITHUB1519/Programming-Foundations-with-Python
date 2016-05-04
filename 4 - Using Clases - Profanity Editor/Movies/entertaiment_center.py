import media
import fresh_tomatoes


# <name_of_file>.<function>

toy_story = media.Movie("Toy Story",
						"A history of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")

#print toy_story.movie_story_line

avatar = media.Movie("Avatar",
					 "A marine on a Alien Planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

titanic = media.Movie("Titanic",
					  "A fictionalized account of the sinking of the RMS Titanic",
					  "https://titanicsound.files.wordpress.com/2014/11/titanic_movie-hd-1.jpg",
					  "https://www.youtube.com/watch?v=kVrqfYjkTdQ")


school_of_rock = media.Movie("School of Rock",
							 "Storyline",
							 "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							 "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouille = media.Movie("Ratatouille",
						  "Storyline",
						  "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
						  "https://www.youtube.com/watch?v=niD-jahFURU")

midnight_in_paris = media.Movie("Midnight in Paris",
								"Storyline",
								"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
								"https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("The Hunger Games",
						   "Storyline",
						   "http://www.hungergamesdwtc.net/wp-content/uploads/2014/02/The-Hunger-Games-Poster-3.jpg",
						   "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story,avatar, school_of_rock, ratatouille,midnight_in_paris, hunger_games, titanic]

#make the website
#fresh_tomatoes.open_movies_page(movies)

# printing the docstring(documentation)
print media.Movie.__doc__

# show the name of the class

print media.Movie.__name__