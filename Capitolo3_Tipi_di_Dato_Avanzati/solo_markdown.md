# 🧠 Dizionari

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

Il metodo `.get()` consente di ottenere il valore associato a una chiave senza sollevare eccezioni se la chiave non esiste.  
È possibile specificare un valore di default da restituire in caso di chiave mancante.

Il metodo `.get()` consente di accedere a una chiave senza rischiare un `KeyError`. Se la chiave non è presente, restituisce `None` (o un valore di default specificato).


### 🔹 Aggiunta o Modifica di coppie chiave-valore

Se assegni un valore a una chiave già esistente, il valore viene sovrascritto. Se la chiave non esiste, viene creata.

## ✏️ 4. Aggiunta, Rimozione e Svuotamento del dizionario

### 🔹 Aggiungere una nuova coppia

Assegna un valore a una nuova chiave come nel caso della modifica:

### 🔹 Inserimento condizionato con `.setdefault()`

Simile a `.get()`, ma se la chiave non esiste, la inserisce con il valore specificato.  
Restituisce sempre il valore associato alla chiave, esistente o appena creato.

### 🔹 Rimuovere coppie dal dizionario

Ci sono vari metodi per rimuovere dati:

📌 **Quando usarli:**

- Usa del se vuoi semplicemente rimuovere una chiave senza interesse per il suo valore.
- Usa pop() se vuoi anche ottenere il valore rimosso.
- Usa popitem() per rimuovere elementi in modo Last-In-First-Out, utile ad esempio per strutture tipo stack.

⚠️ Se `del` o `pop` viene usato con una chiave inesistente, viene sollevato un `KeyError`.

### 🔹 Unione e aggiornamento con `.update()`

Aggiorna il dizionario con chiavi e valori presi da un altro dizionario o da un iterable di coppie `(chiave, valore)`.  
Le chiavi esistenti vengono sovrascritte, quelle nuove aggiunte.

### 🔹 Svuotare completamente il dizionario

## 🛠️ Metodi Utili dei Dizionari

### 🔹 Visualizzazione con `.keys()`, `.values()` e `.items()`

- `.keys()` restituisce una vista dinamica di tutte le chiavi del dizionario.  
- `.values()` restituisce una vista dinamica di tutti i valori.  
- `.items()` restituisce una vista dinamica di tutte le coppie `(chiave, valore)`.

### 🔹 Copia superficiale con `.copy()`

Restituisce una copia superficiale del dizionario.  
Le modifiche agli oggetti mutabili contenuti all’interno influenzano entrambe le copie.

### 🔹 Creazione di un dizionario da sequenze con `fromkeys()`

Permette di creare un nuovo dizionario da una sequenza di chiavi, inizializzando tutte con uno stesso valore (default `None`).

### 🔹 Controllo presenza chiave con `in`

Consente di verificare se una chiave è presente nel dizionario tramite l’operatore `in`.

### 🔹 Ordinamento con `sorted()`

Anche se i dizionari mantengono l’ordine di inserimento (da Python 3.7), è possibile ottenere liste ordinate di chiavi, valori o coppie usando la funzione `sorted()`.

### 🔹 Metodi di default dict e altre estensioni

Il modulo `collections` offre estensioni come `defaultdict`, che permette di specificare un valore di default per chiavi mancanti senza sollevare errori.

## Dizionari Annidati (Nested Dictionaries)

I dizionari annidati sono dizionari che contengono come valori altri dizionari.  
Questa struttura permette di rappresentare dati complessi e gerarchici in modo naturale, molto usata per configurazioni, dati JSON, o strutture a più livelli.

### Caratteristiche principali:
- Le chiavi possono essere associate non solo a valori semplici, ma anche ad altri dizionari.  
- È possibile accedere a un valore annidato concatenando più chiavi, ad esempio `dizionario[chiave1][chiave2]`.  
- La modifica o aggiunta di dati richiede attenzione: è necessario assicurarsi che le chiavi intermedie esistano, altrimenti si rischia un `KeyError`.  

### Considerazioni importanti:
- Per operazioni complesse è utile controllare o creare i dizionari annidati in modo dinamico (ad esempio con `.setdefault()` o usando strutture come `defaultdict`).
- La profondità e complessità dei dizionari annidati può rendere il codice più difficile da leggere e mantenere: è buona norma documentare bene la struttura dati.
- Molte librerie esterne che gestiscono dati strutturati (come JSON) usano proprio dizionari annidati per rappresentare i dati.

## Copia Superficiale vs Copia Profonda (copy vs deepcopy)

Quando si lavora con dizionari annidati o contenenti oggetti mutabili (liste, altri dizionari, oggetti personalizzati), è fondamentale capire la differenza tra:

