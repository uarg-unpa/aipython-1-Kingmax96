# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable. Luego debe
# mostrar por pantalla la frase: "Tu índice de masa corporal es: <imc>". Donde <imc>
# es el índice de masa corporal calculado. Tip. buscar en google cómo calcular el IMC.

        # ¿Cómo se calcula el IMC? Con el sistema métrico,
#  la fórmula para el IMC es el peso en kilogramos dividido por la estatura en metros cuadrados.
# Debido a que la estatura por lo general se mide en centímetros,
# divida la estatura en centímetros por 100 
# para obtener la estatura en metros.



peso = float(input(f'ingrese su peso en kg: '))
altura = float(input(f'ingrese su altura en metros: '))

IMC = (peso/(altura*altura))#buscar en google cómo se calcula.float
print(f'Su IMC (Índice de Masa Corporal) es de: {IMC}')