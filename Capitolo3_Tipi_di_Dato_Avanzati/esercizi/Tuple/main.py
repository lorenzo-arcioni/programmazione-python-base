# Esercizio 1: Crea una tupla mista con elementi di diversi tipi

# Crea una tupla che contenga: un numero intero, una stringa, un booleano, None
tupla_mista = ...

# Esercizio 2: Accesso tramite indicizzazione positiva e negativa

numeri = (10, 20, 30, 40, 50)
primo_elemento = ...  # accesso con indice positivo
ultimo_elemento = ...  # accesso con indice negativo
secondo_da_fine = ...  # penultimo elemento

# Esercizio 3: Slicing - estrarre sotto-tuple

lettere = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
primi_tre = ...  # primi 3 elementi
ultimi_due = ...  # ultimi 2 elementi
elementi_pari = ...  # elementi in posizione pari (0, 2, 4, ...)
tupla_invertita = ...  # tutta la tupla al contrario

# Esercizio 4: Packing - creare tuple senza parentesi

# Crea una tupla usando il packing (senza parentesi) con i valori: "Mario", 25, "Ingegnere"
persona = ...

# Esercizio 5: Unpacking - assegnare elementi a variabili

coordinate = (10, 20)
# Usa l'unpacking per assegnare x e y
x, y = ...

# Esercizio 6: Unpacking con operatore * (asterisco)

valori = (1, 2, 3, 4, 5, 6)
# Usa l'unpacking per assegnare il primo elemento a 'primo', l'ultimo a 'ultimo', 
# e tutti quelli in mezzo alla lista 'mezzo'
primo, *mezzo, ultimo = ...

# Esercizio 7: Tupla con un solo elemento (attenzione alla virgola!)

# Crea una tupla che contiene solo il numero 42
tupla_singola = ...

# Esercizio 8: Concatenazione con operatore +

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenata = ...  # unisci le due tuple

# Esercizio 9: Ripetizione con operatore *

pattern = (0, 1)
tupla_ripetuta = ...  # ripeti il pattern 3 volte

# Esercizio 10: Verifica di appartenenza con in

linguaggi = ("Python", "Java", "C++", "JavaScript")
ha_python = ...  # verifica se "Python" è nella tupla
ha_ruby = ...  # verifica se "Ruby" è nella tupla

# Esercizio 11: Metodo count() - contare occorrenze

voti = (7, 8, 6, 8, 9, 8, 7)
conta_otto = ...  # conta quante volte appare 8
conta_sette = ...  # conta quante volte appare 7

# Esercizio 12: Metodo index() - trovare indice

frutta = ("mela", "banana", "arancia", "banana")
indice_banana = ...  # trova l'indice della prima "banana"
indice_mela = ...  # trova l'indice di "mela"

# Esercizio 13: Lunghezza con len()

colori = ("rosso", "verde", "blu", "giallo", "viola")
numero_colori = ...  # calcola la lunghezza della tupla

# Esercizio 14: Conversione da tupla a lista

numeri_tupla = (1, 2, 3, 4, 5)
numeri_lista = ...  # converti la tupla in lista usando list()

# Esercizio 15: Conversione da lista a tupla

lettere_lista = ['a', 'b', 'c', 'd']
lettere_tupla = ...  # converti la lista in tupla usando tuple()

# Esercizio 16: Tupla annidata e accesso a elementi interni

studente = ("Mario", "Rossi", (2000, "Informatica"))
nome = ...  # accedi al nome (primo elemento)
anno_corso = ...  # accedi alla tupla annidata completa (anno, corso)
anno = ...  # accedi solo all'anno dalla tupla annidata
corso = ...  # accedi solo al corso dalla tupla annidata

# Esercizio 17: Creazione di coordinate 2D e 3D

# Crea una tupla per coordinate 2D (x=5, y=10)
punto_2d = ...

# Crea una tupla per coordinate 3D (x=1, y=2, z=3)
punto_3d = ...

# Esercizio 18: Unpacking multiplo di tuple annidate

dati_persona = ("Alice", "Bianchi", (1995, "Milano"), ("Ingegnere", 50000))
# Usa l'unpacking per estrarre: nome, cognome, anno di nascita, città, professione, stipendio
nome_18, cognome_18, (anno_nascita, citta), (professione, stipendio) = ...

# Esercizio 19: Verifica se una tupla è hashable (può essere usata come chiave)

tupla_numeri = (1, 2, 3)
tupla_con_lista = (1, [2, 3], 4)  # Questa non sarà hashable!

# Calcola l'hash della prima tupla (dovrebbe funzionare)
hash_numeri = ...  # usa hash()

# Esercizio 20: Tupla come chiave in un dizionario

# Crea un dizionario che usa tuple come chiavi per rappresentare coordinate e valori
coordinate_valori = {
    (0, 0): "origine",
    (1, 1): "diagonale",
    (0, 1): "sopra"
}

# Accedi al valore per la coordinata (1, 1)
valore_diagonale = ...
