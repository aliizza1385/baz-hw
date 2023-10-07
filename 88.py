def check(numbers):
    sort = sorted(numbers)
    if numbers == sort:
        return True
    else:
        return False

input1 = int(input())
input2 = []

for i in range(input1):
    num = int(input())
    input2.append(num)

if check(input2):
    print("YES")
else:
    print("NO")