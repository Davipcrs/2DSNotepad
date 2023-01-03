import os
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def Saving(path, string):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(string)


def controlFile(path):
    with open(p+"\\"+'scontrol.2dps', 'a', encoding='utf-8') as f:
        f.write(p+ "\\" + path)
    pass

def loadFile(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    



