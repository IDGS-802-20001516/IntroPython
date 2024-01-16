print("Suma de Numeros")

num1=int(input("Dame el valor de n1"))
num2=int(input("Dame el valor de n2"))

if num1 > num2: 
    print("El {} es mayor que el {}".format(num1,num2))
else:
    print("El {} es mayor que el {}".format(num2,num1))

print("------------- pedir una edad -------------")

edad=int(input("ingrese su edad"))

if edad >18:
    print("Eres mayor de edad")
elif edad == 18:
    print("tienes 18")
else:
    print("No eres mayor de edad")