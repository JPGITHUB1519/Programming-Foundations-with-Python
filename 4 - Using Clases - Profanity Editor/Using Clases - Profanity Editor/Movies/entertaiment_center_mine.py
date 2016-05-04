import media
import fresh_tomatoes


# <name_of_file>.<function>

titanic = media.Movie("Titanic",
					  "A fictionalized account of the sinking of the RMS Titanic",
					  "https://titanicsound.files.wordpress.com/2014/11/titanic_movie-hd-1.jpg",
					  "https://www.youtube.com/watch?v=kVrqfYjkTdQ")


rockie = media.Movie("Rockie IV",
					 "StoryLine",
					 "http://peliculasaudiolatino.com/1movieimg/movie1275124387.jpg",
					 "https://www.youtube.com/watch?v=mIE5HYkzvV0")

karate_kid = media.Movie("The Karate Kid",
						 "StoryLine",
						 "https://upload.wikimedia.org/wikipedia/en/a/a9/Karate_kid.jpg",
						 "https://www.youtube.com/watch?v=n7JhKCQnEqQ")

searching_bf = media.Movie("Searching for Bobby Fischer",
						   "StoryLine",
						   "https://upload.wikimedia.org/wikipedia/en/a/ae/Searching_for_bobby_fischer.jpg",
						   "https://www.youtube.com/watch?v=8khmNiamBxo")

click = media.Movie("Click",
					"StoryLine",
					"https://upload.wikimedia.org/wikipedia/en/b/bd/Click_film.jpg",
					"https://www.youtube.com/watch?v=3-VfwPpbNg4")

hunger_games = media.Movie("The Hunger Games",
						   "Storyline",
						   "http://www.hungergamesdwtc.net/wp-content/uploads/2014/02/The-Hunger-Games-Poster-3.jpg",
						   "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [titanic, rockie, karate_kid, searching_bf, click, hunger_games]

#make the website
fresh_tomatoes.open_movies_page(movies)