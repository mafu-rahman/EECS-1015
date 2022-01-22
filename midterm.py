####
# EECS1015 - Midterm
# Name: Mahfuz Rahman
# Student ID: 217847518
# Email: mafu@my.yorku.ca
####

import random

def task0():
  print("""
Midterm Exam - EECS1015
Name: Mahfuz Rahman
Student ID: 217847518
Email: mafu@my.yorku.ca""")

#####################################################

def task1():
    firstname = input("Your First name: ").strip().lower().title()
    lastname = input("Your Last Name: ").strip().upper()
    wage_week = float(input("Hours you work per week: "))
    wage_hour = float(input("Hourly Wage: "))

    salary = wage_week * wage_hour * 4
    tax_deduction = salary * 0.25
    monthly_salary = salary - tax_deduction

    print(f"""
Employee: {lastname}, {firstname}
${salary:.2f} Monthly salary (gross)
-${tax_deduction:.2f} 25% Tax Deduction
${monthly_salary:.2f} Monthly Salary (net)""")

#####################################################

def task2():
    balance = 10.00
    order = 1
    while (balance > 0.50 and order != 0):  # Balance greater than 0.50 as nothing can be bought with $0.50

        print(f"""You have ${balance:.2f} - What item do you want ?

1: Falafel  $3.00
2: Pizza    $6.00
3: Salad    $1.50
4: Coffee   $1.00
Enter 0 to exit.
""")

        order = int(input("Your Order: "))

        if order == 1 and balance >= 3.00:
            balance = balance - 3.00
            print("Order for *Falafel* confirmed.")

        elif order == 2 and balance >= 6.00:
            print("Order for *Pizza* confirmed.")
            balance = balance - 6.00

        elif order == 3 and balance >= 1.50:
            print("Order for *Salad* confirmed.")
            balance = balance - 1.50

        elif order == 4 and balance >= 1.00:
            print("Order for *Coffee* confirmed.")
            balance = balance - 1.00

        elif order > 4:
            print("Wrong Input !")

        elif order == 0:
            break

        else:
            print("Sorry, you don't have enough money for that item.")

    print(f"You have ${balance:.2f} remaining")
    print("Thank You")

#####################################################

def task3():
    score = 0
    decision = "Y"
    while (decision.upper() != "N"):
        for a in range(1, 11):
            dice = random.randint(1, 6)

            if dice == 6:
                score = score + 1   # Keeping count of score to determine outcome
                print(f"*[{dice}]*")
            else:
                print(f"[{dice}]")

        if score > 1:
            print("You Win")
        else:
            print("You Lose")

        score = 0       # Resetting the score
        decision = input("Do you want to play again? (Y/N): ")

#####################################################

def task4():

    def genrateDNAsequence():
        x = 1
        dna = ""
        for x in range(0, 40):
            a = random.randint(1, 4)
            if a == 1:
                dna = dna + "T"
            elif a == 2:
                dna = dna + "G"
            elif a == 3:
                dna = dna + "C"
            elif a == 4:
                dna = dna + "A"

        applyGammaRadiation(dna)

    def applyGammaRadiation(original_dna):

        if random.randint(1, 100) > 50:

            mutate_position = random.randint(0, 39)                 # Selecting a random mutation position of DNA
            firsthalf_dna = original_dna[0 : mutate_position]       # Separating first half of DNA till mutated position
            lasthalf_dna = original_dna[mutate_position + 1 : 40]   # Separating last half of DNA from mutated position

            if original_dna[mutate_position] == "T":
                replace_dna = "GCA"
                mutated_dna_letter = replace_dna[random.randint(0, 2)]  # Randomly selecting a DNA letter other than "T:

            elif original_dna[mutate_position] == "G":
                replace_dna = "TCA"
                mutated_dna_letter = replace_dna[random.randint(0, 2)]  # Randomly selecting a DNA letter other than "G:

            elif original_dna[mutate_position] == "C":
                replace_dna = "TGA"
                mutated_dna_letter = replace_dna[random.randint(0, 2)]  # Randomly selecting a DNA letter other than "C:

            elif original_dna[mutate_position] == "A":
                replace_dna = "TGC"
                mutated_dna_letter = replace_dna[random.randint(0, 2)]  # Randomly selecting a DNA letter other than "A:

            mutated_dna = firsthalf_dna + mutated_dna_letter + lasthalf_dna  # Concatenating the entire mutated DNA
            detectMutation(original_dna,mutated_dna)  # Passing the original and mutated DNA to the detectMutation() function

        else:
            detectMutation(original_dna, original_dna)

    def detectMutation(dna1, dna2):

        print(dna1 + " (DNA)")
        print(dna2 + " (DNA after radiation)")
        result = " " * 40  # Creating a blank line of 40 spaces
        x = 0
        while x != 40:
            if dna1[x] != dna2[x]:
                m = 1  # Keeping count if mutation detected
                firsthalf_result = result[0:x]                    # Separating first half of blank spaces till mutated position
                lasthalf_result = result[x + 1: 40]                # Separating last half of blank spaces from mutated position
                result = firsthalf_result + "^" + lasthalf_result   # Concatenating the entire result
                print(result)
                print("Mutation Detected")
                break
            else:
                m = 0  # Keeping count if mutation not detected
            x = x + 1

        if m == 0:
            print(result)
            print("No Mutation Detected")

    genrateDNAsequence()

#####################################################

def main():
    task0()
    print("\n-- TASK 1 --\n")
    task1()
    print("\n-- Task 2 --\n")
    task2()
    print("\n-- Task 3 --\n")
    task3()
    print("\n-- Task 4 --\n")
    task4()

if __name__=="__main__":
    main()