### Copia Superficiale (`copy()`):
- Crea un nuovo dizionario, ma gli oggetti contenuti come valori **non vengono copiati**, bensì referenziati.
- Modifiche a oggetti mutabili contenuti influiscono su entrambe le copie.
- È efficiente e veloce, ma non adatta se è necessario un duplicato completamente indipendente.

### Copia Profonda (`deepcopy()`):
- Crea una copia ricorsiva di tutto il dizionario e degli oggetti contenuti, replicando anche tutti gli oggetti annidati.
- Le modifiche a oggetti mutabili nella copia **non** influenzano l’originale.
- Più costosa in termini di prestazioni e memoria, ma indispensabile per duplicati completi e sicuri.

### Quando usare cosa:
- Usa `copy()` per dizionari con solo valori immutabili o se puoi garantire che i valori mutabili non verranno modificati.
- Usa `deepcopy()` quando lavori con strutture dati complesse e annidate che devono essere indipendenti.

## 🔄 Conversioni Tra Dizionari e Altri Tipi di Dati

Spesso è utile trasformare dizionari in altre strutture dati o viceversa, per adattarsi a specifiche esigenze di elaborazione o formattazione.  

### Conversione da dizionario a lista, tuple o set

- È possibile ottenere una **lista** o una **tupla** delle chiavi, dei valori o delle coppie `(chiave, valore)` usando i metodi `.keys()`, `.values()` e `.items()` e convertendoli con `list()` o `tuple()`.
- Si può creare un **set** delle chiavi o dei valori per operazioni di insieme, sfruttando `set()`.

### Conversione da lista, tuple o set a dizionario

- Dati una lista o una tupla di coppie `(chiave, valore)`, si può costruire un dizionario usando il costruttore `dict()`.
- È importante che le chiavi siano uniche e hashable; in caso contrario, i duplicati verranno sovrascritti.

### Conversione da e verso stringhe

- I dizionari possono essere convertiti in stringhe formattate, ad esempio tramite la serializzazione JSON, per essere salvati o trasmessi.
- È possibile ricostruire un dizionario da una stringa JSON o da altre rappresentazioni testuali, previa deserializzazione o parsing.

### Considerazioni generali

- Durante le conversioni, è importante prestare attenzione al tipo e alla struttura dei dati per evitare perdite di informazioni o errori.
- La mutabilità, l’ordine degli elementi e la presenza di dati annidati possono influenzare il risultato e la complessità della conversione.
- Le conversioni sono strumenti potenti per integrare i dizionari con altre librerie, formati e modelli di dati nel vasto ecosistema Python.

## Serializzazione di Dizionari in JSON

La serializzazione è il processo di trasformare un dizionario Python in un formato testo o binario che può essere salvato su disco, trasmesso o usato da altri programmi.

### JSON (JavaScript Object Notation)
- È un formato di testo leggero, leggibile, e ampiamente utilizzato per scambiare dati tra applicazioni e linguaggi diversi.
- I dizionari Python si mappano naturalmente a oggetti JSON: chiavi stringa e valori possono essere numeri, stringhe, liste, booleani, o altri oggetti JSON.
- Limitazioni: le chiavi devono essere stringhe (in JSON), mentre in Python possono essere altri tipi hashable.
- Supporta strutture annidate profonde, quindi è perfetto per dizionari complessi.
- È facile da leggere e scrivere con la libreria standard `json`.
- Il processo inverso (deserializzazione) converte JSON in dizionari e liste Python.

La serializzazione deve sempre tenere conto del contesto d’uso e delle caratteristiche del formato scelto, bilanciando leggibilità, compatibilità, e complessità della struttura dati.

## 🔚 Conclusioni

I **dizionari** sono una struttura dati centrale in Python, apprezzati per la loro capacità di associare chiavi univoche a valori in modo efficiente e flessibile.  
In questa guida abbiamo esplorato:

- La definizione e le caratteristiche principali dei dizionari: mutabilità, indicizzazione tramite chiavi, e ordine di inserimento.
- Come accedere ai valori in modo diretto e sicuro, aggiungere o modificare coppie chiave-valore.
- I principali metodi per aggiungere, rimuovere e aggiornare elementi, inclusi `del`, `pop()`, `popitem()`, e `update()`.
- Metodi utili per la visualizzazione e manipolazione dei dati, come `.keys()`, `.values()`, `.items()`, `.copy()` e `fromkeys()`.
- L’importanza della distinzione tra copia superficiale e copia profonda in presenza di dizionari annidati o contenenti oggetti mutabili.
- Tecniche di serializzazione per esportare e importare dizionari in formati standard come JSON e CSV.

Comprendere i dizionari e saper utilizzare correttamente i loro metodi è fondamentale per gestire dati complessi in modo efficiente e scrivere codice Python chiaro, robusto e performante.

