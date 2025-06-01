# Esercizio 1: Crea una lista mista con elementi di diversi tipi
# Crea una lista che contenga: un numero intero, una stringa, un booleano, None
lista_mista = [42, "ciao", True, None]

# Esercizio 2: Accesso tramite indicizzazione positiva e negativa
numeri = [10, 20, 30, 40, 50]
primo_elemento = numeri[0]  # accesso con indice positivo
ultimo_elemento = numeri[-1]  # accesso con indice negativo
secondo_da_fine = numeri[-2]  # penultimo elemento

# Esercizio 3: Slicing - estrarre sotto-liste
lettere = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
primi_tre = lettere[:3]  # primi 3 elementi
ultimi_due = lettere[-2:]  # ultimi 2 elementi
elementi_pari = lettere[::2]  # elementi in posizione pari (0, 2, 4, ...)
lista_invertita = lettere[::-1]  # tutta la lista al contrario

# Esercizio 4: Modifica di elementi esistenti
frutti = ["mela", "banana", "arancia"]
# Sostituisci "banana" con "pera"
frutti[1] = "pera"

# Esercizio 5: Aggiunta di elementi con append()
animali = ["cane", "gatto"]
# Aggiungi "elefante" alla fine della lista usando append()
animali.append("elefante")

# Esercizio 6: Inserimento in posizione specifica con insert()
colori = ["rosso", "verde", "blu"]
# Inserisci "giallo" alla posizione 1 usando insert()
colori.insert(1, "giallo")

# Esercizio 7: Rimozione per valore con remove()
voti = [7, 8, 6, 8, 9, 8]
# Rimuovi il primo 8 dalla lista usando remove()
voti.remove(8)

# Esercizio 8: Concatenazione con operatore +
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenata = lista1 + lista2  # unisci le due liste

# Esercizio 9: Estensione con extend()
base = [1, 2, 3]
aggiunta = [4, 5, 6]
# Estendi la lista base con gli elementi di aggiunta usando extend()
base.extend(aggiunta)

# Esercizio 10: Differenza tra append() ed extend()
lista_append = [1, 2]
lista_extend = [1, 2]
nuovi_elementi = [3, 4]

# Usa append per aggiungere nuovi_elementi come singolo elemento
lista_append.append(nuovi_elementi)
# Usa extend per aggiungere gli elementi di nuovi_elementi uno per uno
lista_extend.extend(nuovi_elementi)

# Esercizio 11: Ripetizione di liste
pattern_11 = [0, 1]
lista_ripetuta_11 = pattern_11 * 4  # ripeti il pattern 4 volte

# Esercizio 12: Verifica di appartenenza con in
linguaggi_12 = ["Python", "Java", "C++", "JavaScript"]
ha_python_12 = "Python" in linguaggi_12  # verifica se "Python" è nella lista
ha_ruby_12 = "Ruby" in linguaggi_12  # verifica se "Ruby" è nella lista

# Esercizio 13: Ordinamento con sort() - modifica in-place
numeri_13 = [5, 2, 8, 1, 9]
# Ordina la lista in ordine crescente usando sort()
numeri_13.sort()

# Esercizio 14: Ordinamento con sorted() - crea nuova lista
numeri_originali_14 = [5, 2, 8, 1, 9]
numeri_ordinati_14 = sorted(numeri_originali_14)  # crea una nuova lista ordinata con sorted()

# Esercizio 15: Ricerca di indice con index()
frutta_15 = ["mela", "banana", "arancia", "banana"]
indice_banana_15 = frutta_15.index("banana")  # trova l'indice della prima "banana"

# Esercizio 16: Conteggio occorrenze con count()
lettere_16 = ['a', 'b', 'a', 'c', 'a', 'b']
conta_a_16 = lettere_16.count('a')  # conta quante volte appare 'a'

# Esercizio 17: Copia superficiale per evitare riferimenti condivisi
lista_originale_17 = [1, 2, 3, 4]
lista_copia_17 = lista_originale_17.copy()  # crea una copia usando copy()

# Esercizio 18: Conversione da stringa a lista con list()
parola_18 = "Python"
caratteri_18 = list(parola_18)  # converti la stringa in lista di caratteri

# Esercizio 19: Svuotamento lista con clear()
da_svuotare_19 = [1, 2, 3, 4, 5]
# Svuota completamente la lista usando clear()
da_svuotare_19.clear()

# Esercizio 20: Lista annidata e accesso a elementi interni
matrice_20 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elemento_centrale_20 = matrice_20[1][1]  # accedi all'elemento 5 (centro della matrice)
prima_riga_20 = matrice_20[0]  # accedi alla prima riga completa