def comparar_salarios_sin_f():
    nombre1 = input("Nombre del trabajador 1: ")
    bruto1 = float(input("Salario bruto de " + nombre1 + ": "))
    deducciones1 = float(input("Deducciones de " + nombre1 + ": "))
    bonificaciones1 = float(input("Bonificaciones de " + nombre1 + ": "))
    neto1 = bruto1 - deducciones1 + bonificaciones1

    nombre2 = input("Nombre del trabajador 2: ")
    bruto2 = float(input("Salario bruto de " + nombre2 + ": "))
    deducciones2 = float(input("Deducciones de " + nombre2 + ": "))
    bonificaciones2 = float(input("Bonificaciones de " + nombre2 + ": "))
    neto2 = bruto2 - deducciones2 + bonificaciones2

    if neto1 > neto2:
        print("Mayor salario neto: " + nombre1)
    elif neto2 > neto1:
        print("Mayor salario neto: " + nombre2)
    else:
        print("Salario neto igual: " + nombre1 + " y " + nombre2)