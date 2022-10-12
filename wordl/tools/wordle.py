import codecs

with open('Desktop/мусор/tools/en_words.txt') as f_input:
    list_data = f_input.readlines()
    f_input.close

words = []

for line in list_data:
    lineWords=line.split()
    if len(lineWords[0])==5:
        words.append(lineWords[0]+"\n")

with open('Desktop/мусор/tools/words5en.txt', 'w', encoding='utf-8') as f_output:
    f_output.writelines(words)
    f_output.close