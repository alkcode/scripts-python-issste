from ast import Str
from importlib.resources import path
from io import open
from pathlib import Path
import sys

path = "C:\\xampp\\htdocs\\xml\\ArchivoSAT2022\\ArchivoSAT20220930.txt"
recibo =''
rfc=''
num_empleado=''

contador=1

# with open(path) as archivo:
#     for linea in archivo:
#             # if(linea[0:2] == "DC"):           
#             # f=open("leerTXT"+str(contador)+".txt","w")
#         archivo = open(path, "r")
#         datos = archivo.read().split("DC")
#         f=open("leerTXT"+str(contador)+".txt","w")
#         f.write(datos)
#         print(datos)
#         contador=contador+1
#         archivo.close()


with open(path) as f:
    content = f.read()
    split_1 = content.split("DC")
    text = ' '.join(' '.join(split_1).strip().split("DC"))
 
final_file = open("new_file"+str(contador)+".txt", "w")
final_file.write(text)
final_file.close()
        