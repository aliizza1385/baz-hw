def printNumbers(numbers):
    average = sum(numbers[:3]) / 3
    for num in numbers:
        if abs(num - average) > 0:
            print(num)

inputs = []

for i in range(5):
    num = int(input())
    inputs.append(num)
printNumbers(inputs)