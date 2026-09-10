#Activity 1 
n = int(input("Write a number:"))
if n >= 0:
    print ("This number is positive") 
else: 
    print ("This number is negative") 
#Activity 2
purchasing_price = int(input("Enter a Purchasing price"))
selling_price = int(input("Enter a selling price"))
if selling_price > purchasing_price:
    print ("That is a profit by",selling_price - purchasing_price )
else:
    print ("That is a loss by", purchasing_price - selling_price)
#Activity 3

number = int(input("Write a number"))
if number > 15:
    print ("This number is bigger than 15")
else:
    print ("This number is smaller than 15")
#Activity 4
Number = int(input("Write a number"))
if Number % 2 == 0:
    print ("This number is even")
else:
    print ("This number is odd")