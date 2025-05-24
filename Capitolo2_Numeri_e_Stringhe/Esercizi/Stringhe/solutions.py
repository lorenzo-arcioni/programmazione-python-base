# Esercizio 1: Concatena due stringhe con uno spazio
nome = "Marco"
cognome = "Rossi"
nome_completo = nome + " " + cognome

# Esercizio 2: Ripeti una stringa 5 volte
parola = "ciao"
ripetuta = parola * 5

# Esercizio 3: Ottieni la lunghezza di una stringa
frase = "Python è fantastico"
lunghezza = len(frase)

# Esercizio 4: Accedi al primo e ultimo carattere di una stringa
testo = "programmazione"
primo = testo[0]
ultimo = testo[-1]

# Esercizio 5: Estrai una sottostringa dal 3° al 7° carattere (escluso)
stringa = "abcdefghij"
sottostringa = stringa[2:6]

# Esercizio 6: Inverti completamente una stringa usando lo slicing
parola = "python"
invertita = parola[::-1]

# Esercizio 7: Converti una stringa in maiuscolo e minuscolo
testo = "Ciao Mondo"
maiuscolo = testo.upper()
minuscolo = testo.lower()

# Esercizio 8: Verifica se una stringa contiene solo lettere
parola = "Python"
solo_lettere = parola.isalpha()

# Esercizio 9: Sostituisci tutte le occorrenze di una lettera
frase = "la casa sulla collina"
sostituita = frase.replace('a', 'e')

# Esercizio 10: Dividi una stringa in parole
frase = "Python è un linguaggio potente"
parole = frase.split()

# Esercizio 11: Rimuovi spazi in eccesso da una stringa
# Rimuovi gli spazi all'inizio e alla fine della stringa
testo_originale_11 = "   Python è potente   "
testo_pulito_11 = testo_originale_11.strip()

# Esercizio 12: Conta le occorrenze di una lettera in una stringa
# Conta quante volte appare la lettera 'a' nella frase
frase_12 = "La programmazione è fantastica"
conta_a_12 = frase_12.lower().count('a')

# Esercizio 13: Verifica se una stringa inizia e finisce con caratteri specifici
# Verifica se la stringa inizia con "Py" e finisce con "on"
linguaggio_13 = "Python"
inizia_py_13 = linguaggio_13.startswith("Py")
finisce_on_13 = linguaggio_13.endswith("on")

# Esercizio 14: Estrai ogni secondo carattere da una stringa
# Estrai i caratteri in posizione 0, 2, 4, 6, ecc.
testo_14 = "abcdefghij"
ogni_secondo_14 = testo_14[::2]

# Esercizio 15: Capitalizza la prima lettera di ogni parola
# Trasforma "ciao mondo python" in "Ciao Mondo Python"
frase_15 = "ciao mondo python"
capitalizzata_15 = frase_15.title()

# Esercizio 16: Trova la posizione della prima occorrenza di una sottostringa
# Trova la posizione di "pro" nella stringa
testo_16 = "La programmazione è divertente"
posizione_pro_16 = testo_16.find("pro")

# Esercizio 17: Crea un acronimo dalle iniziali delle parole
# Da "Artificial Intelligence" crea "AI"
frase_17 = "Artificial Intelligence"
acronimo_17 = ''.join([parola[0] for parola in frase_17.split()])

# Esercizio 18: Verifica se una stringa è un palindromo (ignora maiuscole/minuscole)
# Un palindromo si legge uguale da sinistra a destra e da destra a sinistra
parola_18 = "Anna"
palindromo_18 = parola_18.lower() == parola_18.lower()[::-1]

# Esercizio 19: Formatta una stringa con f-string per mostrare nome ed età
# Crea una frase del tipo "Mi chiamo Marco e ho 25 anni"
nome_19 = "Marco"
eta_19 = 25
frase_formattata_19 = f"Mi chiamo {nome_19} e ho {eta_19} anni"

# Esercizio 20: Analizza un codice fiscale per estrarre informazioni
# Dal codice fiscale estrai: le prime 3 lettere (cognome), le successive 3 (nome), 
# e i 2 numeri che rappresentano l'anno di nascita
codice_fiscale_20 = "RSSMRC85M15F205X"
cognome_cf_20 = codice_fiscale_20[:3]
nome_cf_20 = codice_fiscale_20[3:6]
anno_nascita_20 = int(codice_fiscale_20[6:8])