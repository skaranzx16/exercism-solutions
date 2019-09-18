sc = int(input("Enter your allergy score "))
adict = {1 : 'Eggs', 2 : 'Peanuts', 4 : 'Shellfish', 8 : 'Strawberries', 16 : 'Tomatoes', 32 : 'Chocolate', 64 : 'Pollen', 128 : 'Cats'}
while sc > 255:
    sc -= 256
    print(sc)
print("Your essential allergy score is", sc)
for x in range (7, -1, -1):
    if sc >= 2**x:
        sc -= 2**x
        print("You are allergic to ", adict[2**x])
