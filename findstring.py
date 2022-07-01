# to check if a string is present in a text file
def search_str(file_path, word):
        with open(file_path, "r") as file:
            content = file.read()
            if word in content:
                print("string exists ")
            else:
                print("string does not exist in file")

search_str(r'C:\Users\FAWASI PC\Desktop\folderdir\hello1.txt', 'hello')