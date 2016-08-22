'''Author Ciarán O'Loughlin, Completion date:27/11/2014
Assignment 1
Object orientated programming
Program description:
This program downloads data from the internet and saves it as a file. It then scans half the data taking averages from each of the fields and changing the discrete
data to numerical data for example changing unemployed to .07 . It then goes on to test the other half of data with the data it has gathered and makes assumptions
about whether the person will earn over or under 50K and prints out the accuracy to which it makes these predictions
'''

#Test case fuction
#This function tests the sceond half of the data with the data gathered from all the other functions to predict whether a person will earn over or under 50K
#It then produces an accuracy rating for how accuratly it predicts people incomes
def Test():
    k=[]
    workclass=[]
    sex=[]
    marital_status=[]
    occupation=[]
    race=[]
    #creates the lists to hold the data
    
    int_i=0
    c=0
    d=0
    f=0


    file= open('text.txt', 'r')#opens the file containing the data
    
    for line in file:#for loop to go through each line of the file
        stat=0
        if int_i>(num+1):#to go through only the second half of the file
            line.strip()#strips the line of whitetspace characthers
            fields=line.split(", ")#splits the line into 14 fields and stores them in the variable fields


            try:#try excemption to make sure the data is valid
                age=int(fields[0])
                k.append(fields[14])
                educ=int(fields[4])
                cap_g=int(fields[10])
                cap_l=int(fields[11])
                hours=int(fields[12])
                workclass.append(fields[1])
                sex.append(fields[9])
                marital_status.append(fields[5])
                occupation.append(fields[6])
                race.append(fields[8])
                
            except ValueError as e:#if the data is corrupt the program will skip it
                continue

            #This part of the code test the data training set I have created earlier in my program
            #this compares the average age against the current age
            #if its greater than statistically your going to earn over 50K, below and your going to be earning less than 50K
            if average<age:
                stat=stat+1#adds 1 to stat if the cureent age is above the average
            elif average>=age:
                stat=stat-1#takes 1 away from stat if the current age is less than the average

            #compares the education value   
            if average2<educ:
                stat=stat+1
            elif average2>=educ:
                stat=stat-1

            #compares the capital gain values    
            if average3<cap_g:
                stat=stat+1
            elif average3>=cap_g:
                stat=stat-1

            #compares the capital loss values     
            if average4<cap_l:
                stat=stat+1
            elif average4>=cap_l:
                stat=stat-1

            #compares the number of hours they've worked      
            if average5<hours:
                stat=stat+1
            elif average5>=hours:
                stat=stat-1

            #compares the values I created for the jobs type and compares them against the average value  
            if workclass[c]=='State-gov':
                if average6<work_1:
                    stat=stat+1
                elif average6>=work_1:
                    stat=stat-1
            if workclass[c]=='Private':
                if average6<work_2:
                    stat=stat+1
                elif average6>=work_2:
                    stat=stat-1
            if workclass[c]=='Self-emp-not-inc':
                if average6<work_3:
                    stat=stat+1
                elif average6>=work_3:
                    stat=stat-1
            if workclass[c]=='Self-emp-inc':
                if average6<work_4:
                    stat=stat+1
                elif average6>=work_4:
                    stat=stat-1
            if workclass[c]=='Federal-gov':
                if average6<work_5:
                    stat=stat+1
                elif average6>=work_5:
                    stat=stat-1       
            if workclass[c]=='Local-gov':
                if average6<work_6:
                    stat=stat+1
                elif average6>=work_6:
                    stat=stat-1
            if workclass[c]=='Without-pay':
                if average6<work_7:
                    stat=stat+1
                elif average6>=work_7:
                    stat=stat-1
            if workclass[c]=='Never-worked':
                if average6<work_8:
                    stat=stat+1
                elif average6>=work_8:
                    stat=stat-1

            #does the same as previously exept fo sex
            if sex[c]=='Male':
                if average7<male:
                    stat=stat+1
                elif average7>=male:
                    stat=stat-1
            if sex[c]=='Female':
                if average7<female:
                    stat=stat+1
                elif average7>=female:
                    stat=stat-1

            #does the same as previously exept for the person relationship
            if marital_status[c]=='Married-civ-spouse':
                if average8<relationship_1:
                    stat=stat+1
                elif average8>=relationship_1:
                    stat=stat-1
            if marital_status[c]=='Divorced':
                if average8<relationship_2:
                    stat=stat+1
                elif average8>=relationship_2:
                    stat=stat-1
            if marital_status[c]=='Never-married':
                if average8<relationship_3:
                    stat=stat+1
                elif average8>=relationship_3:
                    stat=stat-1
            if marital_status[c]=='Separated':
                if average8<relationship_4:
                    stat=stat+1
                elif average8>=relationship_4:
                    stat=stat-1
            if marital_status[c]=='Widowed':
                if average8<relationship_5:
                    stat=stat+1
                elif average8>=relationship_5:
                    stat=stat-1
            if marital_status[c]=='Married-spouse-absent':
                if average8<relationship_6:
                    stat=stat+1
                elif average8>=relationship_6:
                    stat=stat-1
            if marital_status[c]=='Married-AF-spouse':
                if average8<relationship_7:
                    stat=stat+1
                elif average8>=relationship_7:
                    stat=stat-1

            #does the same as previously exept for the fact that it checks the persons specific job
            if occupation[c]=='Tech-support':
                if average9<job_1:
                    stat=stat+1
                elif average9>=job_1:
                    stat=stat-1
            if occupation[c]=='Craft-repair':
                if average9<job_2:
                    stat=stat+1
                elif average9>=job_2:
                    stat=stat-1
            if occupation[c]=='Other-service':
                if average9<job_3:
                    stat=stat+1
                elif average9>=job_3:
                    stat=stat-1
            if occupation[c]=='Sales':
                if average9<job_4:
                    stat=stat+1
                elif average9>=job_4:
                    stat=stat-1
            if occupation[c]=='Exec-managerial':
                if average9<job_5:
                    stat=stat+1
                elif average9>=job_5:
                    stat=stat-1
            if occupation[c]=='Prof-specialty':
                if average9<job_6:
                    stat=stat+1
                elif average9>=job_6:
                    stat=stat-1
            if occupation[c]=='Handlers-cleaners':
                if average9<job_7:
                    stat=stat+1
                elif average9>=job_7:
                    stat=stat-1
            if occupation[c]=='Machine-op-inspct':
                if average9<job_8:
                    stat=stat+1
                elif average9>=job_8:
                    stat=stat-1
            if occupation[c]=='Adm-clerical':
                if average9<job_9:
                    stat=stat+1
                elif average9>=job_9:
                    stat=stat-1
            if occupation[c]=='Farming-fishing':
                if average9<job_10:
                    stat=stat+1
                elif average9>=job_10:
                    stat=stat-1
            if occupation[c]=='Transport-moving':
                if average9<job_11:
                    stat=stat+1
                elif average9>=job_11:
                    stat=stat-1
            if occupation[c]=='Priv-house-serv':
                if average9<job_12:
                    stat=stat+1
                elif average9>=job_12:
                    stat=stat-1
            if occupation[c]=='Protective-serv':
                if average9<job_13:
                    stat=stat+1
                elif average9>=job_13:
                    stat=stat-1
            if occupation[c]=='Armed-Forces':
                if average9<job_14:
                    stat=stat+1
                elif average9>=job_14:
                    stat=stat-1

            
            #does the same as previously exept for the person race
            if race[c]=='White':
                if average10<race_1:
                    stat=stat+1
                elif average10>=race_1:
                    stat=stat-1
            if race[c]=='Asian-Pac-Islander':
                if average10<race_2:
                    stat=stat+1
                elif average10>=race_2:
                    stat=stat-1
            if race[c]=='Amer-Indian-Eskimo':
                if average10<race_3:
                    stat=stat+1
                elif average10>=race_3:
                    stat=stat-1
            if race[c]=='Other':
                if average10<race_4:
                    stat=stat+1
                elif average10>=race_4:
                    stat=stat-1
            if race[c]=='Black':
                if average10<race_5:
                    stat=stat+1
                elif average10>=race_5:
                    stat=stat-1
            #if stat is above 0 the statistically you will earn over 50K, this part checks how many correct predictions i got and how many i got wrong
            if stat>0:
                if k[c]=='>50K\n':
                    d=d+1#counter for if i got it right
                else:
                    f=f+1#counter for if i got it wrong
            #if stat is below 0 statistically your going to be earning less than 50K
            elif stat<=0:
                if k[c]=='<=50K\n':
                    d=d+1
                else:
                    f=f+1


            c=c+1    
        int_i=int_i+1
    print('Got right',d)
    print('Got wrong',f)
    #prints the percentage of predictions i got right
    print((d/c)*100,'%')
            

                       
