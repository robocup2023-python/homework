import os
print(os.path.abspath('.'))
import os
folder_path='/home/robocup/PycharmProjects/pythonProject1/img'
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        new_filename=os.path.splitext(filename)[0]+".jpg"
        old=os.path.join(folder_path,filename)
        new=os.path.join(folder_path,new_filename)
        os.rename(old,new)
