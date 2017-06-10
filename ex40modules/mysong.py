class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
				print line

town_called_malice = ["Better stop dreaming of the quiet life", "'cause it's the one we'll never know",
"And quit running for that runaway bus", "'cause those rosy days are few",
"And stop apologizing for the things you've never done",
"'Cause time is short and life is cruel but it's up to us to change",
"This town called malice"]

puff_the_magic_dragon = Song(["A dragon lives forever but not so little boys",
"Painted wings and giant rings make way for other toys",
"One grey night it happened, Jackie Paper came no more",
"And Puff that mighty dragon, he ceased his fearless roar"
])


the_jam=Song(town_called_malice)

the_jam.sing_me_a_song()

puff_the_magic_dragon.sing_me_a_song()