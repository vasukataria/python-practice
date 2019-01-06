from sys import argv

def make_sentence(filename):
    sentence = ""
    word_file= open(filename)
    for word in word_file:
        word = word.strip()
        if word !=  "":
            if word[-1] != ".":
                sentence = sentence + word + " "
            else:
                sentence = sentence + word + "\n"
        # print('>', sentence)
    word_file.close()
    return sentence.strip()
        

output = make_sentence(argv[1])
print(output)

assert output == 'python is an awesome language.\nyou must learn python.'