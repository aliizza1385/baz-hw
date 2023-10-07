def faktoriel(input2):
    result = 1
    for i in range(1, input2+1):
        result *= i
    return result


inputs = []
javab = []
input1 = int(input())
for i in range(input1):
    input2 = int(input())
    inputs.append(input2)
    javab.append(faktoriel(input2))
for j in range(len(inputs)):
    print(inputs[j] ," : ",javab[j])
    
