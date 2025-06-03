# Esercizio 1: Crea un dizionario con diversi tipi di chiavi e valori

# Crea un dizionario che contenga: una chiave stringa con valore intero, 
# una chiave stringa con valore stringa, una chiave stringa con valore booleano
persona = ...

# Esercizio 2: Accesso diretto ai valori con []

studente = {"nome": "Marco", "età": 20, "corso": "Informatica", "voto": 28}
nome_studente = ...  # accesso al nome
voto_studente = ...  # accesso al voto

# Esercizio 3: Accesso sicuro con get()

prodotto = {"nome": "Laptop", "prezzo": 899.99, "categoria": "Elettronica"}
prezzo_prodotto = ...  # usa get() per ottenere il prezzo
sconto = ...  # usa get() per ottenere "sconto" con valore di default 0

# Esercizio 4: Modifica di valori esistenti

libro = {"titolo": "1984", "autore": "George Orwell", "pagine": 300}
# Modifica il numero di pagine a 328
libro["pagine"] = ...

# Esercizio 5: Aggiunta di nuove coppie chiave-valore

animale = {"nome": "Fido", "specie": "Cane"}
# Aggiungi l'età dell'animale (5 anni)
animale["età"] = ...

# Esercizio 6: Inserimento condizionato con setdefault()

configurazione = {"debug": True, "timeout": 30}
# Usa setdefault per aggiungere "porta" con valore 8080 se non esiste
porta = configurazione.setdefault(...)

# Esercizio 7: Rimozione con del

inventario = {"mele": 50, "banane": 30, "arance": 25, "pere": 15}
# Rimuovi "pere" dal dizionario usando del
del inventario[...]

# Esercizio 8: Rimozione con pop()

punteggi = {"Alice": 95, "Bob": 87, "Carol": 92, "David": 78}
# Rimuovi "Bob" e ottieni il suo punteggio usando pop()
punteggio_bob = punteggi.pop(...)

# Esercizio 9: Aggiornamento con update()

base_config = {"host": "localhost", "porta": 3000}
nuova_config = {"porta": 8080, "debug": True}
# Aggiorna base_config con nuova_config usando update()
base_config.update(...)

# Esercizio 10: Unione di dizionari con unpacking

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict_unito = ...  # unisci i due dizionari usando unpacking

# Esercizio 11: Controllo presenza chiave con in

menu = {"pizza": 12.50, "pasta": 9.00, "insalata": 7.50, "dolce": 5.00}
ha_pizza = ...  # verifica se "pizza" è nel menu
ha_sushi = ...  # verifica se "sushi" è nel menu

# Esercizio 12: Ottenere le chiavi con keys()

temperatura = {"lunedì": 22, "martedì": 25, "mercoledì": 20, "giovedì": 23}
giorni = ...  # ottieni tutte le chiavi (convertile in lista)

# Esercizio 13: Ottenere i valori con values()

prezzi = {"caffè": 1.50, "cappuccino": 2.00, "cornetto": 1.20}
tutti_prezzi = ...  # ottieni tutti i valori (convertili in lista)

# Esercizio 14: Ottenere le coppie con items()

voti_materie = {"matematica": 8, "fisica": 7, "informatica": 9}
coppie_voti = ...  # ottieni tutte le coppie (chiave, valore) come lista

# Esercizio 15: Copia superficiale con copy()

originale = {"x": 10, "y": 20, "z": 30}
copia_dict = ...  # crea una copia usando copy()

# Esercizio 16: Creazione con fromkeys()

chiavi_default = ["rosso", "verde", "blu"]
colori_dict = dict.fromkeys(...)  # crea dizionario con tutte chiavi che hanno valore 0

# Esercizio 17: Svuotamento con clear()

da_svuotare = {"a": 1, "b": 2, "c": 3}
# Svuota completamente il dizionario usando clear()
da_svuotare.clear()

# Esercizio 18: Dizionario annidato e accesso

scuola = {
    "classe_1A": {"studenti": 25, "insegnante": "Prof. Rossi"},
    "classe_2B": {"studenti": 23, "insegnante": "Prof. Bianchi"}
}
insegnante_1A = ...  # accedi all'insegnante della classe 1A
studenti_2B = ...  # accedi al numero di studenti della classe 2B

# Esercizio 19: Conversione da lista di tuple a dizionario

lista_coppie = [("nome", "Luigi"), ("età", 25), ("città", "Roma")]
dict_da_lista = ...  # converti la lista di tuple in dizionario

# Esercizio 20: Popitem() - rimozione ultimo elemento

magazzino = {"sedie": 100, "tavoli": 50, "lampade": 75}
# Rimuovi e ottieni l'ultimo elemento inserito usando popitem()
ultimo_elemento = magazzino.popitem()
