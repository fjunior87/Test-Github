ten_things = 'Apples oranges Crows Telephone Light Sugar'

print "Wait there's no 10 things in the list, let's fix this"

stuff = ten_things.split(" ")

more_stuff = ["Day","Night","Song","Frisbee","Corn", "Banana","Girl"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ",next_one
	
	stuff.append(next_one)
	
	print "There's %d items now."%len(stuff)
	
print "There we go ", stuff

print "Let's do something with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
	