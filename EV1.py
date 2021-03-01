import re
print("S={d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0|.}")
print("ingresa una cadena de texto, toma en cuenta el alfabeto")
txt=input()
match=re.match("^((1|7|9|5|2|4|0)+)((\.|E)((d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0)+))*(E|\.)(dacp)(((\.|E)(d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0)+)*|E)(\.1795240$)",txt)
txt=txt.replace('E','')
print(txt)
if(bool(match)==True):
    print("Cadena Valida")
else:
    print("Cadena invalida")
