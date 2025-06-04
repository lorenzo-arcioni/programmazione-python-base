# Esercizio 1: Crea una tupla mista con elementi di diversi tipi
# Crea una tupla che contenga: un numero intero, una stringa, un booleano, None: 41, "ciao", True, None
tupla_mista = (42, "ciao", True, None)

# Esercizio 2: Accesso tramite indicizzazione positiva e negativa
numeri = (10, 20, 30, 40, 50)
primo_elemento = numeri[0]  # accesso con indice positivo
ultimo_elemento = numeri[-1]  # accesso con indice negativo
secondo_da_fine = numeri[-2]  # penultimo elemento

# Esercizio 3: Slicing - estrarre sotto-tuple
lettere = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
primi_tre = lettere[:3]  # primi 3 elementi
ultimi_due = lettere[-2:]  # ultimi 2 elementi
elementi_pari = lettere[::2]  # elementi in posizione pari (0, 2, 4, ...)
tupla_invertita = lettere[::-1]  # tutta la tupla al contrario

# Esercizio 4: Packing - creare tuple senza parentesi
# Crea una tupla usando il packing (senza parentesi) con i valori: "Mario", 25, "Ingegnere"
persona = "Mario", 25, "Ingegnere"

# Esercizio 5: Unpacking - assegnare elementi a variabili
coordinate = (10, 20)
# Usa l'unpacking per assegnare x e y
x, y = coordinate

# Esercizio 6: Unpacking con operatore * (asterisco)
valori = (1, 2, 3, 4, 5, 6)
# Usa l'unpacking per assegnare il primo elemento a 'primo', l'ultimo a 'ultimo', 
# e tutti quelli in mezzo alla lista 'mezzo'
primo, *mezzo, ultimo = valori

# Esercizio 7: Tupla con un solo elemento (attenzione alla virgola!)
# Crea una tupla che contiene solo il numero 42
tupla_singola = (42,)

# Esercizio 8: Concatenazione con operatore +
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenata = tupla1 + tupla2  # unisci le due tuple

# Esercizio 9: Ripetizione con operatore *
pattern = (0, 1)
tupla_ripetuta = pattern * 3  # ripeti il pattern 3 volte

# Esercizio 10: Verifica di appartenenza con in
linguaggi = ("Python", "Java", "C++", "JavaScript")
ha_python = "Python" in linguaggi  # verifica se "Python" è nella tupla
ha_ruby = "Ruby" in linguaggi  # verifica se "Ruby" è nella tupla

# Esercizio 11: Metodo count() - contare occorrenze
voti = (7, 8, 6, 8, 9, 8, 7)
conta_otto = voti.count(8)  # conta quante volte appare 8
conta_sette = voti.count(7)  # conta quante volte appare 7

# Esercizio 12: Metodo index() - trovare indice
frutta = ("mela", "banana", "arancia", "banana")
indice_banana = frutta.index("banana")  # trova l'indice della prima "banana"
indice_mela = frutta.index("mela")  # trova l'indice di "mela"

# Esercizio 13: Lunghezza con len()
colori = ("rosso", "verde", "blu", "giallo", "viola")
numero_colori = len(colori)  # calcola la lunghezza della tupla

# Esercizio 14: Conversione da tupla a lista
numeri_tupla = (1, 2, 3, 4, 5)
numeri_lista = list(numeri_tupla)  # converti la tupla in lista usando list()

# Esercizio 15: Conversione da lista a tupla
lettere_lista = ['a', 'b', 'c', 'd']
lettere_tupla = tuple(lettere_lista)  # converti la lista in tupla usando tuple()

# Esercizio 16: Tupla annidata e accesso a elementi interni
studente = ("Mario", "Rossi", (2000, "Informatica"))
nome = studente[0]  # accedi al nome (primo elemento)
anno_corso = studente[2]  # accedi alla tupla annidata completa (anno, corso)
anno = studente[2][0]  # accedi solo all'anno dalla tupla annidata
corso = studente[2][1]  # accedi solo al corso dalla tupla annidata

# Esercizio 17: Creazione di coordinate 2D e 3D
# Crea una tupla per coordinate 2D (x=5, y=10)
punto_2d = (5, 10)

# Crea una tupla per coordinate 3D (x=1, y=2, z=3)
punto_3d = (1, 2, 3)

# Esercizio 18: Unpacking multiplo di tuple annidate
dati_persona = ("Alice", "Bianchi", (1995, "Milano"), ("Ingegnere", 50000))
# Usa l'unpacking per estrarre: nome, cognome, anno di nascita, città, professione, stipendio
nome_18, cognome_18, (anno_nascita, citta), (professione, stipendio) = dati_persona

# Esercizio 19: Verifica se una tupla è hashable (può essere usata come chiave)
tupla_numeri = (1, 2, 3)
tupla_con_lista = (1, [2, 3], 4)  # Questa non sarà hashable!

# Calcola l'hash della prima tupla (dovrebbe funzionare)
hash_numeri = hash(tupla_numeri)  # usa hash()

# Esercizio 20: Tupla come chiave in un dizionario
# Crea un dizionario che usa tuple come chiavi per rappresentare coordinate e valori
coordinate_valori = {
    (0, 0): "origine",
    (1, 1): "diagonale",
    (0, 1): "sopra"
}

# Accedi al valore per la coordinata (1, 1)
valore_diagonale = coordinate_valori[(1, 1)]
