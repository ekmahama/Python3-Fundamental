acronym = input("What acronym do you want to add? ")
definition = input(f"What is definitino of {acronym}?")
with open("input.txt", "a") as file:
    file.write(f"{acronym} - {definition}\n")