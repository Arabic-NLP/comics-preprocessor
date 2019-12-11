from os import listdir
from os.path import isfile, join
import sys
import inspect
import pkgutil
from pathlib import Path
from importlib import import_module

currentPath=Path(__file__).parent 
CommandPath=currentPath
utilitiesPath=join(currentPath,"utilities")

print(utilitiesPath)
path= join(utilitiesPath,"hy.py")
print(path)

onlyfiles = [f for f in listdir(utilitiesPath) if isfile(join(utilitiesPath, f))]
onlyfiles.append("commandBase.py.commandBase")

def dynamicImport(name,path):
    components = name.split('.')
    print(components[0])
    mod = __import__(name,path)#components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

#for f in onlyfiles:
    #f=f+".py"
    #file = join(utilitiesPath,f)    
    #print(file)
    #import_module('.' + file , package=f.split(".")[0])
#modules = map(__import__, onlyfiles)
#for f in onlyfiles:
    
file = join("src","commands","utilities")
print(file) 
module= dynamicImport("tokenizer.py",file)


class searchComic(commandBase):
    UNI= unifyLanguage()
    token= tokenizer()
    detect=wordDetector()
    
    def execut(self):
        x = self.parameters        
        UNI.phrase=x
        x= UNI.allinone()
        x= token.splt(x)
        x= stoppingWordsRemover(x)
        x= token.formater(x)
        x= detect.removeIfNotExist(x)
        return x