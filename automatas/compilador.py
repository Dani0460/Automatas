import re

class regexIdentificador:
    def nombreIdentificador(nombre):
        matched=re.match("^[a-z](\w*);",nombre)
        is_match=bool(matched)
        return is_match
    def nombreIdAritmetico(nombre):
        matched=re.match("^[a-z](\w*)",nombre)
        is_match=bool(matched)                         
        return is_match    


def justified():
    with open("test.txt",'r') as file:
        for line in file:
            if line[0:1].isspace():
                return False
        return True        
            

d={}
lines=0
f=open("test.txt","r")
for x in f:
#    print(x)
    d[lines]=x.split()
    lines+=1
#verificacion si archivo está alineado a la izq
if(justified()==False):
    print("err")
    exit()


#verificacion de archivo de texto
#print(len(d))
for key in d.keys():
    if key == 0:
        #print("Titulo del programa")
        #print(d[key])
        if len(d[key]) < 2:
            print("Error en linea: ", key+1)
            break
        nombre=d[key][1]
        if regexIdentificador.nombreIdentificador(nombre) == False:
            print("Error en linea: ", key+1)
        
    if key == 1:
        if len(d[key])!=1 or d[key][0] != "iniciar":
            print("Error en linea: ", key+1)
            break

        if (len(d)-(key+1))== 1:
            print("Programa sin instrucciones")
            break
    #verifica cuerpo de programa
    if (key > 1 and key < len(d)-1):
        #verifica que el cuerpo tenga los espacios adecuados y palabras
        if (len(d[key])<=1 or len(d[key])>3):  
            print("Error en linea: ", key+1)
            break
            
        if len(d[key])==2:
        #verifica que lecturas e impresiones sean correctas
            nombre=d[key][1]
            if ((d[key][0] != "leer" and d[key][0] != "imprimir") or
                (regexIdentificador.nombreIdentificador(nombre) == False)):
                print("Error en linea: ", key+1)
                break
        
        if len(d[key])==3:
        #verifica que expresiones aritméticas sean correctas
            nombre=d[key][0]
            #verifica que el id aritmetico sea correcto y el simbolo := 
            #tambien sea correcto para la asignacion
            if (regexIdentificador.nombreIdAritmetico(nombre) == False or
                d[key][1] != ":="):
                print("Error en linea: ", key+1)
                break
            
    #verifica la ultima linea del programa        
    if key == (len(d))-1:
        #print(len(d[key]))        
        if len(d[key]) != 1 or d[key][0] != "terminar":
            print("Error en linea: ", key+1)
            break

print("No hubo errores")


    

