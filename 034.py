n = int(input("Enter a non-negative integer: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)