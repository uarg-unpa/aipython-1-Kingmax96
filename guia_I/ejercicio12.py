# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.

# #datos
capital_a_invertir = float(input(f'ingrese el capital que desea invertir: ')) 
cantidad_años_inversion = float(input(f'ingrese el tiempo de inversion en años: '))
interes_anual = float(input(f'Ingrese el interés anual en porcentaje: '))

# #ecuacion
capital_obtenido =  ((capital_a_invertir*cantidad_años_inversion)*interes_anual)/100
# #resultado 
print(capital_obtenido)
