print("Enter your choice: ")

print("1- General")
print("2- Women and Citizens with age > 65")
print("3- Disabled")
print("4- Parents of disabled")
print("5- Wounded freedom fighters")

choice = int(input())
income = int(input("Enter the income: "))  # should be > 0

if choice == 1:
    if income <= 300000: # first 300k tk = 0%
        tax = 0
    elif income > 300000 and income <= 400000: # next 100k tk = 5%
        tax= (income - 3000000) * 5/100
    elif income > 400000 and income <= 700000: # next 300k tk = 10%
        tax= (300000 *0/100)+(100000 * 5/100)+(income-400000) * 10/100
    elif income > 700000 and income <= 1100000: # next 400k tk = 15%
        tax= (300000*0/100)+(100000*5/100)+(300000*10/100)+(income-700000)*15/100
    elif income > 1100000 and income <= 1600000: # next 500k tk = 20%
        tax = (300000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(income-1100000)*20/100
    else:  # rest of all = 25%
        tax = (300000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(500000*20/100)+(income-1600000)*25/100

elif choice == 2:
    if income <= 350000: # first 300k tk = 0%
        tax = 0
    elif income > 350000 and income <= 450000: # next 100k tk = 5%
        tax= (income - 350000) * 5/100
    elif income > 450000 and income <= 750000: # next 300k tk = 10%
        tax= (350000*0/100)+(100000*5/100)+(income-450000)*10/100
    elif income > 750000 and income <= 1150000: # next 400k tk = 15%
        tax= (350000*0/100)+(100000*5/100)+(300000*10/100)+(income-750000)*15/100
    elif income > 1150000 and income <= 1650000: # next 500k tk = 20%
        tax = (350000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(income-1150000)*20/100
    else:   # rest of all = 25%
        tax = (350000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(500000*20/100)+(income-1650000)*25/100

elif choice == 3:
    if income <= 450000: # first 300k tk = 0%
        tax = 0
    elif income > 450000 and income <= 550000: # next 100k tk = 5%
        tax= (income - 450000) * 5/100
    elif income > 550000 and income <= 850000: # next 300k tk = 10%
        tax= (450000*0/100)+(100000*5/100)+(income-550000)*10/100
    elif income > 850000 and income <= 1250000:  # next 400k tk = 15%
        tax= (450000*0/100)+(100000*5/100)+(300000*10/100)+(income-850000)*15/100
    elif income > 1250000 and income <= 1750000:  # next 500k tk = 20%
        tax = (450000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(income-1250000)*20/100
    else:     # rest of all = 25%
        tax = (450000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(500000*20/100)+(income-1750000)*25/100

elif choice == 4:
    if income <= 350000:  # first 300k tk = 0%
        tax = 0
    elif income > 350000 and income <= 450000:  # next 100k tk = 5%
        tax= (income - 3500) * 5/100
    elif income > 450000 and income <= 750000:  # next 300k tk = 10%
        tax= (350000*0/100)+(100000*5/100)+(income-450000)*10/100
    elif income > 750000 and income <= 1150000:  # next 400k tk = 15%
        tax= (3500*0/100)+(1000*5/100)+(3000*10/100)+(income-7500)*15/100
    elif income > 1150000 and income <= 1650000:  # next 500k tk = 20%
        tax = (350000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(income-1150000)*20/100
    else:   # rest of all = 25%
        tax = (350000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(500000*20/100)+(income-1650000)*25/100

elif choice == 5:
    if income <= 475000:  # first 300k tk = 0%
        tax = 0
    elif income > 475000 and income <= 575000: # next 100k tk = 5%
        tax = (income - 475000) * 5 / 100
    elif income > 575000 and income <= 875000: # next 300k tk = 10%
        tax = (475000 * 0 / 100) + (100000 * 5 / 100) + (income - 575000) * 10 / 100
    elif income > 875000 and income <= 1275000: # next 400k tk = 15%
        tax = (475000 * 0 / 100) + (100000 * 5 / 100) + (300000 * 10 / 100) + (income - 875000) * 15 / 100
    elif income > 1275000 and income <= 1775000:  # next 500k tk = 20%
        tax = (475000 * 0 / 100) + (100000 * 5 / 100)+(300000*10/100)+(400000*15/100)+(income-1275000)*20/100
    else:  # rest of all = 25%
        tax = (475000*0/100)+(100000*5/100)+(300000*10/100)+(400000*15/100)+(500000*20/100)+(income-1775000)*25/100

else:
    print("Invalid choice !! Try again please. N.B. : input range (1-5)")

print('Total tax pay',tax,'TK')

