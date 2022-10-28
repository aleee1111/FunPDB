species=['human', 'mouse', 'rat', 'cow', 'chicken', 'pig', 'rabbit', 'cat', 'dog', 'SARSCoV2', 'hamster', 'frog', 'SARSCoV1']
#file=open('dataset/pdb_chain_taxonomy.csv')

# #creo file con id e aa
file=open('Phosphorylation_site_dataset')
id_and_aa=[]
temp_str=''
for linee in file:
    lista=file.readline().split('\t')
    if len(lista)>6:
        temp_str=lista[2]+' '+lista[4]
        id_and_aa.append(temp_str)
file.close()

#rimuovo -p dalla lista 
lista_id_aa=[]
for elem in id_and_aa:
    lista_id_aa.append(elem[:-2])

#creo file sift
str_temp=''
file_a=open('Phosphorylation_site_dataset').readlines() #dataset fosforilazioni
file_b=open('pdb_chain_uniprot.csv').readlines()#file sifts
lista_a=[]
lista_b=[]
#elem 2(id uniprot), 4(aa) da righe dataset
#elem 0(id pdb), 2(id uniprot) da file sifts
for elem in file_a:
    lista_a.append(elem.split('\t'))
for elem in file_b:
    lista_b.append(elem.split(','))
#rimuovo dalle liste le prime righe 
lista_a=lista_a[4:]
lista_b=lista_b[2:]

#mi servono due file sifts per avere tutte le info
#comincio prendendo l'id del pdb
sifts_a=[]

for b in lista_b:
    for a in lista_a:
        if b[2] == a[2]:
            temp_str=b[0]+' '+a[2]+' '+a[4]
            sifts_a.append(temp_str)
print(sifts_a)