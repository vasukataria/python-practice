from sys import argv

def add(numbers):
    sum=0
    for n in numbers:
        sum = sum+int(n)
    return sum

print('argv', argv)
print(add(argv[1:]))