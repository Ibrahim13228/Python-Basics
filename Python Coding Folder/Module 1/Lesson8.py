Medical_cause = (input("Do you have a medical cause? Y/N"))
if Medical_cause == ("Y"):
    print ("You are allowed")
else:
    attendance = int (input("What is your attendance?"))
    if attendance >= 75:
        print ("You are allowed")
    else:
        print ("You are not allowed")   

#Activity 2
Unit = int (input("How many units are you using?"))
if  (Unit < 50):
    cost = (Unit * 2.60)
    surcharge = 25 
    print (cost + surcharge)

elif (Unit > 50 and Unit < 100):
    cost = (Unit * 3.25)
    surcharge = (35)
    print (cost + surcharge)

#Activity 3

print ("What type of ride would you like?")
print ("Pick a for bike and b for car")
choice = (input("Choose a or b"))
if choice == 'a':
    print ("You chose bike")
    print ("What type of bike would you like")
    print ("Pick A for a mountain bike and B for a cruiser")
    choice = (input("Pick A or B"))
    if choice == 'A':
        print ("A mountain bike is coming to your door")
    else:
        print("A cruiser will arrive at your door soon")
else:
    print ("You chose car")
    print ("What type of car would you like")
    print ("Pick a for a BMW and b for a Ford")
    choice = (input("Pick a or b"))
    if choice == 'a':
        print ("A BMW will pick you up shortly")
    else:
        print ("A Ford will pick you up shortly")
    
