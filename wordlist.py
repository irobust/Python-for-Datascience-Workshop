from urllib.request import urlopen

story = urlopen('https://sixty-north.com/c/t.txt')

words = []
for line in story:
    line_words = line.decode().split()
    for word in line_words:
        words.append(word)
        print(word)

