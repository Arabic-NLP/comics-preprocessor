#this is the preprocessor entry

from os import listdir
from os.path import isdir, join
import sys, os, inspect, pkgutil
from pathlib import Path
from importlib import import_module

# prepare current path and commands path
currentPath=Path(__file__).parent 
commandsPath=join(str(currentPath),"commands")

# add commands as sys path so that python could find the modules inside it 
sys.path.append(commandsPath)

#get module names from /commands
modulesNames = [f for f in listdir(commandsPath) if (isdir(join(commandsPath, f)) and (f != '__pycache__') and (f != 'commandBase'))]
print("Imported Modules are: ",modulesNames)

def dynamicImport(name):
    components = name.split('.')
    mod = __import__(components[0].strip())
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

#load all commands and test them
modules = dict()
for moduleName in modulesNames:
    importPath=moduleName+"."+moduleName
    modules[moduleName]= dynamicImport(importPath)
    # print(modules[moduleName])
    # print(moduleName) 
    # x=modules[moduleName]()


#
def __main__(phrase):
    phrase= phrase.split()
    try:
        print(phrase[0])
        mod=modules[phrase[0]]()
        mod.parameters=phrase[1]
        # mod.prepare()
        res=mod.execut()
        # mod.clean()
    except:
        res="error in __main__ from preprocessor mostly this command %s is not suported".format(phrase[0])
    finally:
        final_res={
            phrase[0]:res
        }
    return final_res

print(__main__(input()))