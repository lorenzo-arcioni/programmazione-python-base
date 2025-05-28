# Esercizio 1: Estrai il dominio da un indirizzo email
# Da "utente@esempio.com" estrai "esempio.com"

email = "marco.rossi@università.it"
dominio = ...

# Esercizio 2: Normalizza un numero di telefono rimuovendo tutti i caratteri non numerici
# Da "+39-123 456.789" ottieni "39123456789"

telefono = "+39-123 456.789"
telefono_pulito = ...

# Esercizio 3: Estrai l'estensione di un file dal percorso completo
# Da "/home/user/documento.pdf" estrai "pdf"

percorso = "/home/user/documento.pdf"
estensione = ...

# Esercizio 4: Converte una stringa in formato "snake_case" a "kebab-case"
# Da "hello_world_python" a "hello-world-python"

snake_case = "hello_world_python"
kebab_case = ...

# Esercizio 5: Estrai le prime due parole da un nome completo
# Da "Marco Antonio Rossi" ottieni "Marco Antonio"

nome_completo = "Marco Antonio Rossi"
prime_due_parole = ...

# Esercizio 6: Rimuovi tutte le vocali da una stringa (sia maiuscole che minuscole)
# Da "Programmazione" ottieni "Prgrmmzn"

parola = "Programmazione"
senza_vocali = ...

# Esercizio 7: Estrai il nome utente da un URL GitHub
# Da "https://github.com/utente123/repository" estrai "utente123"

url_github = "https://github.com/utente123/repository"
username = ...

# Esercizio 8: Normalizza una stringa rimuovendo caratteri speciali e spazi multipli
# Da "  Ciao!!!   Mondo???  " ottieni "Ciao Mondo"

testo_sporco = "  Ciao!!!   Mondo???  "
testo_pulito = ...

# Esercizio 9: Estrai il codice paese da un numero di telefono internazionale
# Da "+39 123 456 789" estrai "39"

tel_internazionale = "+39 123 456 789"
codice_paese = ...

# Esercizio 10: Converti una data in formato "GG/MM/AAAA" in formato "AAAA-MM-GG"
# Da "15/03/2024" ottieni "2024-03-15"

data_italiana = "15/03/2024"
data_iso = ...

# Esercizio 11: Estrai la parte locale di un indirizzo email (prima della @)
# Da "nome.cognome@dominio.com" estrai "nome.cognome"

email_11 = "nome.cognome@dominio.com"
parte_locale_11 = ...

# Esercizio 12: Rimuovi i prefissi "www." e "http://" da un URL
# Da "http://www.esempio.com" ottieni "esempio.com"

url_12 = "http://www.esempio.com"
dominio_pulito_12 = ...

# Esercizio 13: Estrai l'ora da un timestamp in formato "AAAA-MM-GG HH:MM:SS"
# Da "2024-03-15 14:30:25" estrai "14:30:25"

timestamp_13 = "2024-03-15 14:30:25"
ora_13 = ...

# Esercizio 14: Censura una parola in una frase sostituendo le lettere centrali con asterischi
# Da "password" ottieni "pa****rd" (lascia primi 2 e ultimi 2 caratteri)

parola_14 = "password"
censurata_14 = ...

# Esercizio 15: Estrai il nome del file senza estensione da un percorso
# Da "/documenti/report.docx" estrai "report"

percorso_15 = "/documenti/report.docx"
nome_file_15 = ...

# Esercizio 16: Converte coordinate "lat,lon" in formato separato
# Da "45.4642,9.1900" estrai latitudine "45.4642" e longitudine "9.1900"

coordinate_16 = "45.4642,9.1900"
latitudine_16 = ...
longitudine_16 = ...

# Esercizio 17: Estrai la versione da una stringa di user agent
# Da "Mozilla/5.0 (Windows NT 10.0)" estrai "10.0"

user_agent_17 = "Mozilla/5.0 (Windows NT 10.0)"
versione_17 = ...

# Esercizio 18: Converte un hashtag in testo normale
# Da "#PythonProgramming" ottieni "Python Programming" (rimuovi # e separa le parole maiuscole)

hashtag_18 = "#PythonProgramming"
testo_normale_18 = ...

# Esercizio 19: Estrai il protocollo da un URL completo
# Da "https://www.esempio.com/pagina" estrai "https"

url_completo_19 = "https://www.esempio.com/pagina"
protocollo_19 = ...

# Esercizio 20: Normalizza un codice fiscale rimuovendo spazi e convertendo in maiuscolo
# Da "rssmrc 85m15 f205x" ottieni "RSSMRC85M15F205X"

cf_sporco_20 = "rssmrc 85m15 f205x"
cf_pulito_20 = ...

# Esercizio 21: Estrai i caratteri alle posizioni pari da una stringa
# Da "programmazione" ottieni "pormain"
s = "programmazione"
risultato_21 = ...

# Esercizio 22: Estrai i caratteri alle posizioni dispari da una stringa
# Da "programmazione" ottieni "rgamzoe"
s = "programmazione"
risultato_22 = ...

# Esercizio 23: Inverti una stringa saltando un carattere ogni due (primo carattere incluso)
# Da "abcdefghij" ottieni "jhfdb"
s = "abcdefghij"
risultato_23 = ...

# Esercizio 24: Estrai gli ultimi 5 caratteri in ordine inverso
# Da "manipolazione" ottieni "enoiz"
s = "manipolazione"
risultato_24 = ...

# Esercizio 25: Estrai ogni terzo carattere partendo dal secondo (incluso)
# Da "0123456789abcdef" ottieni "147ad"
s = "0123456789abcdef"
risultato_25 = ...

# Esercizio 26: Estrai i caratteri in ordine inverso escludendo il primo e l’ultimo
# Da "algoritmo" ottieni "mtirogl"
s = "algoritmo"
risultato_26 = ...

# Esercizio 27: Estrai un carattere ogni due (primo incluso), tra la terza e l’ultima posizione esclusa
# Da "estrazione" ottieni "tain"
s = "estrazione"
risultato_27 = ...

# Esercizio 28: Crea una nuova stringa concatenando i primi 3 caratteri e gli ultimi 3 (gli ultimi 3 invertiti)
# Da "funzionale" ottieni "funela"
s = "funzionale"
risultato_28 = ...

# Esercizio 29: Estrai ogni terzo carattere, a partire dal penultimo verso l’inizio
# Da "abcdefghijk" ottieni "jgda"
s = "abcdefghijk"
risultato_29 = ...

# Esercizio 30: Escludendo i primi 2 e gli ultimi 2 caratteri, estrai i rimanenti saltandone uno ogni volta.
# Da "programmazione" ottieni "ormai"
s = "programmazione"
risultato_30 = ...