#Race function
#This function creates numeric values for each of the races included in the training data
#It then also creates a midpoint average for all these values
def Race():
    k=[]
    fields=[]
    race=[]

    
    a=0
    b=0
    c=0
    d=0
    f=0
    g=0
    h=0
    i=0
    j=0
    l=0
    m=0
    n=0
    #creates numerical values for all the races so that they can be called in the test() function
    global race_1
    global race_2
    global race_3
    global race_4
    global race_5
    
    int_i=0
    #global average for the average of the races values
    global average10
    file= open('text.txt', 'r')

    
    for line in file:
        if int_i<num:
            line.strip()
            fields=line.split(", ")


            try:
                k.append(fields[14])
                race.append(fields[8])
                d=d+1
        
            except ValueError as e:
                continue


            #This part of the code is going through the training set of data creating the averages to be used in the test function
            if race[c]=='White':
                if k[c] == '<=50K\n':
                    a=a+1
                elif k[c]== '>50K\n':
                    b=b+1
            if race[c]=='Asian-Pac-Islander':
                if k[c] == '<=50K\n':
                    f=f+1
                elif k[c]== '>50K\n':
                    g=g+1
            if race[c]=='Amer-Indian-Eskimo':
                if k[c] == '<=50K\n':
                    h=h+1
                elif k[c]== '>50K\n':
                    i=i+1
            if race[c]=='Other':
                if k[c] == '<=50K\n':
                    j=j+1
                elif k[c]== '>50K\n':
                    l=l+1
            if race[c]=='Black':
                if k[c] == '<=50K\n':
                    m=m+1
                elif k[c]== '>50K\n':
                    n=n+1

                
            c=c+1
            int_i=int_i+1
        else:
            continue
    #The numerical values are created by counting up all the occurences of that particular race and dividing by the total number of entries and then dividing by 2
    race_1=((a/d)+(b/d))/2# Creating the numerical values for each of the races
    race_2=((f/d)+(g/d))/2
    race_3=((h/d)+(i/d))/2
    race_4=((j/d)+(l/d))/2
    race_5=((m/d)+(n/d))/2
    #The average is made by adding up all the values for above 50K(divided by the total number of entries)and then adding that to the sum of all the values for below
    #50K. This is then divided by 2 and this now the average for all values
    average10=((((a/d)+(f/d)+(h/d)+(j/d)+(m/d)/5)+((b/d)+(g/d)+(i/d)+(l/d)+(n/d))/5))/2
    print('Race weighting', average10)

