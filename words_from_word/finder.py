import codecs

with open('C://Users/79371/Desktop/python apps/words_from_word/russian_nouns.txt', encoding='utf-8') as f_input:
    words = f_input.read().split()
    f_input.close

rez_words = []

big_word = 'приставка'
for word in words:
    ok = True
    for letter in word:
        if letter not in big_word:
            ok = False
            break
    if not ok:
        continue
    ok = True
    big_word_copy = big_word
    for letter in word:
        if letter not in big_word_copy:
            ok = False
            break
        big_word_copy = big_word_copy.replace(letter, '', 1)
    if not ok:
        continue
    rez_words.append(word)

rez_words.sort(key=len)
for word in rez_words:
    print(word)

print(len(rez_words) - 1)