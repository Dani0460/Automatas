import exrex

lista=(list(exrex.generate('\d{1}((\.|E)((a|b){1}|E)){1}(E|\.)dacp((((\.|E)(a|b){1}){1})|E)\.1795240')))
#matching = [s for s in lista if "dacp" in s]

print(lista)
#(d|a|n|i|e|l|j|r|o|c|u|z|1|7|9|5|2|4|0)
#((\.|E)(a|b){1}){2}




