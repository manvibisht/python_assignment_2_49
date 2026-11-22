units = float(input("Enter electricity units consumed: "))
if units >= 0:
    if units <= 100:
        bill = units * 5
    else:
        if units <= 200:
            bill = (100 * 5) + (units - 100) * 7
        else:
            bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    print("Total Electricity Bill: Rs.", bill)
else:
    print("Invalid units entered.")