#Occupation function
#This function creates numeric values for each of the job types included in the training data
#It then also creates a midpoint average for all these values
def Occupation():
    k=[]
    fields=[]
    occupation=[]
    a=0
    b=0
    
    c=0
    d=0
    
    f=0
    g=0
    
    h=0
    i=0
    
    j=0
    l=0
    
    m=0
    n=0
    
    p=0
    q=0
    
    r=0
    s=0
    
    t=0
    u=0

    v=0
    w=0

    x=0
    y=0

    occ_a2=0
    occ_b2=0

    occ_c2=0
    occ_d2=0

    occ_e2=0
    occ_f2=0

    occ_g2=0
    occ_h2=0

    occ_average1=0
    occ_average2=0

    int_i=0
#Creates all the global values for the job types that ill be calling in the test() function
    global job_1
    global job_2
    global job_3
    global job_4
    global job_5
    global job_6
    global job_7
    global job_8
    global job_9
    global job_10
    global job_11
    global job_12
    global job_13
    global job_14

    
#creates global average for all the job type values
    global average9

    file= open('text.txt', 'r')

    
    for line in file:
        if int_i<num:
            line.strip()
            fields=line.split(", ")


            try:
                k.append(fields[14])
                occupation.append(fields[6])#This puts all the jobs into a list called occupation
                d=d+1
        
            except ValueError as e:
                continue


            #This part of the code is going through the training set of data creating the averages to be used in the test function
            if occupation[c]=='Tech-support':
                if k[c] == '<=50K\n':
                    a=a+1
                elif k[c]== '>50K\n':
                    b=b+1
            if occupation[c]=='Craft-repair':
                if k[c] == '<=50K\n':
                    f=f+1
                elif k[c]== '>50K\n':
                    g=g+1
            if occupation[c]=='Other-service':
                if k[c] == '<=50K\n':
                    h=h+1
                elif k[c]== '>50K\n':
                    i=i+1
            if occupation[c]=='Sales':
                if k[c] == '<=50K\n':
                    j=j+1
                elif k[c]== '>50K\n':
                    l=l+1
            if occupation[c]=='Exec-managerial':
                if k[c] == '<=50K\n':
                    m=m+1
                elif k[c]== '>50K\n':
                    n=n+1
            if occupation[c]=='Prof-specialty':
                if k[c] == '<=50K\n':
                    p=p+1
                elif k[c]== '>50K\n':
                    q=q+1
            if occupation[c]=='Handlers-cleaners':
                if k[c] == '<=50K\n':
                    r=r+1
                elif k[c]== '>50K\n':
                    s=s+1
            if occupation[c]=='Machine-op-inspct':
                if k[c] == '<=50K\n':
                    t=t+1
                elif k[c]== '>50K\n':
                    u=u+1
            if occupation[c]=='Adm-clerical':
                if k[c] == '<=50K\n':
                    v=v+1
                elif k[c]== '>50K\n':
                    w=w+1
            if occupation[c]=='Farming-fishing':
                if k[c] == '<=50K\n':
                    x=x+1
                elif k[c]== '>50K\n':
                    y=y+1
            if occupation[c]=='Transport-moving':
                if k[c] == '<=50K\n':
                    occ_a2=occ_a2+1
                elif k[c]== '>50K\n':
                    occ_b2=occ_b2+1
            if occupation[c]=='Priv-house-serv':
                if k[c] == '<=50K\n':
                    occ_c2=occ_c2+1
                elif k[c]== '>50K\n':
                    occ_d2=occ_d2+1
            if occupation[c]=='Protective-serv':
                if k[c] == '<=50K\n':
                    occ_e2=occ_e2+1
                elif k[c]== '>50K\n':
                    occ_f2=occ_f2+1
            if occupation[c]=='Armed-Forces':
                if k[c] == '<=50K\n':
                    occ_g2=occ_g2+1
                elif k[c]== '>50K\n':
                    occ_h2=occ_h2+1
            c=c+1
            int_i=int_i+1
    #The numerical values are created by counting up all the occurences of that particular job,adding both the values for above 50K and below 50K
    #and dividing by the total number of entries then dividing by 2
    job_1=((a/d)+(b/d))/2
    job_2=((f/d)+(g/d))/2
    job_3=((h/d)+(i/d))/2
    job_4=((j/d)+(l/d))/2
    job_5=((m/d)+(n/d))/2
    job_6=((p/d)+(q/d))/2
    job_7=((r/d)+(s/d))/2
    job_8=((t/d)+(u/d))/2
    job_9=((v/d)+(w/d))/2
    job_10=((x/d)+(y/d))/2
    job_11=((occ_a2/d)+(occ_b2/d))/2
    job_12=((occ_c2/d)+(occ_d2/d))/2
    job_13=((occ_e2/d)+(occ_f2/d))/2
    job_14=((occ_g2/d)+(occ_h2/d))/2

    #I split this here because it was too long to do within just creating average 9
    occ_average1=(((a/d)+(f/d)+(h/d)+(j/d)+(m/d)+(p/d)+(r/d)+(t/d)+(v/d)+(x/d)+(occ_a2/d)+(occ_c2/d)+(occ_e2/d)+(occ_g2/d))/14)
    occ_average2=(((b/d)+(g/d)+(i/d)+(l/d)+(n/d)+(q/d)+(s/d)+(u/d)+(w/d)+(y/d)+(occ_b2/d)+(occ_d2/d)+(occ_f2/d)+(occ_h2/d))/14)
    average9=(occ_average1+occ_average2)/2#this the creates the average for all the numeric values of the job types
    
    print('Occupation weighting', average9)

    
