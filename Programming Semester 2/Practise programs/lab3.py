def main():
    tuple1=(1,3);
    tuple2=(3,6);
    ans2=funct_gcd(tuple1)
    print(ans2)
    ans3=funct_lcm(tuple1);
    funct__add__(tuple1,tuple2)
    funct__sub__(tuple1,tuple2)
        

def funct_gcd(tuple1):
    a=tuple1[0]
    b=tuple1[1]
    while a!=b:
        if a<b:
            a,b=b,a
        a=a-b
    print("gcd of {} is {}".format(tuple1,a))
    return a
    
def funct_lcm(tuple1):
    x=tuple1[0]
    y=tuple1[1]

    if x > y:
       greater = x
    else:
       greater = y

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
    print("LCM of {} is {}".format(tuple1,lcm))
    return lcm
    
    


def funct__add__(tuple1,tuple2):
    a1=tuple1[0]
    a2=tuple1[1]
    b1=tuple2[0]
    b2=tuple2[1]

    if a2 > b2:
       greater = a2
    else:
       greater = b2

    while(True):
       if((greater % a2 == 0) and (greater % b2 == 0)):
           lcm = greater
           break
       greater += 1
    x=lcm/a2
    y=lcm/b2

    a2=a2*x
    b2=b2*y

    a1=a1*x
    b1=b1*y

    ans=a1+b1


    print("{},{} Added together give {}/{}".format(tuple1,tuple2,ans,b2))
    




def funct__sub__(tuple1,tuple2):
    a1=tuple1[0]
    a2=tuple1[1]
    b1=tuple2[0]
    b2=tuple2[1]

    if a2 > b2:
       greater = a2
    else:
       greater = b2

    while(True):
       if((greater % a2 == 0) and (greater % b2 == 0)):
           lcm = greater
           break
       greater += 1
    x=lcm/a2
    y=lcm/b2

    a2=a2*x
    b2=b2*y

    a1=a1*x
    b1=b1*y

    ans=b1-a1


    print("{},{} Added together give {}/{}".format(tuple1,tuple2,ans,b2))

main()
    
