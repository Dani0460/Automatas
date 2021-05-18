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





ABC="abcdefghijklmnñopqrstuvwxyz"
numeros="0123456789"  
lenguajearitmetico = ["0","1","2","3","4","5","6","7","8","9", "+", "*", "/", "-", "^", "(", ")"]
constantessigno = ["-9","-8","-7","-6","-5","-4","-3","-2","-1","-0","+0","+1","+2","+3","+4","+5","+6","+7","+8","+9"]
identificadores = []



def q3_aritmetica(cadena, n, parentesisabiertos, identificadores):
   if(cadena[n] in list(numeros)):
         cadena[n]="A"
         return(q3_aritmeticac(cadena, n+1, parentesisabiertos, identificadores))
     
   if(cadena[n] in ABC):
        ident=[]
        for x in range(n,len(cadena)) :  
           if( (cadena[x] in ABC) or (cadena[x]in numeros) ):
               ident.append(cadena[x])
           else:
               break
        if("".join(ident) not in identificadores):
            return -1
        else:
            return(q3_aritmeticac(cadena, n+len(ident), parentesisabiertos, identificadores))               
               
   if(cadena[n]+cadena[n+1] in constantessigno):
       cadena[n:n+2]=list("AA")
       return(q3_aritmeticac(cadena, n+2, parentesisabiertos, identificadores))
   if(cadena[n] == "(" ):
       cadena[n]="A"
       return(q3_aritmetica(cadena, n+1, parentesisabiertos+1, identificadores))
   
   print(cadena)
   print(n)
   return 0

def q3_aritmeticac(cadena, n, parentesisabiertos, identificadores):
     if(cadena[n] in list(numeros)):
         cadena[n]="A"
         return(q3_aritmeticac(cadena, n+1, parentesisabiertos, identificadores))
    
     if(cadena[n]in ABC):
         return(q3_aritmetica(cadena, n, parentesisabiertos, identificadores))
     if(cadena[n] in list("+-*/^")):
         cadena[n]="A"
         return( q3_aritmetica(cadena, n+1, parentesisabiertos, identificadores) )
     if(cadena[n]== ")" ):
         cadena[n]="A"
         return( q3_aritmeticac(cadena, n+1, parentesisabiertos-1, identificadores) )
     if( (cadena[n:n+1]==list(";")) and (parentesisabiertos== 0)):
       cadena[n:n+1]=list("A")
       return(1)
     return(0)  








validez=1 

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
            if(d[key][0]=="leer"): 
                identificadores.append( nombre[ 0: (len(nombre)-1) ] )
            
        
        if len(d[key])==3:
        #verifica que expresiones aritméticas sean correctas
            nombre=d[key][0]
            #verifica que el id aritmetico sea correcto y el simbolo := 
            #tambien sea correcto para la asignacion
            if (regexIdentificador.nombreIdAritmetico(nombre) == False or
                d[key][1] != ":="):
                print("Error en linea: ", key+1)
                break
            aritm=q3_aritmetica(list(d[key][2]), 0,0, identificadores)
            if(aritm== 0):
                print("Error de sintáxis en linea: ", key+1)
                break
            if(aritm== -1):
                print("Error de léxico en linea: ", key+1)
                break
                
            
            
    #verifica la ultima linea del programa        
    if key == (len(d))-1:
        #print(len(d[key]))        
        if len(d[key]) != 1 or d[key][0] != "terminar":
            print("Error en linea: ", key+1)
            break

print("No hubo errores")
print(identificadores)
bool(re.match("^[a-z](\w*);", "a1")) 

    

