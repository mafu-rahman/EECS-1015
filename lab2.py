# Lab 2
# Author: Mahfuz Rahman
# Email: mafu@my.yorku.ca
# Student ID: 217847518

print("__________")

# Task 1

power = str(input("""Task 1: Type in an exponential in the following form x^y, where x and y are single digits from 0-9.
Type exponent here: """)).strip()

x = int(power[0])           # Extracting the first digit
y = int(power[-1])          # Extracting the last digit
power1 = x**y
print (f"{x}^{y} is {power1}")

print("__________")

# Task 2

sentence = input("""Task 2: First half upper, second half lower
Type a sentence: """).strip()
length = len(sentence)
middle = ((length//2))                  # Finding the middle index
middle_char = sentence[middle]          # Finding the middle character
firsthalf = sentence[0:middle].upper()
secondhalf = sentence[middle:length].lower()
print(f"""The string is {length} characters long. '{middle_char}' is the middle character.
Modified sentence: {firsthalf}|{secondhalf}""")

print("__________")

# Task 3

sentence2 = input("""Task 3: Remove commas and periods. Convert spaces to * and characters to lowercase.
Type a sentence: """).lower()
sentence_edit = sentence2.strip().lower().replace(",","").replace(".","").replace(" ","*")  # Replacing commas, periods and spaces
print(sentence_edit)

print("__________")

# Task 4

sentence3 = input("""Task 4: Substring highlight.
Type a sentence: """).strip()
substring = input("Type your substring: ").strip()
substring_edit = "*"+substring.upper()+"*"          # Highlighting the substring
substring_replace = sentence3.replace(substring,substring_edit)
print(substring_replace)

print("__________")