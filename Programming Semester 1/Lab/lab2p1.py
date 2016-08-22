str1=input("Enter in plain text to be encrypted or decrypted\n")

str2=input("Do you wish to encrypt or decrypt the string 1/2  \n")

str4=''

if str2 == '1':
    
    for i in range(0,len(str1)):
        
        str3=chr(ord(str1[i])+1)
        
        print(str1[i],"------>",str3)
        
        str4=str4+str3

    str4=str4[::-1]
    
    print(str4)

else:
    
    for i in range(0,len(str1)):
        
        str3=chr(ord(str1[i])-1)
        
        print(str1[i],"------>",str3)
        
        str4=str4+str3

    str4=str4[::-1]

    print(str4)
        
        
    
    
