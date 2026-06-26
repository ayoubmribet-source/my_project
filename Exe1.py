transactions =[
("Ali", "PC", 7500), ("Sara", "Tablette", 1500), ("Ali", "Souris", 150),
("Sara", "PC", 12000), ("Omar", "Clavier", 70), ("Ali", "Ecran", 1500),
("Khalid", "PC", 7000), ("Ali", "Imprimante", 2350)
]

dictionnaire={}
for trans in transactions:
    dictionnaire[trans[0]]=trans[1],trans[2]
    
print(dictionnaire)

total_achat_par_client={}
total_nbre_achat={}
moyenne_par_client={}
flag=0
max_nbre_achat=0
for i in range(len(transactions)):
    if flag==1:
        max_nbre_achat=nbre_achat
    client=transactions[i][0]
    prix_tot=0
    nbre_achat=0
  
    for j in range(len(transactions)):
        if client==transactions[j][0]:
            prix_tot=prix_tot+transactions[j][2]
            nbre_achat=nbre_achat+1
            flag=flag+1
            
    
    total_achat_par_client[client]=prix_tot
    total_nbre_achat[client]=nbre_achat
    moyenne_par_client[client]=prix_tot/nbre_achat
    
    if nbre_achat>max_nbre_achat:
        client_fidele=client

print("total_achat_par_client ",total_achat_par_client,"\n")
print("total_nbre_achat ",total_nbre_achat,"\n")
print("moyenne_par_client ",moyenne_par_client,"\n")
print("le client le plus fidèle ayant le plus de nombre d'achat est", client_fidele,"\n")

#Partie non terminée########################

dic_produit={}
for i in range(len(transactions)):
    produit=transactions[i][1]

    
    for j in range(len(transactions)):
        if produit==transactions[j][1]:
            dic_produit[produit]=transactions[i][0]
            

print(dic_produit)
print(dictionnaire)
