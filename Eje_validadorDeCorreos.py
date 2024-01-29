# For
email = False 
cont = 0
userEmail = input("Ingrese su correo electronico: ")
for i in userEmail:
    if i == "@" or i == ".":
        cont=cont+1

if cont == 2:
    print("correo electronico valido")
else:        
    print("correo electronico invalido")        
        