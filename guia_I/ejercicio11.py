# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
# costo por hora. Después debe mostrar por pantalla el sueldo que le corresponde.

horas_trabajadas = float(input(f'ingrese la cantidad de horas trabajadas: '))
valor_hora = float(input(f'ingrese el costo de la hora trabajada: '))
sueldo = horas_trabajadas*valor_hora
print(f' el sueldo que le corresponde es de {sueldo}')

