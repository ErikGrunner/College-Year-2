fh=open("Hnr1.abc","r")
title="T:"
time="M:"
key="K:"
count=0

for line in fh:
    
    bits_of_line=line.split(" ")
    
    if (line.find(title)>=0):
        if count==0:
            print(line,end="",)
            count=1
            
    if (line.find(time)>=0):
        print(line,end="",)
        
    if (line.find(key)>=0):
        print(line,end="" '\n\n')
        count=0
    

    
