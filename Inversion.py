# Proyecto de inversion de numeros denteros de cuatro digitos
print("------------------------------")
n = int(input("INGRESA UN NUMERO DE CUATRO DIGITOS: "))

# Separar los dígitos
n1= n // 1000
n2 = (n // 100) % 10
n3 = (n // 10) % 10
n4 = n % 10


print("---RESULTADO---:")


# Invertir el número
invertido = n4 * 1000 + n3 * 100 + n2 * 10 + n1

print("El numero invertido es:", invertido)

print("------------------------")
print("GRACIAS POR PARTICIPAR:)")
print("------------------------")