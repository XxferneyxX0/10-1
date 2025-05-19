calificacion= float(input("ingrese nota"))
if calificacion>=4.5:
    print("es superior")
elif calificacion>=3.9 and calificacion<4.5:
    print("alto")
elif calificacion>=3.8 and calificacion<3.0:
    print("basico")
elif calificacion>=2.9 and calificacion<1.0:
    print("bajo")
else:
    print("estudiante no evaluado")