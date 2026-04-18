print ("hola mundo")

# programa calculadora de indice de masa corporal (IMC)



    # entrada de datos    
peso = float(input("tu peso en kg:"))
altura = float(input("tu altura en metros:"))
imc = peso/ (altura ** 2)
print(f"Tu IMC es {imc:.2f}")
if imc < 18.5:
    print("bajo peso")
elif imc < 25:
    print("normal")
elif imc <30:
    print("sobrepeso")
else:
    print("obesidad")

  

 # fin del programa   



