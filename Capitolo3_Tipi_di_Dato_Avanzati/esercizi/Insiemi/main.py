# Esercizio 1: Crea un set misto con elementi di diversi tipi
# Crea un set che contenga: 
# - numero 42
# - stringa "ciao"
# - booleano True
# - None
set_misto = ...

# Esercizio 2: Conversione da lista a set per rimuovere duplicati

numeri_duplicati = [10, 20, 20, 30, 10, 40]
numeri_unici = ...  # converti in set per rimuovere duplicati

# Esercizio 3: Conversione da stringa a set di caratteri

parola = "programmazione"
caratteri_unici = ...  # converti la stringa in set di caratteri

# Esercizio 4: Aggiunta di elementi con add()

frutti = {"mela", "banana"}
# Aggiungi "arancia" al set usando add()
frutti.add(...)

# Esercizio 5: Rimozione di elementi con remove()

colori = {"rosso", "verde", "blu", "giallo"}
# Rimuovi "verde" dal set usando remove()
colori.remove(...)

# Esercizio 6: Rimozione sicura con discard()

voti = {7, 8, 6, 9}
# Rimuovi il voto 8 usando discard()
voti.discard(...)
# Prova a rimuovere il voto 10 (non presente) usando discard()
voti.discard(...)

# Esercizio 7: Verifica di appartenenza con in

linguaggi = {"Python", "Java", "C++", "JavaScript"}
ha_python = ...  # verifica se "Python" è nel set
ha_ruby = ...  # verifica se "Ruby" è nel set

# Esercizio 8: Unione di set con operatore |

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_unione = ...  # unisci i due set

# Esercizio 9: Intersezione di set con operatore &

animali_domestici = {"cane", "gatto", "pesce", "uccello"}
animali_mammiferi = {"cane", "gatto", "elefante", "leone"}
mammiferi_domestici = ...  # trova l'intersezione

# Esercizio 10: Differenza di set con operatore -

tutti_numeri = {1, 2, 3, 4, 5, 6}
numeri_pari = {2, 4, 6}
numeri_dispari = ...  # trova i numeri dispari (differenza)

# Esercizio 11: Differenza simmetrica con operatore ^

studenti_matematica = {"Alice", "Bob", "Charlie", "Diana"}
studenti_fisica = {"Bob", "Diana", "Eve", "Frank"}
solo_una_materia = ...  # studenti che seguono solo una delle due materie

# Esercizio 12: Aggiornamento in-place con update()

base_set = {1, 2, 3}
nuovo_set = {4, 5, 6}
# Aggiungi gli elementi di nuovo_set a base_set usando update()
base_set.update(...)

# Esercizio 13: Copia di un set

originale = {"a", "b", "c"}
copia_set = ...  # crea una copia usando copy()

# Esercizio 14: Confronto di uguaglianza tra set

set_a = {1, 2, 3}
set_b = {3, 2, 1}
sono_uguali = ...  # verifica se i due set sono uguali

# Esercizio 15: Verifica di sottoinsieme con <=

piccolo_set = {1, 2}
grande_set = {1, 2, 3, 4, 5}
e_sottoinsieme = ...  # verifica se piccolo_set è sottoinsieme di grande_set

# Esercizio 16: Verifica di sovrainsieme con >=

gruppo_completo = {"admin", "user", "guest", "moderator"}
gruppo_base = {"user", "guest"}
e_sovrainsieme = ...  # verifica se gruppo_completo è sovrainsieme di gruppo_base

# Esercizio 17: Verifica di disgiunzione con isdisjoint()

set_pari = {2, 4, 6, 8}
set_dispari = {1, 3, 5, 7}
sono_disgiunti = ...  # verifica se i due set non hanno elementi comuni

# Esercizio 18: Svuotamento set con clear()

da_svuotare = {"elemento1", "elemento2", "elemento3"}
# Svuota completamente il set usando clear()
da_svuotare.clear()

# Esercizio 19: Creazione di frozenset

lista_immutabile = [10, 20, 30, 20, 10]
frozen_numeri = ...  # crea un frozenset dalla lista

# Esercizio 20: Lunghezza di un set

vocali = {"a", "e", "i", "o", "u"}
numero_vocali = ...  # trova la lunghezza del set