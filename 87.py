numbers = []
input1 = int(input())
for i in range(input1):
    num = int(input())
    numbers.append(num)
moratab = sorted(numbers, reverse=True)
for num in moratab:
    print(num)