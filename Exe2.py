
dict={"Ali":{"PC",7500},"Sara":{"Tablette",1500}, "Ali":{"Souris",150},
    "Sara":{"PC",12000},"Omar":{"Clavier",70},"Ali":{"Ecran",1500},"Khalid":{"PC",7000},"Ali":{"Imprimante",2350}}

#transforme dictionnaire en tableau
nom=[]
val=[]
tabl=[]
for x in dict.items():
    
    nom.append(x[0])
    val.append(x[1])
    
print(nom)