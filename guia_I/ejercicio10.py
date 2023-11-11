# Escribir un programa que pida una temperatura en grados Celsius al usuario, realice
# la transformación de grados Celsius a Fahrenheit e imprima el resultado por pantalla.
# cambio de (50 °C × 9/5) + 32 = 122 °F

temp_C = float(input(f'Ingrese la temperatura en grados Celcius.'))
temp_F = (temp_C * 9/5)+32

print(f'el equivalente de {int(temp_C)} C°, es {temp_F} °F ')
