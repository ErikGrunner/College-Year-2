num=input("Enter your number ")
num=int(num)
array=[0,0,0,0,0,0,0,0,0,0]
i=0
y=10
print (num)
if num >=0 :
    while num!=0 :
        if num%2 ==1 :
            print("1")
        else :
            print("0")
        array[i]=num%2
        num=num/2
        i+=1
    for i in range(0, 9):
        for y in range(9, 0):
            array[y]=array[i]
    for i in range(0, 9):
        print (array[i])
        

    
    

