import random
import string
import os
from os.path import splitext

def gen_code(len=4):
    li=random.sample(string.ascii_letters+string.digits,len)
    return ''.join(li)

def creat_files():
    li={gen_code() for i in range(100)}
    os.mkdir ('img')
    for i in li:
        os.mknod('img/'+i+'.png')
creat_files ()

def modify_suffix(dirname,old_suffix,new_suffix):
    pngfile=filter(lambda filename:filename.endswith(old_suffix),os.listdir(dirname))
    basefiles=[os.path.splitext(filename)[0] for filename in pngfile]
    for filename in basefiles:
        oldname=os.path.join(dirname,filename+old_suffix)
        newname=os.path.join(diename,filename+new_suffix)
        os.rename(oldname,newname)
        print("%s重命名为%成功" %(oldname,newname))
modify_suffix('img','.png','.jpg')