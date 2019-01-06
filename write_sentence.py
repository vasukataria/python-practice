from sys import argv

# f = open(filename, 'w')
# f.write('some string')
# f.close()

def write_sentence(filename, text):
    print('> filename:', filename)
    print('> text:', text)
    passing = open(filename, "w")
    passing.write(text)
    passing.close()

text = input()
write_sentence(argv[1], text)