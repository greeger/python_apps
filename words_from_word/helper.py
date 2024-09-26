import codecs

with open('C://Users/79371/Desktop/python apps/words_from_word/russian_nouns_1.txt', encoding='utf-8') as f_input:
    words_1 = f_input.read().split('\n')
    f_input.close

with open('C://Users/79371/Desktop/python apps/words_from_word/russian_nouns_2.txt', encoding='utf-8') as f_input:
    words_2 = f_input.read().split('\n')
    f_input.close

with open('C://Users/79371/Desktop/python apps/words_from_word/russian_nouns_3.txt', encoding='utf-8') as f_input:
    words_3 = f_input.read().split('\n')
    f_input.close
    
rez_words = sorted(list(set(map(lambda word: word + '\n', words_1 + words_2 + words_3))))

with open('C://Users/79371/Desktop/python apps/words_from_word/russian_nouns.txt', 'w', encoding='utf-8') as f_output:
    f_output.writelines(rez_words)
    f_output.close