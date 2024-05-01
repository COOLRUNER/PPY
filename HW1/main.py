num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

weight = float(input("Enter your weight: "))
height = float(input("Enter your height in meters: "))
bmi = (float(weight) / float(height * height))
print(bmi)

temperature = int(input("Enter the temperature:"))
ceorfa = input("Enter c for celsius or f for fahrenheit:")
if ceorfa == "c":
    sol = (9 / 5) * temperature + 32
    print("The temperature in fahrenheit is " + str(sol))
else:
    sol = (9 / 5) * (temperature - 32)
    print ("The temperature in celsius is " + str(sol))

isPalindrome = False
word = str(input("Enter a word"))
for i in word:
    for j in reversed(word):
        if i == j:
            isPalindrome = True
        else: isPalindrome = False
print(isPalindrome)

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")
