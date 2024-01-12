num1=25
num2=3

print("la suma es: ",(num1+num2))
print("la resta es: ",(num1-num2))
print("la multiplicacion es: ",(num1*num2))
print("la division es: ",(num1/num2))
print("la division exacta  es: ",(num1//num2))
print("la potencia es: ",(num1**num2))

#CONCATENACION EN PYTHON

texto1="Hola"
texto2="Mundo"
textoFinal=texto1+" "+texto2
print(textoFinal)
print("El saludo es: %s %s" %(texto1,texto2))

saludoFinal="Saludo {} {}".format(texto1,texto2)
print(saludoFinal)

saludoFinal2="Saludo {y} {x}".format(x=texto1,y=texto2)
print(saludoFinal2)
