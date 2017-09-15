# This little program takes some songs that the user inputs and
# shuffles them, then writes them to a text file. So for example,
# if you're in a band and change setlists between shows, you could use
# this to quickly make a new one.

from random import shuffle

songs = input("Enter your songs, separated by a command and a space: ")

list_of_songs = songs.split(', ')

shuffle(list_of_songs)

with open ('songs.txt', 'w') as f:
	for index, song in enumerate(list_of_songs, start=1):
		string_of_songs = ("{} {} \n").format(index, song)
		f.write(string_of_songs)