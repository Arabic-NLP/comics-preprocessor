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