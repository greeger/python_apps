import codecs
from email.policy import default

with open('C://Users/79371/Desktop/мусор/words5ru.txt', encoding='utf-8') as f_input:
    wordsRu = f_input.read().split()
    f_input.close
with open('C://Users/79371/Desktop/мусор/words5en.txt') as f_input:
    wordsEn = f_input.read().split()
    f_input.close

def getStats(words):
    stats=[{}, {}, {}, {}, {}]
    for word in words:
        for j in range(5):
            k=stats[j].get(word[j])
            stats[j][word[j]]= 1 if k==None else k+1
    return stats

def getSStats(words):
    sstats=[]
    stats=getStats(words)
    for stat in stats:
        sstat=list(stat.items())
        sstat.sort(key=lambda i: i[1], reverse=True)
        sstats.append(sstat)
    return sstats

def filterWords(words, filter):
    rezWords=[]
    for word in words:
        ok=True
        for i in range(5):
            if filter[1][i]==0:
                if filter[0][i] in word:
                    ok=False
            elif filter[1][i]==1:
                if (filter[0][i] not in word) or (word[i]==filter[0][i]):
                    ok=False
            else:
                if word[i]!=filter[0][i]:
                    ok=False
            if not ok:
                break
        if ok:
            rezWords.append(word)
    return rezWords

def getFilter(sugWord, realWord):
    filter=(sugWord,[])
    for i in range(5):
        if sugWord[i] not in realWord:
            filter[1].append(0)
        elif (sugWord[i] in realWord) and sugWord[i]!=realWord[i]:
            filter[1].append(1)
        else:
            filter[1].append(2)
    return filter

def getBestWord(allWords, words):
    minCount=len(words)**2
    rezWord=allWords[0]
    for allWord in allWords:
        k=0
        for word in words:
            k+=len(filterWords(words,getFilter(allWord,word)))
        if k<minCount or (k==minCount and allWord in words):
            minCount=k
            rezWord=allWord
    return rezWord




# https://wordle.belousov.one/
# https://www.nytimes.com/games/wordle/index.html
ruHardMode = False;
enHardMode = False;

words2=wordsRu
# word=getBestWord(wordsRu,wordsRu)
word="тоска"
print(word)
for i in range(6):
    rez=input().split()
    for j in range(5):
        rez[j]=int(rez[j])
    words2=filterWords(words2,(word,rez))
    word=getBestWord(words2 if ruHardMode else wordsRU, words2,words2)
    if len(words2)==1:
        print(word)
        break
    elif len(words2)==0:
        print("слово не в словаре")
        break
    else:
        print(word)

words2=wordsEn
# word=getBestWord(wordsEn,wordsEn)
word="raise"
print(word)
for i in range(6):
    rez=input().split()
    for j in range(5):
        rez[j]=int(rez[j])
    words2=filterWords(words2,(word,rez))
    word=getBestWord(words2 if enHardMode else wordsEn, words2)
    if len(words2)==1:
        print(word)
        break
    elif len(words2)==0:
        print("слово не в словаре")
        break
    else:
        print(word)