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

    def more_than(self, new_time):
        if self.h > new_time.h:
            return True
        if self.h < new_time.h:
            return False
        if self.m > new_time.m:
            return True
        if self.m < new_time.m:
            return False
        if self.s < new_time.s:
            return False
        return True

file_name = 'C:/Users/79371/Downloads/suits-s08/Suits.S08E16.720p.BluRay.X264-REWARD.srt'

# when shift starts (in video) and seconds of it
times = [(Time('00:00:00'), 5), (Time('00:04:20'), 4), (Time('00:13:03'), 3), (Time('00:18:43'), 2.5), (Time('00:26:45'), 0.5), (Time('00:33:09'), -1), ]

for i in range(1, len(times)):
    times[i][0].add_s(-times[i-1][1])

with open(file_name) as f_input:
    list_data = f_input.readlines()
    f_input.close
list_data[0] = '1\n'

rez = []

for line in list_data:
    line_words=line.split(' --> ')
    if(len(line_words) < 2):
        rez.append(line)
    else:
        t0 = Time(line_words[0])
        t1 = Time(line_words[1])

        for i in range(len(times)-1, -1, -1):
            if t0.more_than(times[i][0]):
                rez.append(t0.add_s(times[i][1]) + ' --> ' + t1.add_s(times[i][1]) + "\n")
                break

with open(file_name[:len(file_name)-4]+'_new.srt', 'w', encoding='utf-8') as f_output:
    f_output.writelines(rez)
    f_output.close