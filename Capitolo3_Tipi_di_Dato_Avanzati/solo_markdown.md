# 🧠 Dizionari in Python: Guida Completa

I **dizionari** (`dict`) sono una delle strutture dati più potenti e versatili in Python.  
Sono utilizzati per rappresentare **collezioni di coppie chiave-valore**, dove ogni chiave è un identificatore unico che punta a un valore associato.

🔑 I dizionari sono ideali per modellare:

- Oggetti reali (es. un utente con nome, età, email)
- Tabelle di lookup (es. conversioni tra codici e significati)
- Configurazioni di sistema o parametri di un programma
- Contatori e frequenze (es. conteggio parole in un testo)
- Strutture annidate come JSON

Utilizzando i dizionari, è possibile ottenere un accesso diretto ai dati tramite una chiave, evitando la necessità di scorrere l’intera collezione.

⚡ Sono inoltre estremamente efficienti in termini di prestazioni: l’accesso, l’inserimento e la cancellazione di un elemento avvengono mediamente in tempo **costante** (`O(1)`), grazie all’uso di una **hash table**.

## 📌 1. Definizione e Sintassi

Un dizionario in Python è:

- **Mutabile**: può essere modificato dopo la creazione (aggiunta, modifica o rimozione di elementi).
- **Indicizzato tramite chiavi**: al posto degli indici numerici delle liste, si usano chiavi definite dall’utente.
- **Non ordinato** (fino a Python 3.6): l’ordine degli elementi non era garantito.
- **Ordinato** (da Python 3.7 in poi): mantiene l’ordine di inserimento.
- **Chiavi univoche**: ogni chiave deve essere unica nel dizionario; i valori, invece, possono ripetersi.

📘 Le chiavi devono essere di tipo **hashable** (immutabili), come `str`, `int`, `float`, `tuple` (contenente solo elementi immutabili), mentre i valori possono essere di qualsiasi tipo (inclusi altri dizionari).

### 🔹 Sintassi base

### 🔹 Creazione con `dict()`

## 🔍 3. Accesso ai dati e Modifica dei valori nei dizionari

I dizionari utilizzano le **chiavi (keys)** per accedere ai **valori (values)**. Esistono vari modi per accedere, modificare o aggiungere coppie chiave-valore.

### 🔹 Accesso diretto con l'operatore `[]`

Utilizza la sintassi `dizionario[chiave]` per accedere al valore associato a una chiave. Se la chiave non esiste, Python solleverà un `KeyError`.

### 🔹 Accesso sicuro con `.get()`

Il metodo `.get()` consente di accedere a una chiave senza rischiare un `KeyError`. Se la chiave non è presente, restituisce `None` (o un valore di default specificato).


### 🔹 Aggiunta o Modifica di coppie chiave-valore

Se assegni un valore a una chiave già esistente, il valore viene sovrascritto. Se la chiave non esiste, viene creata.

## ✏️ 4. Aggiunta, Rimozione e Svuotamento del dizionario

### 🔹 Aggiungere una nuova coppia

Assegna un valore a una nuova chiave come nel caso della modifica:

### 🔹 Rimuovere coppie dal dizionario

Ci sono vari metodi per rimuovere dati:

📌 **Quando usarli:**

- Usa del se vuoi semplicemente rimuovere una chiave senza interesse per il suo valore.
- Usa pop() se vuoi anche ottenere il valore rimosso.
- Usa popitem() per rimuovere elementi in modo Last-In-First-Out, utile ad esempio per strutture tipo stack.

⚠️ Se `del` o `pop` viene usato con una chiave inesistente, viene sollevato un `KeyError`.

### 🔹 Svuotare completamente il dizionario

