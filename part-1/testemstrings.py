movie = "2001: A SAMMY ODYSSEY"
book = "A Thousand Splendid Sharks"
poem = "sammy lived in a pretty how town"
nospaces = "sammywasaFINEfella"

# print(movie.islower())
# print(movie.isupper())
#
# print(book.istitle())
# print(book.isupper())
#
# print(poem.istitle())
# print(poem.islower())
#
#
# print("Is it all alphanum? ")
# print(str.isalnum(nospaces))
# print("What about all alpha?")
# print(str.isalnum(nospaces))
# print(nospaces)

print("Slices!")
print(nospaces[-4:-2])

print("Stride?")

print(movie[::3])

print("Count a string?!")
print(movie.count("0"))
print("First 0: "+str(movie.find("0")))

print("Multiply that string, bebeh!!!")
print(movie*3)

many = '''
This is a long string
But not a haiku
Just a long string
'''

many2 = '''\
This is a long string
But not a haiku
Just a long string\
'''
print(many)
print("Spacing on multi line strings")
print(many2)
print("Spacing on multi line strings")

print("The raw string")
print(r"Sammy says,\"The balloon\'s color is red.\"")
