# this is used to filter the list of words into a new list of 5 letter words only

wordsNEW = open("english3NEW", "w")
words = open("english3.txt", "r")
for line in words:
    if len(line) == 6:
        wordsNEW.write(line.upper())

wordsNEW.close()
words.close()