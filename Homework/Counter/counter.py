people = int( input() )
words = int( input() )

if words % people == 0:
	print(people)
else:
	print(words % people)