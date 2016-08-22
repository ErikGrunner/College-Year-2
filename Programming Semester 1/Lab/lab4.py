tup1=(20,10)

def fxn1(tup1):
    answer = tup1[0]/tup1[1]
    return answer
answer=fxn1(tup1)
print(answer)

def fxn2(tup1):
    gcd=list(tup1)
    while gcd[1]>0:
        gcd[0]=gcd[0]-gcd[1]
        if gcd[0]<gcd[1]:
            gcd[0],gcd[1]=gcd[1],gcd[0]
        answer=gcd[0]
    return answer

answer=fxn2(tup1)
print(answer)

def fxn3(tup1):
    gcd=list(tup1)
    while gcd[1]>0:
        gcd[0]=gcd[0]-gcd[1]
        if gcd[0]<gcd[1]:
            gcd[0],gcd[1]=gcd[1],gcd[0]
        answer=gcd[0]
    answer=(tup1[0]*tup1[1]/answer)
    return answer
answer=fxn3(tup1)
print(answer)



                
            
            
        
