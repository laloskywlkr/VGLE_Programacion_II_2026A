num1=int(input("Dame el primer número: "))
num2=int(input("Dame el segundo número: "))
num3=int(input("Dame el tercer número: "))

suma=num1+num2+num3
promedio=suma/3

if num1>=num2:
    if num1>=num3:
        mayor=num1
    else:
        mayor=num3
else:
    if num2>num3:
        mayor=num2
    else:
        mayor=num3

print("La suma de los 3 números es:", suma)
print("El promedio es:", promedio)
print("El mayor de los 3 es:", mayor)