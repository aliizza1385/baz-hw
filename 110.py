def Big():
    inputs=[]
    input1 = int(input())
    for i in range(input1):
        input2 = int(input())
        inputs.append(input2)
    sort = sorted(inputs , reverse=True)
    for i in sort:
        print(i)
Big()
