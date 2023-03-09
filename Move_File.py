import os
import shutil

from_dir = "C:/Users/warri/Downloads"
to_dir = "C:/Users/warri/Documents"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file in list_of_files:
    nam, ext = os.path.splitext(file)

    if ext == "":
        continue
    elif ext in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + "/" + nam + ext
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + nam + ext

        if os.path.exists(path2):
            print("Moving ", file, ".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving ", file, ".....")
            shutil.move(path1,path3)
    
    