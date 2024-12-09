
cadena = input ("Introduce una cadena")
letras =sum (c.isalpha()for c in cadena)
digitos = sum(c.isdigit()for c in cadena)
print (f"La cadena tiene {letras} letras y {digitos} digitos ")