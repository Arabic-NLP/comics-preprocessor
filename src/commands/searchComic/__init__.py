from os import listdir
from os.path import isdir, join
import sys, os, inspect, pkgutil
from pathlib import Path
from importlib import import_module

# prepare current path and utilities path
currentPath=Path(__file__).parent 
CommandPath=currentPath
print(currentPath)
utilitiesPath=join(str(currentPath),"..","..","utilities")

# add utilities as sys path so that python could find the modules inside it 
sys.path.append(utilitiesPath)

# import base class commandBase, but call it "base"
basePath=join(str(currentPath),"..")
sys.path.append(basePath)
#print(sys.path)
from commandBase import commandBase as base


#get module names from /utilities
modulesNames = [f for f in listdir(utilitiesPath) if (isdir(join(utilitiesPath, f)) and (f != '__pycache__'))]
print("Imported Modules are: ",modulesNames)

def dynamicImport(name):
    components = name.split('.')
    print(components[0])   
    mod = __import__(components[0].strip())
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




class searchComic(base):
    
    def __init__(self):
        self.UNI= modules['unifyLanguage']() 
        self.token= modules['tokenizer']()
        self.detect= modules['wordDetector']()
    
    def execut(self):
        x = self.parameters        
        #UNI.phrase=x
        #x= UNI.allinone()
        self.token.phrase=x
        print(x)
        x= self.token.splitter()
        print(x)
        self.detect.lst=x
        print(x)
        x= self.detect.stoppingWordsRemover()
        print(x)
        self.token.phrase=x
        print(x)
        x= self.token.formatter()
        print(x)
        self.detect.phrase=x
        print(x)
        x= self.detect.removeIfNotExist()
        print(x)
        return x
    
    def allInOne():
        self.prepare()
        res= self.execut()
        self.clean()
        return res
    def clean():
        return 0
    def prepare():
        return 0   
    
    
    
'''
x= searchComic()
x.parameters=input("enter phrase to ssearch: ")
n= x.execut()
print("N",n)
f=open ("result.txt" , "w", encoding=('utf-8') )

for i in range(0,len(n)):
    f.write(n[i]+"\r\n")
f.close()


'''