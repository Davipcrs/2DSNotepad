import os
import platform
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(p)
def Saving(path, string):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(string)


def controlFile(path):
    if(platform.system() == "Windows"):
        with open(p+"\\"+'scontrol.2dps', 'a', encoding='utf-8') as f:
            f.write(p+ "\\" + path)
    else:
        with open(p+"/"+'scontrol.2dps', 'a', encoding='utf-8') as f:
            f.write(p+ "/" + path)
    

def loadFile(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def loadControlFile():
    if(platform.system() == "Windows"):
        with open(p+"\\"+'scontrol.2dps', 'r', encoding='utf-8') as f:
            return f.readlines()
    else:
        with open(p+"/"+'scontrol.2dps', 'r', encoding='utf-8') as f:
            return f.readlines()

    
