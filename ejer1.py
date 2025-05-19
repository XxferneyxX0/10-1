edad = int (input ("ingrese la edad"))
if edad>0 and edad<10:
    print ("es un niño")
elif edad >=10 and edad <15:
    print ("es un preadolecente")
elif edad >=15 and edad<18:
    print ("es un adolecente")
elif edad >= 18 and edad<50:
    print ("es un adulto")
elif edad>= 50 and edad<150:
    print ("es un adulto mayor")
