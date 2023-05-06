todos = {
    "Harry Houdini": "mago",
    "Newton": "cientifico",
    "David Blaine": "mago",
    "Hawking": "cientifico",
    "Messi": "otros",
    "Teller": "mago",
    "Einstein": "cientifico",
    "Pele": "otros",
    "Juanes": "otros",
}

# store the names (the keys of the new dict) as a set (keeps elements unique)
profesiones = set(todos.values())  # print(profesiones) --> {'cientifico', 'otros', 'mago'}

# use a list comprehension, iterating through keys and checking the values match each n
indexed_by_prof = {}
for profesion in profesiones:
    indexed_by_prof[profesion] = [k for k in todos.keys() if todos[k] == profesion]

magos = indexed_by_prof['mago']
cientificos = indexed_by_prof['cientifico']
otros = indexed_by_prof['otros']

def hacer_grandioso(dict):
    just_mago = [item[1] for item in dict.items() if item[0] == "mago"]  # [['Harry Houdini', 'David Blaine', 'Teller']]
    return ["El gran " + str(item) for sublist in just_mago for item in sublist]  # flat list


def imprimir_nombres(dict):
    # print(dict.keys())
    if type(dict) is dict:
        for key, value in dict.items():
            print(key)
    else:
        for item in dict:
            print(item)

grandiosos = hacer_grandioso(indexed_by_prof)
# print(grandiosos)

print("** TODOS **")
imprimir_nombres(todos)
print("\n")

print("** GRANDIOSOS **")
imprimir_nombres(grandiosos)
print("\n")

print("** CIENTIFICOS **")
imprimir_nombres(cientificos)
print("\n")

print("** OTROS **")
imprimir_nombres(otros)
print("\n")

print("** MAGOS **")
imprimir_nombres(magos)