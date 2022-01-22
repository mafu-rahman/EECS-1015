# Lab 3
# Author: Mahfuz Rahman
# Email: mafu@my.yorku.ca
# Student ID: 217847518

print("""
-----TASK 1: Ticket Price-----
""")

age = int(input("What is your age ? ").strip())
status = input("Are you a student (Y/N)? ")

if (age<=12):
    if (status != 'Y' and status != 'y' and status != 'N' and status != 'n'):
        print("WRONG INPUT !")
    else:
        print("Fare Type 'CHILD' - Price: $0.50")

elif (age>=65):
    if (status != 'Y' and status != 'y' and status != 'N' and status != 'n'):
        print("WRONG INPUT !")
    else:
        print("Fare Type 'SENIOR' - Price: $0.50")

elif (age>12 and age<65):
    if (status == "Y" or status == 'y'):
        print("Fare Type 'STUDENT' - Price: $1.00")
    elif (status == "N" or status == 'n'):
        print("Fare Type 'ADULT' - Price: $1.50")
    else:
        print("WRONG INPUT !")


print("""
-----TASK 2: Printing String Characters & Reversing-----
""")

sentence = input("Input a sentence: ").strip()
length = len(sentence)
counter = 0         # For controlling the while loop
reverse = ""        # I will store the reversed string in this variable letter by letter.
while (counter<length):
    print(f"Str[{counter}] = '{sentence[counter]}'")
    counter = counter+1
    reverse = reverse + sentence[length-counter]  # Storing the reversed string
print(f"Reversed sentence: '{reverse}'")


print("""
-----TASK 3: The Maximum-----
""")

print("""Keep entering positive numbers.
To quit, enter a negative number.
""")
num=0
max=0
while (num>=0):
    num=int(input("Enter a number: "))
    if (num>max):
        max=num
print(f"Largest number: {max}")

print("""
-----TASK 4: String Triangle-----
""")

str = input("Enter a string: ")
length = int(len(str))

i = 0
j = 1

for i in range(i,length):
    print(str[0 : i+1])

for j in range(j,length):
    print(str[0 : length-j])


input("""
Enter to exit program.""")