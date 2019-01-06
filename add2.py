from sys import argv
def add(filename):
    '''
    Reads the numbers from the given file and returns the summation of the numbers
    '''
    # Write your code below
    sum = 0
    num_file = open(filename)
    for line in num_file:
        sum=sum+int(line)
    num_file.close()
    return sum

print(add(argv[1]))  # take filename as argument