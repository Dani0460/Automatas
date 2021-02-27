import exrex

lista=(list(exrex.generate("(1|7|9|5|2|4|0){1}((\.|E)((a|b){1}|E)){1}(E|\.)dacp((((\.|E)(a|b){1}){1})|E)\.1795240")))
for i in range(len(lista)):
    
    if('E' in lista[i]):
        lista[i]=lista[i].replace('E','')

    print(lista[i])
#(d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0)
#((\.|E)(a|b){1}){1}




