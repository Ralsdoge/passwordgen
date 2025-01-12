import random
MLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Mnumbers = ['1','2','3','4','5','6','7','8','9','0']
Mspecial = ['!','@','#', '$','%','^','&','*','-','_','=','+',';',':','"',"'",',','.','<','>','/','?','`','~']

def PassGeneratorSampl(alp,num,spe,Length,restricted=None):#alphebetical,numerical,special,total#Input weights 
    passtring = ''
    tot = alp + num + spe 
    genList = []
    Lower = MLower
    Upper = MUpper
    numbers = Mnumbers
    special = Mspecial
    low =0
    upp=0
    numb=0
    spec=0
     ##Restricted filteromg
    if restricted == None:
        pass
    else:
        restricted = str(restricted) 
        print(restricted)
        restricted = restricted[:len(restricted)-1]
        print(restricted)
        print(str(restricted).split(','))
        restricted = str(restricted).split(',')
        for p in range(len(restricted)):
            Lower = [i for i in Lower if i != restricted[p]]
            Upper = [i for i in Upper if i != restricted[p]]
            numbers = [i for i in numbers if i != restricted[p]]
            special = [i for i in special if i != restricted[p]]
    for i in range(0,int(Length),1):
        Choice1 = random.randint(1,tot+1)
        if Choice1 -1 <= alp and alp != 0:#alphebetical
            if random.randint(0,1) == 0:
                genList.append('a')
                low+=1
            else:
                genList.append('A')
                upp+=1
        elif Choice1 -1 <= alp+num and num != 0:#numerical
            genList.append('0')
            numb+=1
        elif Choice1 -1 <= alp+num+spe and spe != 0:#Special
            genList.append(':')
            spec+=1
        else:
            print('over')
    UpperL = len(Upper)
    LowerL = len(Lower)
    numbersL = len(numbers)
    specialL = len(special)
    
    if upp > UpperL:#26 characters #Uppercase
        uppercase = random.sample(Upper,UpperL)
        upp = upp-UpperL
        while True:
            if upp >UpperL:
                uppercase += random.sample(Upper,UpperL)
                upp = upp-UpperL
            else:  
                uppercase += random.sample(Upper,upp)
                break
    else:
        uppercase = random.sample(Upper,upp)
    
    if low > LowerL:#26 characters #Lowercase
        lowercase = random.sample(Lower,LowerL)
        low = low-LowerL
        while True:
            if low >LowerL:
                lowercase += random.sample(Lower,LowerL)
                low = low-LowerL
            else:  
                lowercase += random.sample(Lower,low)
                break
    else:
        lowercase = random.sample(Lower,low)

    if numb > numbersL: #10 characters #Number
        numerical = random.sample(numbers,numbersL)
        numb = numb-numbersL
        while True:
            if numb >numbersL:
                numerical += random.sample(numbers,numbersL)
                numb = numb-numbersL
            else:  
                numerical += random.sample(numbers,numb)
                break    
    else:
        numerical = random.sample(numbers,numb)

    if spec > specialL:#24 characters #special
        specialchar = random.sample(special,specialL)
        spec = spec-specialL
        while True:
            if spec >specialL:
                specialchar += random.sample(special,specialL)
                spec = spec-specialL
            else:  
                specialchar += random.sample(special,spec)
                break
    else:
        specialchar = random.sample(special,spec)
    
    for k in range(0, len(genList)):
        if genList[k] == 'a':
            passtring += lowercase[0]
            lowercase.pop(0) 
        elif genList[k] == 'A':
            passtring += uppercase[0]
            uppercase.pop(0) 
        elif genList[k] == '0':
            passtring += numerical[0]
            numerical.pop(0) 
        elif genList[k] == ':':
            passtring += specialchar[0]
            specialchar.pop(0) 
        else: 
            print('Wth')

    
    return(passtring)
    

def PassGenerator(alp,num,spe,Length):#alphebetical,numerical,special,total#Input weights 
    passtring = ''
    tot = alp + num + spe 
    for i in range(0,int(Length/2),1):
        Choice1 = random.randint(1,tot+1)
        if Choice1 -1 <= alp and alp != 0:
            if random.randint(0,1) == 0:
                passtring += MLower[random.randint(0,len(MLower))-1]
            else:
                passtring += MUpper[random.randint(0,len(MUpper))-1]
        elif Choice1 -1 <= alp+num and num != 0:
            passtring += Mnumbers[random.randint(0,len(Mnumbers)-1)]
        elif Choice1 -1 <= alp+num+spe and spe != 0:
            passtring += Mspecial[random.randint(0,len(Mspecial)-1)]
        else:
            print('over')
        if Choice1 -1 <= alp and alp != 0:
            if random.randint(0,1) == 0:
                passtring += MLower[random.randint(0,len(MLower))-1]
            else:
                passtring += MUpper[random.randint(0,len(MUpper))-1]
        elif Choice1 -1 <= alp+num and num != 0:
            passtring += Mnumbers[random.randint(0,len(Mnumbers)-1)]
        elif Choice1 -1 <= alp+num+spe and spe != 0:
            passtring += Mspecial[random.randint(0,len(Mspecial)-1)]
        else:
            print('over')
    return(passtring)