#Marital_status() function
#This function creates numeric values for each of the relationship types included in the training data
#It then also creates a midpoint average for all these values
def Marital_Status():
    
    k=[]
    fields=[]
    marital_status=[]
    a=0
    b=0
    c=0
    d=0
    f=0
    g=0
    h=0
    i=0
    j=0
    l=0
    m=0
    n=0
    p=0
    q=0
    r=0
    s=0

    #Creating the global varibals which will hold the numeric values for the relationship types
    global relationship_1
    global relationship_2
    global relationship_3
    global relationship_4
    global relationship_5
    global relationship_6
    global relationship_7

    #creating the global varibal that will hold the average of all the relationship types
    global average8

    int_i=0

    file= open('text.txt', 'r')

    
    for line in file:
        if int_i<num:
            line.strip()
            fields=line.split(", ")


            try:
                k.append(fields[14])
                marital_status.append(fields[5])#takes all the relationships that occur in the training set and places them into a list
                d=d+1
        
            except ValueError as e:
                continue


            #This part of the code is going through the training set of data creating the averages to be used in the test function
            if marital_status[c]=='Married-civ-spouse':
                if k[c] == '<=50K\n':
                    a=a+1
                elif k[c]== '>50K\n':
                    b=b+1
            if marital_status[c]=='Divorced':
                if k[c] == '<=50K\n':
                    f=f+1
                elif k[c]== '>50K\n':
                    g=g+1
            if marital_status[c]=='Never-married':
                if k[c] == '<=50K\n':
                    h=h+1
                elif k[c]== '>50K\n':
                    i=i+1
            if marital_status[c]=='Separated':
                if k[c] == '<=50K\n':
                    j=j+1
                elif k[c]== '>50K\n':
                    l=l+1
            if marital_status[c]=='Widowed':
                if k[c] == '<=50K\n':
                    m=m+1
                elif k[c]== '>50K\n':
                    n=n+1
            if marital_status[c]=='Married-spouse-absent':
                if k[c] == '<=50K\n':
                    p=p+1
                elif k[c]== '>50K\n':
                    q=q+1
            if marital_status[c]=='Married-AF-spouse':
                if k[c] == '<=50K\n':
                    r=r+1
                elif k[c]== '>50K\n':
                    s=s+1
            c=c+1
            int_i=int_i+1

        
    #The numerical values are created by counting up all the occurences of that particular Relationship type,adding both the values for above 50K and below 50K
    #and dividing by the total number of entries, then dividing by 2
    relationship_1=((a/d)+(b/d))/2
    relationship_2=((f/d)+(g/d))/2
    relationship_3=((h/d)+(i/d))/2
    relationship_4=((j/d)+(l/d))/2
    relationship_5=((m/d)+(n/d))/2
    relationship_6=((p/d)+(q/d))/2
    relationship_7=((r/d)+(s/d))/2

    #this creates an average value for all the relationships    
    average8=((((a/d)+(f/d)+(h/d)+(j/d)+(m/d)+(p/d)+(r/d))/7)+(((b/d)+(g/d)+(i/d)+(l/d)+(n/d)+(q/d)+(s/d))/7))/2
    print('Marital status weighting', average8)


