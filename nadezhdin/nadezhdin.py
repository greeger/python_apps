import re
import urllib.request

with urllib.request.urlopen("https://nadezhdin2024.ru/signatures") as fp:
    list_data = fp.read().decode("utf8").split('\n')

sum = 0
for line in list_data:
    if re.search('Отсортировано подписей', line):
        num = (int)(line.split('Отсортировано подписей: ')[1].split(' ')[0].split('<')[0])
        sum += min(num, 2500)
sum = (int)(sum/2)
print(sum)
