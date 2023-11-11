import random

names = ["Tom Hanks", "Angelina Jolie", "Scarlett Johansson", "Emma Watson", "Julia Roberts", "Natalie Portman", "Emma Stone", "Johnny Depp", "Morgan Freeman", "Robert DowneyJR"]

print("Welcome to Who Would You Rather!")
print("You will randomly choose two people each time. Choose one, eliminate the other.")

selected_name = random.choice(names)
names.remove(selected_name)
print(f"Selected person: {selected_name}")

while len(names) > 1:
    compared_name = random.choice(names)
    print(f"Comparison person: {compared_name}")

    choose = input(f"{selected_name} or {compared_name} ? (1 or 2): ")

    if choose == "1":
        names.remove(compared_name)
    elif choose == "2":
       names.remove(compared_name)
    else:
        names.remove(selected_name)
        print("Invalid selection !")

    selected_name = selected_name if choose == "1" else compared_name
    print(f"Selected person: {selected_name}")

print("\nGame Over! Last your choose :")
print(selected_name)
