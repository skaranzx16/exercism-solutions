str = input("Enter the string to be converted into an acronym ")
res = str[0]
for i in range (0, len(str)):
    if str[i] == " ":
        res = res + str[i+1]
res = res.upper()
print("The acronym is", res)
