file = open("movie.txt", "w")
file.write("Fav movies: Pandippada, cid moosa, vettam")
file.close()

file = open("movie.txt", "r")
content = file.read()
print(content)