def sumar (a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b
def modulo(a,b):
    return a%b
def exponente(a,b):
    return a**b

while True:
    print("\nCalculadora en Python")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Modulo")
    print("6.Exponente")
    print("7.Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "7":
        break
    if opcion in ("1" , "2" , "3" , "4" , "5" , "6"):
        try:
            num = float (input("Ingrese primer numero: "))
            num2 = float (input("Ingrese segundo numero: "))
            if opcion == "1":
                print ("Resultado: ", sumar(num,num2))
            elif opcion == "2":
                print ("Resultado: ", restar(num,num2))
            elif opcion == "3":
                print ("Resultado: ", multiplicar(num,num2))
            elif opcion == "4":
                if num2 == 0:
                    print("No se puede dividir entre 0")
                else:
                    print("Resultado: ", dividir(num,num2))
            elif opcion == "5":
                print ("Resultado: ", modulo(num,num2))
            elif opcion == "6":
                print ("Resultado: ", exponente(num,num2))
        except ValueError:
            print("ERROR, debes introducir un numero")
    else:
        print("Opcion no valida")