#Sex() function
#This function creates numeric values for male and female in the training data
#It then also creates a midpoint average for these values    
def Sex():
    k=[]
    fields=[]
    sex=[]
    a=0
    b=0
    c=0
    d=0
    f=0
    g=0
    global average7
    i=0
    #Creating the global varibals which will hold the numeric values for the2 sex types
    global male
    global female


    file= open('text.txt', 'r')

    
    for line in file:
        if i<num:
            line.strip()
            fields=line.split(", ")
  


            try:
                k.append(fields[14])
                sex.append(fields[9])#puts either male or female into this list from the file text.txt
                d=d+1

            except ValueError as e:
                continue

            #This part of the code is going through the training set of data creating the averages to be used in the test function
            if sex[c]=='Male':
                if k[c] == '<=50K\n':
                    a=a+1
                elif k[c]== '>50K\n':
                    b=b+1
            if sex[c]=='Female':
                if k[c] == '<=50K\n':
                    f=f+1
                elif k[c]== '>50K\n':
                    g=g+1
            c=c+1
            i=i+1
        else:
            continue

    #The numerical values are created by counting up all the occurences of that particular sex,adding both the values for above 50K and below 50K
    #and dividing by the total number of entries, then dividing by 2
    male=((a/d)+(b/d))/2
    female=((f/d)+(g/d))/2

    #this then creates an average for the two values 
    average7=((((a/d)+(f/d))/2)+(((b/d)+(g/d))/2))/2
    print('Sex weighting', average7)
         


