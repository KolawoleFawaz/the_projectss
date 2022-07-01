import os 
dir_path = r'\\ACER\Users\FAWASI PC\Desktop\folderdir'
word = str(input('type a word'))
for file in os.listdir(dir_path):
    cur_path = os.path.join(dir_path, file)

    if os.path.isfile(cur_path):
        with open(cur_path, 'r') as file:
            if word in file.read():
                print('string found')
            elif word not in file.read():
                print('string not found') 