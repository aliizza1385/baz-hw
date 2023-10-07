input1 = input()
Myinput = input1.split()
for i in range(len(Myinput)):
    if (ord(Myinput[i][0]) >= 97 and ord(Myinput[i][0]) <= 122):
        m = chr(ord(Myinput[i][0]) - 32)
        print(m + Myinput[i][1:], end=" ")
    else:
        print(Myinput[i], end=" ")