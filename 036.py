num = int(input("Enter an integer: "))
rev = 0
n = abs(num)
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
if num < 0:
    rev = -rev
print("Reversed integer:", rev)