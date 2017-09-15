from random import shuffle

songs = input("Enter your songs, separated by a command and a space: ")

# converts songs to a list
list_of_songs = songs.split(', ')

# shuffles list of songs
shuffle(list_of_songs)

# creates file called songs.txt
with open ('songs.txt', 'w') as f:

	#loops through songs starting at 1
	for index, song in enumerate(list_of_songs, start=1):

		# changes songs and index to a string 
		string_of_songs = ("{} {} \n").format(index, song)

		# writes the songs and index to a file
		f.write(string_of_songs)