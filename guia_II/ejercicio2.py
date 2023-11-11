# 2. Compare su edad y mi edad usando if..else. ¿Quién es mayor (vos o yo)?,
# para el ingreso de la edad use input(“Ingrese su edad: ”)
# Use un condición anidada para:
# Imprimir año si la diferencia es de 1, sino años para diferencias
# mayores.
# Cuando las edades son iguales imprimir un mensaje personalizado,
# ser creativo!!
print(f' quien es mayor, vos o yo ? ')
tu_edad= float(input('ingresa la edad del otro weon: '))

mi_edad= float(input(f'ingresa tu edad chupa: '))

if tu_edad>mi_edad:
    print(f'tas viejito compa')
else:
    print(f' ah so un pibe')