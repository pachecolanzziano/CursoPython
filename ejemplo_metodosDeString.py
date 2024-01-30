#ejercicio propuesto para cadenas #1
email = input("Ingrese su correo electronico: ")
#solucion sin metodos 
# cont = 0
# for l in email:
#     if l == "@":
#         cont+=1
# print(cont)
# if(cont==1):
#     if(email[0]=="@" or email[(len(email)*-1)]):
#         print("email incorrecto")
#     else:
#         print("email correcto")
# else:
#         print("email incorrecto")
            
#solucion con metodos 
arroba = email.count('@')
if(arroba!=1 or email.rfind('@')==(len(email)-1) or email.find('@')==0):
    print("Email incorrecto")
else:
    print("Email correcto")
    