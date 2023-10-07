def numberZoje():
    number = 0
    for i in range(5):
        input1 = int(input())
        if input1 % 2 == 0:
            number+=1
    return number
print(numberZoje())