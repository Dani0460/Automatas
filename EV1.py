import exrex

lista=(list(exrex.generate("(1|7|9|5|2|4|0){1}((\.|E)(d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0){1}){1}(\.|E){1}dacp((((\.|E)(d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0){1}){1})|E)\.1795240")))

print("Sanitizando...")
for i in range(len(lista)):
    if('E' in lista[i]):
        lista[i]=lista[i].replace('E','')

print("Ya casi terminamos xddd")
lista = list(dict.fromkeys(lista))
print(lista)



#(d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0)
#((\.|E)(a|b){1}){1}
"""print("S={d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0|.}")
print("ingresa una cadena de texto, toma en cuenta el alfabeto")
s=input()"""




