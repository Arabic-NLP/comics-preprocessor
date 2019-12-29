
class wordDetector:
    phrase=""
    def __init__(self):
        self.lst=[]
        self.phrase.encode('utf-8')

        
    def stoppingWordLoader(self):
        f=open("stoppingWords.txt", "r", encoding=('utf-8'))
        content= f.read().splitlines()
        stopping=[]
        for i in content:
            stopping.append(i)
        return stopping        
         
        
    def stoppingWordsRemover(self):
        for i in range(0, len(self.lst)-1):
            if self.lst[i] in self.stoppingWordLoader():
                self.lst.remove(self.lst[i])
                i=i-1
        return self.lst
    
    
    def specialCharsRemover(self):
        for i in self.phrase:
                       
            if ord(i)>32 and ord(i) <47 and ord(i)>57 and ord(i) <96:
                self.phrase.replace(i, '')                
        
        return self.phrase
    
    '''
    def suffixRemover(self,word):
        return
    
    def prefixRemover(self,word):
        return
    
    '''
    
    def removeIfNotExist(self):
        #x=DB()
        new=[]
        f=open("exist.txt", "r", encoding=('utf-8') )
        exist= f.read().splitlines()
        for i in self.lst:
            if i in exist:
                new.append(i)
                
            '''
            if x.checkWord(self.lst[i])==0:
                if x.checkWord(self.prefixRemover(self.lst[i]))==1:
                    self.lst[i]=self.prefixRemover(self.lst[i])
                elif x.checkWord(self.suffixRemover(self.lst[i]))==1:
                    self.lst[i]=self.suffixRemover(self.lst[i])
                else:
                    self.lst.remove(self.lst[i]) 
                    i=i-1 
                  '''
        self.lst=new
        
        return self.lst





x= wordDetector()

x.phrase= input ("input: ")
n=x.phrase.split()
x.lst=n
'''
f=open ("result.txt" , "w", encoding=('utf-8') )
for i in range(0,len(x.lst)):
    f.write(x.lst[i]+"\r\n")
'''


x.stoppingWordsRemover()
x.removeIfNotExist()
f=open ("result.txt" , "w", encoding=('utf-8') )

for i in range(0,len(x.lst)):
    f.write(x.lst[i]+"\r\n")
f.close()


