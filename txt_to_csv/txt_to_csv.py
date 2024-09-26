import codecs
import pathlib

input_dir_name = 'C:/Users/79371/Downloads/Telegram Desktop/experiment_data/experiment_data/'
output_dir_name = 'C:/Users/79371/Desktop/Subscheme_time_test/'

with open(output_dir_name + 'Subscheme_time' + '.csv', 'w', encoding='utf-8') as f_output_time,\
      open(output_dir_name + 'Subscheme_test' + '.csv', 'w', encoding='utf-8') as f_output_test:

    rez_time = ['subject,trial,stim,task,time,correct\n']
    rez_test = ['subject,trial,pair,type,choice\n']
        
    input_directory = pathlib.Path(input_dir_name)
    for currentFile in input_directory.iterdir():
        with open(currentFile) as f_input:
            list_data = f_input.readlines()

        filename = currentFile.name.split('.')[3]

        i = 1
        for line in list_data[50:200]:
            rez_time.append(filename+','+(str)(i)+','+line.replace(' ', ','))
            i += 1
        
        i = 1
        for line in list_data[200:]:
            rez_test.append(filename+','+(str)(i)+','+line.replace(' ', ','))
            i += 1
        
    f_output_time.writelines(rez_time)
    f_output_test.writelines(rez_test)