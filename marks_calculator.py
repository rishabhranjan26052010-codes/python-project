print("====== EXAM MARKS ======")

Name =input ("name:")
m1 =int(input("Physics: "))
m2 =int(input("Chemistry : "))
m3 = int(input("Math: "))
m4 = int(input("English: "))
m5 = int(input("Hindi: "))

total = m1 + m2 + m3 + m4 + m5
print("Total Marks :", total  )

percentage = total /5
print("Percentage:" , percentage)
