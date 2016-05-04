# using the int, input, bin, hex, oct built in functions

def convert_number(n) :

    print "Conversor de Numeros"

    print "1- Convert to bin\n2- Convert to Octal\n3- Convert to Hex"

    print "\nIngrese una opcion : "
    opcion = int(input())

    if opcion == 1 :

        return bin(n)

    if opcion == 2 :

        return oct(n)

    return hex(n)


print "Ingrese numero : "
n = int(input())

print convert_number(n)



