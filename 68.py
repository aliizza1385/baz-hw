input1 = input()
count = 0
for i in range(len(input1)):
    if input1[i] == '0':
        count+=1
print(count)