import urllib

connection = urllib.urlopen("https://es.wikipedia.org/wiki/A")

text = connection.read()

connection.close()


print text