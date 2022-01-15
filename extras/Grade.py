#What is the score?
Grade_fun = {"A":"Alpha","B":"Bravo","C":"Charlie", "D":"Delta","F":"Foxtrot"}
Grade_fun2 = {"A":"Alabaster and Artichoke","B":"Buffalo and Brickette","C":"Chameleon and Chocolate", "D":"Dingo and Delicate","F":"Failure and Frustrated"}
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print(f'Your grade is an A as in {Grade_fun["A"]}.')
else:
    if score >= 80:
        print(f'Your grade is a B as in {Grade_fun["B"]}.')
    else:
        if score >= 70:
            print(f'Your grade is a C as in {Grade_fun["C"]}.')
        else:
            if score >= 60:
                print(f'Your grade is a D as in {Grade_fun["D"]}.')
            else:
                print(f'Your grade is an F as in {Grade_fun["F"]}.')

# Try it another way
score2 = int(input("What is your NEXT test score? "))
if score2 >= 90:
    print(f"Grade is A as in {Grade_fun2['A']}.")
elif score2 >= 80:
    print(f"Grade is B as in {Grade_fun2['B']}.")
elif score2 >= 70:
    print(f"Grade is C as in {Grade_fun2['C']}.")
elif score2 >= 60:
    print(f"Grade is D as in {Grade_fun2['D']}.")
else:
    print(f"Grade is F as in {Grade_fun2['F']}.")