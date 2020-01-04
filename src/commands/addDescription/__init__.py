from os import listdir
from os.path import isdir, join
import sys, os, inspect, pkgutil
from pathlib import Path
from importlib import import_module

# prepare current path and utilities path
currentPath=str(Path(__file__).parent) 
CommandPath=currentPath
utilitiesPath=join(currentPath,"..","..","utilities")

# add utilities as sys path so that python could find the modules inside it 
sys.path.append(utilitiesPath)

# import base class commandBase, but call it "base"
basePath=join(currentPath,"..")
sys.path.append(basePath)
from commandBase import commandBase as base


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
    importPath=moduleName+"."+moduleName
    modules[moduleName]= dynamicImport(importPath)
    #print(modules[moduleName])
    #print(moduleName) 
    #x=modules[moduleName]()




class addDescription(base):
    UNI= modules['unifyLanguage']() 
    token= modules['tokenizer']()
    detect= modules['wordDetector']()
    
    def execut(self):
        x = self.parameters        
        UNI.phrase=x
        x= UNI.allinone()
        x= token.splt(x)
        x= stoppingWordsRemover(x)
        x= token.formater(x)
        x= detect.removeIfNotExist(x)
        return x    
    def prepare(self):
        self.parameters=self.parameters.split(",")   
        return
    
    def allInOne():
        return
    def clean():
        return
