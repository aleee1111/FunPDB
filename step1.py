import operator


file=open('/home/ale_pcc/bioinformatica/progetto_tesi/dataset/Phosphorylation_site_dataset')

colonna=[]
for linee in file:
    lista=file.readline().split('\t')
    if len(lista)>6:
        colonna.append(lista[6])#metto in lista tutta la colonna con i nomi
file.close()

#uso set per avere solo elementi unici e dopo ricreo una lista
set_species=set(colonna)
list_species=list(set_species)

#creo un dizionario e lo inizializzo con valori iniziali a 0
dict_species={}
for i in range(len(list_species)):
    dict_species.setdefault(list_species[i],0)

#conto il numero di occorrenze delle specie nel file
file=open('/home/ale_pcc/bioinformatica/progetto_tesi/dataset/Phosphorylation_site_dataset')
for linea in file:
    for specie in list_species:
        if specie in linea:
            dict_species[specie]+=1
#print(dict_species)
file.close()

#filtro le specie che ricorrono più di 20 volte
for key in dict_species.copy(): #uso una copia del dizionario per non avere errori durante l'esecuzione
    if dict_species[key] < 20:
        del dict_species[key]
#ordino il dizionario 
sorted_dict_species= dict(sorted(dict_species.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict_species)