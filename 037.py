num = abs(int(input("Enter an integer: ")))
count = 1 if num == 0 else 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)