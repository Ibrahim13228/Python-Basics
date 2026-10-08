user_input = (input("Enter a character and i will tell you if it is a letter"))
if (user_input >= "a" and user_input <= "z") or (user_input >= "A" and user_input <= "Z"):
    print ("This is a letter")
else:
    print ("This is not a letter")