import sys 
class tokenizer:
    phrase= ""
    lst=[]
    
   
    def __init__(self):
        self.lst=[]
        self.phrase.encode('utf-8')
        
    def numloader(self):
        f=open("numbers.txt", "r", encoding=('utf-8') )
        content= f.read().splitlines()
        nums=[]
        for i in content:
            nums.append(i)
        f.close()
        return nums
    
    
    def splitter(self):
        self.lst= self.phrase.split()
        return self.lst
    
    
    def testAppendBefore(self, word):
        #x=DB()
        index= self.lst.index(word)
        f=open("data.txt", "r", encoding=('utf-8') )
        data= f.read().splitlines()
        '''
        if x.checkWord(self.lst[index-1]+word)==1:
            return 1
        else:
            return 0
        '''
        if index==0:
            return 0
        elif self.lst[index-1]+word in data:
            return 1
        else:
            return 0
        
    def testAppendAfter(self,word):
        #x=DB()
        index= self.lst.index(word)
        f=open("data.txt", "r", encoding=('utf-8') )
        data= f.read().splitlines()
                
        '''
        if x.checkWord(word+self.lst[index+1])==1:
            return 1
        else:
            return 0        
        '''
        if index==len(self.lst):
            return 0
        elif word+self.lst[index+1] in data:
            return 1
        else:
            return 0
        
    
    def formatter(self): 
        for i in range (0,len(self.lst)-1):                      
            if self.lst[i] in self.numloader():
                if self.testAppendBefore(self.lst[i])==1:
                    self.lst[i-1]=self.lst[i-1]+self.lst[i]
                    self.lst.remove(self.lst[i])
                    i=i-1
                    
                elif self.testAppendAfter(self.lst[i])==1:
                    self.lst[i+1]=self.lst[i]+self.lst[i+1]
                    self.lst.remove(self.lst[i])
                    i=i-1                    
        return self.lst 
     
    
    
    '''    
x= tokenizer()
x.phrase = input("Enter the phrase: ") 
x.splitter()
x.formatter()

f=open ("result.txt" , "w", encoding=('utf-8') )


for i in x.numloader():
    f.write(i)
f.close()


f=open ("result.txt" , "w", encoding=('utf-8') )

for i in range(0,len(x.lst)):
    f.write(x.lst[i]+"\r\n")
f.close()

'''

