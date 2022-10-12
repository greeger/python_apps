import codecs

class Time:
    def __init__(self, line):
        numbers = line.split(':')
        self.h = int(numbers[0])
        self.m = int(numbers[1])
        self.s = float(numbers[2].replace(',', '.'))
    
    def get_line(self):
        return '%02d:%02d:'%(self.h, self.m) + ('%06.3f'%(self.s)).replace('.', ',')

    def add_m(self, n):
        self.m += n
        if n > 0:
            while self.m >= 60:
                self.h += 1
                self.m -= 60
        elif n < 0:
            while self.m < 0:
                self.h -= 1
                self.m += 60
        return self.get_line()

    def add_s(self, n):
        self.s += n
        cur_m = 0
        if n > 0:
            while self.s >= 60:
                cur_m += 1
                self.s -= 60
        elif n < 0:
            while self.s < 0:
                cur_m -= 1
                self.s += 60
        self.add_m(cur_m)
        return self.get_line()

file_name = 'C:/Users/79371/Downloads/suits-s04/Suits.S04E01.HDTV.x264-LOL.srt'

with open(file_name) as f_input:
    list_data = f_input.readlines()
    f_input.close
list_data[0] = '1\n'

words = []

for line in list_data:
    line_words=line.split(' --> ')
    if(len(line_words) < 2):
        words.append(line)
    else:
        t0 = Time(line_words[0])
        t1 = Time(line_words[1])
        words.append(t0.add_s(1) + ' --> ' + t1.add_s(1) + "\n")

with open(file_name[:len(file_name)-4]+'_new.srt', 'w', encoding='utf-8') as f_output:
    f_output.writelines(words)
    f_output.close