katz_deli = []

def line(katz_deli):
    if katz_deli == []:
        print("The line is currently empty.")
    else:
        sentence = "The line is currently:"

        for index, name in enumerate(katz_deli):
            sentence += f" {index + 1}. {name}"
        print(sentence)


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        person = line.pop(0)
        print(f"Currently serving {person}.")