# Wordcount - count the number of times a word appears in a document.
# Peter Koppelman January 7, 2018


def wordcount(w):
    with open(r'c:\users\madan\Onthe1stdayofChristmas.txt', 'r') as f:

        wc = 0
        for words in f:
            line = words.split()
            if len(line) != 0:
                for x in line:
                    if x.lower() == w.lower():
                        wc += 1

    print('{} appears in the file {} times'.format(w, wc))


if __name__ == '__main__':
    word = 'Christmas'
    wordcount(word)