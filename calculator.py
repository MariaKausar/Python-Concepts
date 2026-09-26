a = int(input("Enter a = "))
b = int(input("Enter b = "))
operator = input("Which operator you want to perform? ")
print(a, operator, b)

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)    
elif operator == "*":
    print(a * b)
elif operator == "%":
    print(a % b)
elif operator == "**":
    print(a ** b)   
else:
    print("Invalid operator")