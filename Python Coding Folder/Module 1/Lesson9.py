N = int (input("Enter a number"))
sum = 0

for i in range (1,N+1):
    sum = i + sum
print (sum)

#Activity 2
name = "Ibrahim"
empty = ""
for ch in name:
    empty = ch + empty
print ("The original writing is", name)
print ("The reversed writing is", empty) 

#Activity 3

Number = int (input("Enter a number"))
for I in range (Number,0,-1):
    print (I)