import os
import shutil




file_path = ""
source = "D:/Dakshiin/Python/class99project/folder1"
destination = "D:/Dakshiin/Python/class99project/folder2"
print(os.listdir(source))

for file_name in os.listdir(source):
    print(file_name)
    file_path = source+"/"+ file_name
    print(file_name.find(".txt"))
    shutil.move(file_path, destination)
    
