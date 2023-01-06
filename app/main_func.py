import os
import platform
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def Saving(path, string):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(string)

##necessário alteração nessa parte aqui.
##Fazer nova forma de encontrar os arquivos salvos.
##Talvez remover o /n do final na hora da leitura ou reconhecer o final.
##Fazer uma listagem a partir de um repositório
##Entre outras ideias
def controlFile(path):
    if(platform.system() == "Windows"):
        with open(p+"\\"+'scontrol.2dps', 'r', encoding='utf-8') as f:
            aux_str = f.readlines()
        with open(p+"\\"+'scontrol.2dps', 'w', encoding='utf-8') as f:
            for i in aux_str:
                f.writelines(p+ "\\" + i)
            f.writelines(p + "\\" + path)
                
    else:
        with open(p+"/"+'scontrol.2dps', 'r', encoding='utf-8') as f:
            aux_str = f.readlines()
        with open(p+"/"+'scontrol.2dps', 'w', encoding='utf-8') as f:
            for i in aux_str:
                f.writelines(p+ "/" + i)
            f.writelines(p+ "/" + path)

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

    
