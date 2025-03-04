# Enter acronym to look up

def AddAcronym():
    acronym = input("What acronym do you want to add? ")
    definition = input(f"What is definitino of {acronym}?")
    with open("input.txt", "a") as file:
        file.write(f"{acronym} - {definition}\n")

def FindAcronym():
    acc = input("Enter acronym: ")
    found = False
    try:
        with open('input.txt') as file:
            for line in file:
                if acc in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError:
        print("File not found")

    if not found:
        print("The acronym was not found")

def mainIn():
    choice = input("Do you want to find(F) or add(A) acronym? Enter F or A or Q to exit ")
    if choice.lower() == "a":
        AddAcronym()
    elif choice.lower() =="f":
        FindAcronym()
    elif choice.lower() == "q":
        exit()

if __name__=="__main__":
        while True:
            mainIn()

