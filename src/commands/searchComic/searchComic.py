from os import listdir
from os.path import isdir, join
import sys, os
import inspect
import pkgutil
from pathlib import Path
from importlib import import_module
#from commandBase import commandBase 

# prepare current path and utilities path
currentPath=Path(__file__).parent 
CommandPath=currentPath
utilitiesPath=join(currentPath,"..","..","utilities")

# add utilities as sys path so that python could find the modules inside it 
sys.path.append(utilitiesPath)

basePath=join(currentPath,"..")
sys.path.append(basePath)
print(sys.path)
from commandBase import commandBase
#print()

#get module names from /utilities
modulesNames = [f for f in listdir(utilitiesPath) if (isdir(join(utilitiesPath, f)) and (f != '__pycache__'))]
print(modulesNames)

def dynamicImport(name):
    components = name.split('.')    
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

#load all utilities and test them
modules = dict()
for moduleName in modulesNames:
    moduleName=moduleName+"."+moduleName
    modules[moduleName]= dynamicImport(moduleName)
    #print(modules[moduleName])
    #x=modules[moduleName]()




#class searchComic(base):
    #UNI= unifyLanguage()
    #token= tokenizer()
    #detect=wordDetector()
    
    #def execut(self):
        #x = self.parameters        
        #UNI.phrase=x
        #x= UNI.allinone()
        #x= token.splt(x)
        #x= stoppingWordsRemover(x)
        #x= token.formater(x)
        #x= detect.removeIfNotExist(x)
        #return x