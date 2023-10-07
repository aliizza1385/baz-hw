Myarry = []
for i in range(10):
    input2 = int(input())
    Mybool = True
    for j in range(2, input2):
        if input2 % j == 0:
            Mybool = False
    if Mybool == False:
        Myarry.append(input2)
for i in range(len(Myarry)):
    print(Myarry[i])