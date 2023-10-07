input1 = input()
for i in range(len(input1)):
    if(ord(input1[i]) >= 97 and ord(input1[i]) <= 122):
        l = chr((ord(input1[i])) - 32)
        print(l, end="")
    else:
        print(input1[i], end="")
