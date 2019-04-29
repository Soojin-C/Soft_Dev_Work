# team Reduction Eruption - Bo Lu, Soojin Choi
# SoftDev2 pd07
# K20 -- Reductio ad Absurdum
# 2019-04-28

from functools import reduce

def reader(filename):
    file = open(filename, "r")
    l = file.read().split("\n")
    list = []
    for each in l:
        list+=each.split()

    #print(list)
    return list

#book = reader('excerpt.txt')
book = reader('dracula.txt')
def freq(word):
    list = [1 for x in book if x == word]
    print("Frequency of: " + word + "-> " + str( len(list) ) )
    return reduce(lambda x,y: x+y, list)

freq("the")
print(freq("I"))


def freq_Group(wordList):
    if len(wordList) == 1:
        return freq(wordList[0])
    word = reduce(lambda x,y: x+y, wordList)
    #print(word)
    list = [x if x in wordList else 0 for x in book ]
    #print(list)
    words = [ reduce(lambda x,y: str(x) + str(y),list[x: x+len(wordList)]) for x in range(len(list) - len(wordList))]
    #print(words)
    list = [1 if x == word else 0 for x in words]
    freqW = reduce(lambda x,y: x+y, list)
    print ("The frequency of " + word + " is " + str(freqW))
    return freqW

freq_Group(["I", "cried,", "the"])
freq_Group(["let", "us", "come"])

def mfhelp (word):
    list = [1 for x in book if x == word]
    return reduce(lambda x,y: x+y, list)

def mostFreq():
    master = []
    [master.append(x) for x in book  if x not in master]
    #print(master)
    freqsM = [[mfhelp(x),x] for x in master]
    print(freqsM)
    max = reduce(lambda x,y: x if x[0] > y[0] else y, freqsM)
    print(max)
    print('The most frequent word is "'  + max[1] + '" with ' + str(max[0]))
    return max
mostFreq()
