import random
name = input(" enter your name:")
salary=int(input("enter your current salary"))
raise_per = random.randint(0, 100)
raise_amount = salary +(salary * raise_per / 100)
new_salary = raise_amount + salary

print(" {0}, your current salary is {1}" .format(name, salary))
print(f" your raise is{raise_per}%of ${salary}" )

print(f""""{name},your new salary is {new_salary}"""")


