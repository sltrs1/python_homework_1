temperature = float(input("Enter Temperature: "))

if temperature > -5.0:
    print("High probability of ice breaking")
else:
    print("Ice breaking is unlikely")

price = float(input("Enter Price: "))

if price > 5000:
    discount = 0.1
elif price > 3000:
    discount = 0.05
elif price > 1000:
    discount = 0.02
else:
    discount = 0

finalPrice = price*(1-discount)

print("Price =", price)
print("Discount is ", discount*100, "%", sep='')
print("Price with discount =", finalPrice)

