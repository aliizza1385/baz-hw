def Getinput():
    count = 0
    input1 = int(input())
    for i in range(input1):
        input2 = int(input())
        Mybool=True
        for j in range(2,input2):
            if(input2 % j == 0):
                Mybool = False
        if Mybool:
            count+=1
            
    return count

print(Getinput())