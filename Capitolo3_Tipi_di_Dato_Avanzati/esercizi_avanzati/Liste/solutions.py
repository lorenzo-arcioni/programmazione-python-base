# Esercizio 1: Copia profonda vs superficiale con liste annidate
# Crea una lista annidata e sperimenta la differenza tra copia superficiale e profonda
import copy
matrice_originale = [[1, 2], [3, 4], [5, 6]]
copia_superficiale = matrice_originale.copy()  # usa copy()
copia_profonda = copy.deepcopy(matrice_originale)  # usa copy.deepcopy()

# Esercizio 2: Ordinamento base con sort()
# Ordina le città in ordine alfabetico (crescente)
citta = ["Roma", "Milano", "Napoli", "Torino", "Bologna", "Bari"]
# Crea una copia e ordinala con sorted()
citta_ordinate = sorted(citta)

# Esercizio 3: Ordinamento decrescente
# Ordina i numeri in ordine decrescente
numeri_da_ordinare = [85, 92, 78, 88, 65, 91]
# Usa sorted() con parametro reverse
numeri_decrescenti_1 = sorted(numeri_da_ordinare, reverse=True)

# Esercizio 4: Ordinamento in-place vs creazione nuova lista
numeri_originali = [5, 2, 8, 1, 9, 3]
# Crea una copia e ordinala con sorted()
numeri_sorted = sorted(numeri_originali)
# Ordina la lista originale con sort()
numeri_originali.sort()

# Esercizio 5: Concatenazione multipla con operatore +
lista_a = [1, 2]
lista_b = [3, 4]
lista_c = [5, 6]
# Concatena tutte e tre le liste in una nuova lista
lista_concatenata = lista_a + lista_b + lista_c

# Esercizio 6: Differenza tra append() ed extend() con liste
base_append = [1, 2]
base_extend = [1, 2]
da_aggiungere = [3, 4, 5]
# Usa append per aggiungere l'intera lista come elemento singolo
base_append.append(da_aggiungere)
# Usa extend per aggiungere ogni elemento singolarmente
base_extend.extend(da_aggiungere)

# Esercizio 7: Ripetizione di liste con operatore *
pattern = ["X", "O"]
# Crea un pattern ripetuto 5 volte
pattern_ripetuto = pattern * 5

# Esercizio 8: Operazioni di ricerca multiple
frutta = ["mela", "banana", "arancia", "banana", "pera", "banana"]
# Trova l'indice della prima "banana"
primo_indice_banana = frutta.index("banana")
# Conta quante volte appare "banana"
conta_banana = frutta.count("banana")
# Verifica se "kiwi" è presente
ha_kiwi = "kiwi" in frutta

# Esercizio 9: Manipolazione di liste annidate
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accedi all'elemento centrale (5)
elemento_centrale = matrice[1][1]
# Accedi all'intera seconda riga
seconda_riga = matrice[1]
# Modifica il primo elemento della terza riga
matrice[2][0] = 10

# Esercizio 10: Casting e conversioni
# Converti la stringa in lista di caratteri
parola = "Python"
caratteri = list(parola)
# Riconverti la lista di caratteri in stringa
parola_ricostruita = "".join(caratteri)

# Esercizio 11: Svuotamento e reinizializzazione
numeri_da_svuotare = [1, 2, 3, 4, 5]
# Svuota la lista usando clear()
numeri_da_svuotare.clear()
# Verifica che sia vuota
lunghezza_dopo_clear = len(numeri_da_svuotare)

# Esercizio 12: Slicing avanzato con step
numeri_slicing = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Elementi in posizione pari (0, 2, 4, 6, 8)
elementi_pari = numeri_slicing[::2]
# Elementi dal terzo al settimo (inclusi)
elementi_centrali = numeri_slicing[2:8]
# Lista completamente invertita
lista_invertita = numeri_slicing[::-1]
# Ogni terzo elemento partendo dal secondo
ogni_terzo = numeri_slicing[1::3]

# Esercizio 13: Problemi con riferimenti condivisi
lista_master = [1, 2, 3]
# Assegnazione diretta (riferimento condiviso)
lista_riferimento = lista_master
# Copia superficiale
lista_copia = lista_master.copy()
# Modifica la lista master
lista_master.append(4)
# Verifica i risultati dopo la modifica

# Esercizio 14: Inserimento e rimozione in posizioni specifiche
compiti = ["studiare", "mangiare", "dormire"]
# Inserisci "fare_sport" alla posizione 1
compiti.insert(1, "fare_sport")
# Rimuovi l'elemento in posizione 2 usando pop()
elemento_rimosso = compiti.pop(2)

# Esercizio 15: Operazioni con liste di liste (matrici semplici)
righe = []
# Crea 3 righe, ognuna con 4 zeri usando ripetizione
riga1 = [0] * 4
riga2 = [0] * 4  
riga3 = [0] * 4
righe.append(riga1)
righe.append(riga2)
righe.append(riga3)
# Modifica l'elemento in posizione [1][2] con il valore 99
righe[1][2] = 99

# Esercizio 16: Reverse e ordinamento decrescente
numeri_reverse = [3, 1, 4, 1, 5, 9, 2, 6]
# Inverti l'ordine degli elementi senza ordinare
numeri_reverse.reverse()
# Crea una lista ordinata in modo decrescente
numeri_decrescenti_2 = sorted(numeri_reverse, reverse=True)

# Esercizio 17: Operazioni su stringhe e liste
frase = "Python linguaggio potente"
# Dividi la frase in parole
parole = frase.split()
# Trova il numero di parole
numero_parole = len(parole)

# Esercizio 18: Verifica di appartenenza base
prezzi = [10.5, 25.0, 30.75, 15.25, 8.99]
prezzo_cercato = 25.0
# Verifica se il prezzo è presente
prezzo_presente = prezzo_cercato in prezzi
# Trova il suo indice (assumendo che sia presente)
indice_prezzo = prezzi.index(prezzo_cercato)

# Esercizio 19: Gestione di liste vuote e controlli
lista_vuota = []
lista_piena = [1, 2, 3]
# Verifica se le liste sono vuote usando len()
e_vuota_1 = len(lista_vuota) == 0
e_vuota_2 = len(lista_piena) == 0
# Verifica usando valutazione booleana diretta
e_vuota_3 = not lista_vuota
e_vuota_4 = not lista_piena

# Esercizio 20: Operazioni avanzate su liste annidate con copia profonda
dati_sensibili = [["user1", ["password1", "email1"]], ["user2", ["password2", "email2"]]]
# Crea una copia profonda per sicurezza
backup_dati = copy.deepcopy(dati_sensibili)
# Modifica la password del primo utente nella copia
backup_dati[0][1][0] = "nuova_password"
# Verifica che l'originale non sia stato modificato