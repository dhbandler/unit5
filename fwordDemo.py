#Sam Smedinghoff
#4/23/18
#fwordDemo.py - print out only the words that have an f

words = input('Type in some words: ').split(' ')

for item in words:
    if 'f' in item or 'F' in item:
        print(item)
