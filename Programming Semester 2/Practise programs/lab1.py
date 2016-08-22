#Author Ciaran O'Loughlin
#Lab 1 semester 2 year 2
import time

class clock(object):
    def __init__(self,x=0):
        self.sec=x
        self.min=x
        self.hour=x
        self.day=x

    def tick(self):
        time.sleep(1)
        if self.sec==59:
            self.sec=0
            
            if(self.min==59):
                self.min=0
                if self.hour==23:
                    self.hour=0
                    if self.day==365:
                        self.day=0
                    else:
                        self.day+=1
                else:
                    self.hour+=1
            else:
                self.min+=1
        else:
            self.sec+=1
             
    def display(self):
        print("%d:%d:%d:%d" % (self.day, self.hour, self.min, self.sec))

    def __str__(self):
        return "%2d:%2d:%2d:%2d" % (self.day, self.hour, self.min, self.sec)

x=clock()
print(x)
while(1==1):
    x.tick()
    print(x)
        
