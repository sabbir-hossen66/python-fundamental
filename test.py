print("=== Scientific Calculator ===")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Power (**)")

choice = int(input("Enter your choice (1-6): "))
# print(choice)
a= float(input('try to enter number :'))
b = float(input('enter second number: '))

if(choice ==1):
    print(a+b)
elif (choice != 4):
    print(a/b)
else:
    print("Result:", a ** b)