#Workclass() function
#This function creates numeric values for each of the workclass types included in the training data
#It then also creates a midpoint average for all these values
def Workclass():
    i=0
    k=[]
    fields=[]
    workclass=[]
    a=0
    b=0
    c=0
    d=0
    f=0
    g=0
    h=0
    i=0
    j=0
    l=0
    m=0
    n=0
    p=0
    q=0
    r=0
    s=0
    t=0
    u=0
    global average6
    #creating the global varibal that will hold the average of all the relationship types
    global work_1
    global work_2
    global work_3
    global work_4
    global work_5
    global work_6
    global work_7
    global work_8

    file= open('text.txt', 'r')

    
    for line in file:
        if i<num:
            line.strip()
            fields=line.split(", ")


            try:

                k.append(fields[14])#this puts the last field which contains the persons income into a list
                workclass.append(fields[1])#this puts the workclass type from the file into a list
                d=d+1
        
            except ValueError as e:
                continue


            #This part of the code is going through the training set of data creating the averages to be used in the test function
            if workclass[c]=='State-gov':
                if k[c] == '<=50K\n':
                    a=a+1
                elif k[c]== '>50K\n':
                    b=b+1
            if workclass[c]=='Private':
                if k[c] == '<=50K\n':
                    f=f+1
                elif k[c]== '>50K\n':
                    g=g+1
            if workclass[c]=='Self-emp-not-inc':
                if k[c] == '<=50K\n':
                    h=h+1
                elif k[c]== '>50K\n':
                    i=i+1
            if workclass[c]=='Self-emp-inc':
                if k[c] == '<=50K\n':
                    j=j+1
                elif k[c]== '>50K\n':
                    l=l+1
            if workclass[c]=='Federal-gov':
                if k[c] == '<=50K\n':
                    m=m+1
                elif k[c]== '>50K\n':
                    n=n+1
            if workclass[c]=='Local-gov':
                if k[c] == '<=50K\n':
                    p=p+1
                elif k[c]== '>50K\n':
                    q=q+1
            if workclass[c]=='Without-pay':
                if k[c] == '<=50K\n':
                    r=r+1
                elif k[c]== '>50K\n':
                    s=s+1
            if workclass[c]=='Never-worked':
                if k[c] == '<=50K\n':
                    t=t+1
                elif k[c]== '>50K\n':
                    u=u+1
            c=c+1
            i=i+1
            
        else:
            continue
    #The numerical values are created by counting up all the occurences of that particular workclass,adding both the values for above 50K and below 50K
    #and dividing by the total number of entries then dividing by 2
    work_1=((a/d)+(b/d))/2
    work_2=((f/d)+(g/d))/2
    work_3=((h/d)+(i/d))/2
    work_4=((j/d)+(l/d))/2
    work_5=((m/d)+(n/d))/2
    work_6=((p/d)+(q/d))/2
    work_7=((r/d)+(s/d))/2
    work_8=((t/d)+(u/d))/2

    #this creates an average value for all the workclass types
    average6=((((a/d)+(f/d)+(h/d)+(j/d)+(m/d)+(p/d)+(r/d)+(t/d))/8)+(((b/d)+(g/d)+(i/d)+(l/d)+(n/d)+(q/d)+(s/d)+(u/d))/8))/2
    print('Workclass weighting', average6)





