from abc import ABC, abstractmethod

class commandBase (ABC): 
    parameters =None
    comicID =None
    
    @abstractmethod    
    def prepare(self):
        pass
    
    @abstractmethod    
    def execut(self):
        pass
    
    @abstractmethod    
    def clean(self):
        pass
    
    @abstractmethod    
    def allInOne(self):
        pass
    

class searchComic(commandBase):
    def execut(self):
        return 
    
    
class addDescription(commandBase):
    def prepare(self):
        return
    
    def execut(self):
        return
    

class deleteComic(commandBase):
    def execut(self):
        return
    


class unifyLanguage:
    def __init__(self, ph):
        self.phrase=ph
    
    
    def numUnifier(self):
        return phrase
    
    def translator(self, engASCII):
        return 
    
    def stringUnifier(self):
        return phrase


class tokenizer:
    def __init__(self, ph):
        self.phrase=ph
        
    def numloader(self,file):
        return
    
    def splitter(self):
        return list
    
    def testAppendBefore(self):
        return 
    
    def testAppendAfter(self):
        return
    
    def formatter(self):
        return list
    
    
class wordDetector:
    def __init__(self, li):
        self.list=li
        
    def stoppingWordLoader(self,file):
        return 
        
    def stoppingWordsRemover(self):
        return
    
    def specialCharsRemover(self):
        return
    
    def suffixRemover(self):
        return
    
    def prefixRemover(self):
        return
    
    def removeIfNotExist(self):
        return 
    
    
    
    
    
        
        
        
    
    
    
    


    
    