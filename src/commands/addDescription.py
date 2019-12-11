    
class addDescription(commandBase):
    def prepare(self):
        self.parameters=self.parameters.split(",")
        UNI= unifyLanguage()
        token= tokenizer()
        detect=wordDetector()
        x = self.parameters        
        return
    
   
    def execut(self):
        UNI.phrase=x
        x= UNI.allinone()
        x= token.splt(x)
        x= stoppingWordsRemover(x)
        x= token.formater(x)
        x= detect.removeIfNotExist(x)
        return x