#download function
#This function downloads the file and saves it as a file called text.txt
def Download():
    from urllib.request import urlretrieve
    html = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    urlretrieve(html,"text.txt")
    
#Main()
#This is the main function where all other functions are called
#this functions main concern is to create values for fields that already had numeric values eg age
#after this it calls all the previous functions and then finally tests out its training data in the test function
def Main():
    k=[]
    fields=[]
    age=[]
    workclass=[]

    age_above=0#age with income above 50K
    age_below=0#age with income below 50K
    education_number_above=0
    education_number_below=0
    capital_gain_above=0
    capital_gain_below=0
    capital_loss_above=0
    capital_loss_below=0
    hours_above=0
    hours_below=0

    
    a=0
    b=0
    c=0
    i=0

    #num is the number of entries i will scan in my training set
    global num
    num=15000

    #global varibals for the averages of the numeric values
    global average
    global average2
    global average3
    global average4
    global average5
    
    file= open('text.txt', 'r')

    
    for line in file:
        if i<=num:#this makes sure that it only scans up to the number the number of entries i want scanned 
            
            line.strip()#strips the file of all blank space charachters
            fields=line.split(", ")#splits the file into 14 seperate fields 



            try:
                n=int(fields[0])#puts the 0 field into n, that field contains the age of the person
                educ=int(fields[4])#puts the 4 field into educ, which is a person number of years in education
                cap_g=int(fields[10])#puts the 10 field which contains capital gain into cap_g
                cap_l=int(fields[11])#puts the 11 field which contains capital loss into cap_l
                hours=int(fields[12])#puts the 12 field which contain the nuimber of hours the person does per week into hours 
                k.append(fields[14])#puts the level of income into k


            except ValueError as e:
                continue


        
            if k[c] == '>50K\n':#This part essentially just gets the values of all thoes above 50K
                age_above=age_above+n
                education_number_above=education_number_above+educ
                capital_gain_above=capital_gain_above+cap_g
                capital_loss_above=capital_loss_above+cap_l
                hours_above=hours_above+hours
                a=a+1
            
            elif k[c]== '<=50K\n':#This part essentially just gets the values of all thoes below 50K
                age_below=age_below+n
                education_number_below=education_number_below+educ
                capital_gain_below=capital_gain_below+cap_g
                capital_loss_below=capital_loss_below+cap_l
                hours_below=hours_below+hours
                b=b+1   
            
            c=c+1
        else:
            continue
        
    #This then gets the aVERAGE OF THE VALUES ABOVE 50k
    capital_loss_above=capital_loss_above/a
    capital_gain_above=capital_gain_above/a
    education_number_above=education_number_above/a
    hours_above=hours_above/a
    age_above=age_above/a

    #this then gets the values of all thoes below 50K
    age_below=age_below/b
    education_number_below=education_number_below/b
    capital_gain_below=capital_gain_below/b
    capital_loss_below=capital_loss_below/b
    hours_below=hours_below/b

    #then the average of the two above values is got and this is created as a global midpoint
    average=(age_above+age_below)/2
    average2=(education_number_above+education_number_below)/2
    average3=(capital_gain_above+capital_gain_below)/2
    average4=(capital_loss_above+capital_loss_below)/2
    average5=(hours_above+hours_below)/2




    print('Age' ,int(average))
    print('Education number' ,int(average2))
    print('Capital gain' ,int(average3))
    print('Capital Loss' ,int(average4))
    print('Hours' ,int(average5))

    #this then calls all the other functions in secuential order
    Workclass()
    Sex()
    Marital_Status()
    Occupation()
    Race()
    Test()

    file.close()#closes the file



#this basically checks if the file text.txt exits and if it does the program starts otherwise it downloads the file and then starts the program
try:
    f=open('text.txt','r')
    Main()
    f.close()
          
except IOError:
    print ('File downloading ')
    Download()
    f=open('text.txt','r')
    Main()
    f.close()
