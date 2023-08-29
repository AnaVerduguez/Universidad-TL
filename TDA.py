#CREAMOS EL TAD
def crearCursada(): 
  cursada = [] #Creamos un arreglo vacio
  return cursada #Lo devolvemos

def agregarMateria(cursada, nombre, codigo): #Parametros
  materia = [nombre, codigo] #Crea un arreglo con el nombre y el codigo de la materia
  cursada.append(materia) #Añado la materia a la cursada

def eliminarMateria(cursada, codigo):
  eliminar = -1; #Se inicializan las variables 
  eliminado = False 
  for i in range(0,len(cursada)): #Se iteran la cursada
    if (cursada[i][1] == codigo): #Si el código coincide entra
      eliminar = i; #Se le asigna el indice de la materia a la variable
  if (eliminar >= 0): #Si es mayor o igual a 0 entra
    cursada.pop(eliminar) #Se utiliza pop pasandole el indice para que lo elimine de cursada
    eliminado = True #Se cambia el valor a true porque se pudo eliminar
  return eliminado #Se retorna el valor de eliminado

#PROBAMOS EL TAD
cursada22 = crearCursada() # Creamos la cursada

#Agregamos materia a cursada
agregarMateria(cursada22, "TeoriaDeLenguajes", 123)
agregarMateria(cursada22, "Programacion1", 223)
agregarMateria(cursada22, "Ingles5", 213)

print(cursada22) # -> [['TeoriaDeLenguajes', 123], ['Programacion1', 223], ['Ingles5', 213]]

#Eliminamos la materia con el código 213
eliminarMateria(cursada22, 313)
print(cursada22) # -> [['TeoriaDeLenguajes', 123], ['Programacion1', 223]