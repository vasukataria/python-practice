from sys import argv
script, user_name = argv[1:]
prompt = '> '

print(argv)
print("0: ", argv[0])
print("1: ",argv[1])
print("2: ",argv[2])
# print("3: ",argv[3])
print(script, user_name)

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))