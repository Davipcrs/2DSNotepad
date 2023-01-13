import os
import platform
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def saving(path, string):
    if platform.system == "Windows":
        with open('text\\'+path, 'w', encoding='utf-8') as f:
            f.write(string)
    else:
        with open('text/'+path, 'w', encoding='utf-8') as f:
            f.write(string)



def loadFile(path):
    if platform.system == "Windows":
        with open('text\\'+path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        with open('text/'+path, 'r', encoding='utf-8') as f:
            return f.read()

def loadControlDir():
    if platform == "Windows":
        return os.listdir(p+"\\"+"text")
    else:
        return os.listdir(p + '/'+"text")
    
    
def mkdir():
    if platform == "Windows":
        if os.path.isdir(p+"\\"+"text") == False:
            os.mkdir(p+"\\"+"text")
    else:
        if os.path.isdir(p+"/"+"text") == False:
            os.mkdir(p + '/'+"text")