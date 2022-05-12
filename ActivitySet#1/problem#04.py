# Conditional Execution

#hrs = input("Enter hours? ")
hrs = int((input("Enter Hours:")))
rate = float (input("Enter rate:"))
gross=( hrs * rate) if hrs <= 40 else 40 * rate + 1.5 * rate * (hrs-40)
print(str(gross))
