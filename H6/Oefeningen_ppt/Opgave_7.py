song = "Barefoot on the grass,# listening to our favorite song"
hashtag_index = song.find("#")
song_after_hashtag = song[hashtag_index + 1:].strip()
print(song_after_hashtag)
