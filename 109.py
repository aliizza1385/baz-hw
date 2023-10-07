def faktoriel(input2):
    result = 1
    for i in range(1, input2+1):
        result *= i
    return result
result = []
input1 = int(input())
for i in range(input1):
    input2 = int(input())
    result.append(faktoriel(input2))

for i in range(len(result)):
    print(result[i])

