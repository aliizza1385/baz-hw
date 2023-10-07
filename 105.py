def maghsom(input1):
    Myarry = []
    for i in range(1, input1+1):
        if input1 % i == 0:
            Myarry.append(i)
    return Myarry


input1 = int(input())
for i in maghsom(input1):
    print(i)
