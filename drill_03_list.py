todos = [ "Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

magos, cientificos, otros = [], [], [],

for item in todos:
    if item == "Harry Houdini" or item == "David Blaine" or item == "Teller":
        magos.append(item)
    elif item == "Newton" or item == "Hawking" or item == "Einstein":
        cientificos.append(item)
    else:
        otros.append(item)


def hacer_grandioso(the_list):
    return ["El gran " + str(item) for item in the_list]

def imprimir_nombres(lst):
        for item in lst:
            print(item)

grandiosos = hacer_grandioso(magos)
# print(grandiosos)

all = magos + cientificos + otros

# print("** TODOS **")
# imprimir_nombres(todos)
# print("\n")

print("** TODOS **")
imprimir_nombres(all)
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
