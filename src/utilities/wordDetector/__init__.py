class wordDetector:
    def __init__(self):
        self.lst=[]
        
    def stoppingWordLoader(self):
        f=open("stoppingWords.txt", "r")
        content= f.readlines()
        stopping=[]
        for i in content:
            stopping.append(i)
        return stopping        
         
        
    def stoppingWordsRemover(self):
        for i in self.lst:
            if i in self.stoppingWordLoader():
                self.lst.remove(i)     
        return self.lst
    
    
    def specialCharsRemover(self):
        for i in self.phrase:
            print(i)
        
        return
    
    def suffixRemover(self,word):
        return
    
    def prefixRemover(self,word):
        return
    
    
    
    def removeIfNotExist(self):
        x=DB()
        for i in self.lst:
            if x.checkWord(i)==0:
                if x.checkWord(self.prefixRemover(i))==1:
                    self.lst[self.lst.index(i)]=self.prefixRemover(i)
                elif x.checkWord(self.suffixRemover(i))==1:
                    self.lst[self.lst.index(i)]=self.suffixRemover(i)
                else:
                    self.lst.remove(i) 
        return self.lst
