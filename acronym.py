str = input("Enter the string to be converted into an acronym ")
acronym = str[0]
for i in range (0, len(str)):
    if str[i] == " ":
        acronym += str[i+1]
acronym = acronym.upper()
print("The acronym is ", acronym)
