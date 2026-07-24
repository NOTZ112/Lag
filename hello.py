print("Hello World")
name = input("Anu? ")

print("Welcome", name)
a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
age = int(input("നിങ്ങളുടെ വയസ്സ് എത്ര? "))

print("അടുത്ത വർഷം നിങ്ങളുടെ വയസ്സ്:", age + 1)
age = int(input("നിങ്ങളുടെ വയസ്സ്: "))

if age >= 18:
    print("നിങ്ങൾക്ക് Vote ചെയ്യാം.")
else:
    print("നിങ്ങൾക്ക് ഇനിയും Vote ചെയ്യാൻ കഴിയില്ല.")
mark = int(input("മാർക്ക് നൽകൂ: "))

if mark >= 95:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
else:
    print("Fail")
