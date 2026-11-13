from clases.persona import Persona

# Objeto per de tipo Persona 
per = Persona()

nom = input("Nombre: ")
ed = int(input("Edad: "))

per.set_nombre(nom)
per.set_edad(ed)

print("Datos persona")
print(f"{per.get_nombre()}, usted es {per.categoria_edad()} y " \
      f"tiene {per.get_edad()} años")



