#Hecho Por José Aleksei Martínez Hernández
import sys
from importlib.resources import path
import os

def imprimirTexto(path_recibido):

    path = path_recibido.replace('\\','/') 
    
    i=1
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f:
            x=filename
            f = open("leerTXT.txt", "a")
    
            root, extension = os.path.splitext(x)
            if extension == ".TXT" or extension == ".txt" or extension == ".Txt":
                f.write(str(i)+"|"+x+"\n")
                print(str(i)+".- "+x)
                i=i+1
            
            f.close()

def imprimirError(path_recibido):

    path = path_recibido.replace('\\','/') 
    
    i=1
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f:
            x=filename
            f = open("leerError.txt", "a")
    
            root, extension = os.path.splitext(x)
            if extension == ".ERROR" or extension == ".Error" or extension == ".error":
                f.write(str(i)+"|"+x+"\n")
                print(str(i)+".- "+x)
                i=i+1
            
            f.close()

print("¿Que desea leer?\n 1.- Archivos de texto(.TXT)\n 2.-Archivos de error(.ERROR)")
x = input()

if x == "1":
    imprimirTexto(sys.argv[1])
elif x == "2":
    imprimirError(sys.argv[1])
else:
    print("Opcion no valida")
#imprimirTexto(sys.argv[1])


#Hecho Por José Aleksei Martínez Hernández
