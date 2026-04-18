#proma calculadora de indice de masa corporal



    # entrada de datos
peso = float(input("tu peso en kg: "))
altura = float(input("tu altura en metros: "))

    # formula del IMC
imc = peso / (altura ** 2) # ** 2 significa "elevado al cuadrado"

    # mostrar resultado con 2 decimales
print(f"tu IMC es {imc:.2f}")

    # Clasificacion
if imc < 18.5:
        print("clasificacion: bajo peso")
elif imc < 25:
        print("clasificacion: normal") 
elif imc < 30:
        print("clasificacion: sobrepeso") 
else:
        print ("clasificacion: obesidad") 

        
    # fin del programa
       