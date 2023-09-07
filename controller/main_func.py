import os
import platform
from model.path import PathModel
p = PathModel().appUsrDir


def saving(path, string):
    if platform.system == "Windows":
        with open(p+'\\'+path, 'w', encoding='utf-8') as f:
            f.write(string)
    else:
        with open(p+'/'+path, 'w', encoding='utf-8') as f:
            f.write(string)

   

def loadFile(path):
    if platform.system == "Windows":
        with open(p+'\\'+path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        with open(p+'/'+path, 'r', encoding='utf-8') as f:
            return f.read()

def loadControlDir():
    return os.listdir(p)
    
def mkdir():
    if os.path.isdir(p) == False:
        print('create')
        os.mkdir(p)
        return 
   