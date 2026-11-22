start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
for num in range(max(2, start), end + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")