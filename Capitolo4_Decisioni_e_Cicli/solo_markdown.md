# 🔄 Iterabili e Iteratori in Python

## 📚 Introduzione

In Python, **l'iterazione** è uno dei concetti fondamentali per la manipolazione e l'elaborazione di collezioni di dati. Alla base di ogni ciclo `for`, `while` o costrutto iterativo, esiste un insieme di meccanismi che coinvolgono due concetti strettamente legati:

- **Iterabile** (*Iterable*)
- **Iteratore** (*Iterator*)

Questi concetti non rappresentano semplici "tipi di oggetti", ma definiscono **comportamenti specifici** che gli oggetti possono esibire quando vengono usati in contesti iterativi. Comprendere come funzionano questi comportamenti permette di scrivere codice più efficiente, controllato e conforme ai principi del linguaggio Python.

## 🔁 Cos'è un Iterabile?

Un **iterabile** è un oggetto che rappresenta una **sequenza di elementi** e che è in grado di **fornire un iteratore** per accedere a questi elementi uno alla volta.

Un oggetto è considerato **iterabile** se implementa il **protocollo dell'iterabile**, ovvero se:

- **implementa un metodo speciale chiamato `__iter__()`**
- questo metodo restituisce un **oggetto iteratore**

Un iterabile è quindi **una collezione di dati** che non è direttamente responsabile di fornire ciascun valore uno dopo l'altro, ma **sa come creare** un oggetto incaricato di farlo.

Come abbiamo potuto osservare, se un oggetto implementa il metodo `__iter__()`, quando esso viene chiamato, restituisce un oggetto **iteratore**.

## 🔄 Cos'è un Iteratore?

Un **iteratore** è un oggetto che **mantiene uno stato interno** e che sa **come restituire i valori successivi** di una sequenza, uno alla volta, fino all'esaurimento degli elementi.

Un oggetto è considerato **un iteratore** se:

- **implementa il metodo `__next__()`**, che restituisce l’elemento successivo nella sequenza a ogni chiamata
- **implementa anche il metodo `__iter__()`**, che restituisce l'oggetto stesso (quindi un iteratore è anche un iterabile)

La caratteristica principale dell’iteratore è che, una volta consumati tutti gli elementi, ogni ulteriore richiesta tramite `__next__()` causerà il sollevamento di un’**eccezione di tipo `StopIteration`**, che segnala la **fine dell’iterazione**.

Quindi l'iteratore si "consuma" ogni volta che usiamo il metodo `__next__()`. Quindi se utilizziamo il metodo ancora una volta, otteniamo un errore dall'interprete:

## ⚙️ Differenza tra Iterabile e Iteratore

| Caratteristica | Iterabile | Iteratore |
|----------------|-----------|-----------|
| Responsabilità | Sa come **fornire un iteratore** | Sa come **restituire i valori uno a uno** |
| Metodo richiesto | `__iter__()` | `__iter__()` e `__next__()` |
| Stato interno | Non mantiene stato | Mantiene uno **stato interno** tra chiamate successive |
| Riutilizzabile | Può essere usato per creare **nuovi iteratori** ogni volta | **Non riutilizzabile** una volta esauriti gli elementi |
| Tipico esempio | Liste, stringhe, tuple | Oggetto restituito da `iter()` |

Quindi, un iterabile può fornire uno (o più) iteratori, ovvero ha la potenzialità di generare un iteratore.

### 🗂️ Dizionari: iterabili e iteratori

- Un **dizionario** in Python è un oggetto **iterabile**, il che significa che si può ottenere un iteratore da esso chiamando il metodo `__iter__()`.
- L’iteratore ottenuto da un dizionario scorre **le chiavi** del dizionario, una alla volta.
- L’iteratore implementa il metodo `__next__()`, che restituisce la chiave successiva ogni volta che viene chiamato.
- Quando si raggiungono tutte le chiavi, una chiamata successiva a `__next__()` genera un’eccezione `StopIteration` (tipico comportamento di tutti gli iteratori).

**In sintesi:**

- Dizionario = iterabile (puoi chiamare `__iter__()` su di esso)  
- Iteratore del dizionario = oggetto con `__next__()` che restituisce le chiavi, una alla volta

Se vuoi iterare sui valori o sulle coppie chiave-valore, puoi ottenere iterabili e iteratori specifici usando i metodi `.values()` e `.items()` del dizionario, che funzionano in modo analogo.  

## 🧠 Perché questa distinzione è importante?

Questa distinzione permette a Python di:

- **Separare la struttura dei dati dalla logica di accesso** sequenziale: un iterabile può essere semplice da rappresentare, mentre l’iteratore si occupa della logica dell’avanzamento.
- **Supportare la lazy evaluation**: gli iteratori possono produrre dati “su richiesta” senza doverli tenere tutti in memoria.
- **Consentire l’uso di cicli `for`**, funzioni come `map()`, `filter()`, e comprensioni, basandosi sul protocollo dell’iterazione.

## 🧭 Protocollo dell’Iterazione in breve

1. Quando un oggetto viene usato in un ciclo `for`, Python chiama il suo metodo `__iter__()`.
2. Questo metodo restituisce un oggetto **iteratore**.
3. Python continua a chiamare il metodo `__next__()` sull’iteratore per ottenere ciascun valore.
4. Quando non ci sono più valori, il metodo `__next__()` solleva l’eccezione `StopIteration`.
5. Il ciclo `for` intercetta l’eccezione e termina l’iterazione.

## 🧩 Alcune proprietà aggiuntive degli iteratori

- Gli **iteratori sono consumabili**: una volta iterati completamente, non possono essere riutilizzati senza ricrearne uno nuovo.
- Gli **iteratori non hanno lunghezza** nota a priori, a differenza delle liste o tuple.
- La loro natura li rende ideali per lavorare con **flussi di dati infiniti o grandi** (es. file, stream, generatori).

### 🧬 Iteratori e gestione efficiente di grandi quantità di dati

Quando lavoriamo con dataset di dimensioni molto grandi — ad esempio una sequenza genomica composta da miliardi di caratteri (A, C, G, T) — caricare l'intera struttura in memoria può essere estremamente inefficiente o addirittura impossibile. Strutture come `list`, `str` o `tuple` contengono tutti i dati in RAM, il che non è scalabile per file di grandi dimensioni.

#### ✅ Iteratori come soluzione

Gli **iteratori** permettono di elaborare dati **uno alla volta**, senza bisogno di caricare l'intera sequenza in memoria. Questo approccio si chiama **lazy evaluation** (valutazione pigra): i dati vengono forniti solo quando richiesti, tramite il metodo `__next__()`.

In questo modo:

- ✅ l'utilizzo di memoria è minimo (viene mantenuto solo l'elemento corrente),
- ✅ l'applicazione può scalare facilmente a dataset enormi,
- ✅ si riducono i tempi di caricamento iniziale.

#### 📌 Esempio realistico

Nel caso di un file contenente il genoma umano (oltre 3 miliardi di caratteri), è possibile aprirlo come un iteratore di caratteri o righe. Python fornisce oggetti file che **sono già iteratori**: è quindi possibile leggere il file **una riga alla volta**, con un impatto minimo sulla memoria.

Questo approccio è utile, ad esempio, per:

- contare la frequenza di una base (es. quante volte appare "G"),
- cercare un pattern genetico,
- validare o convertire il formato dei dati,
- generare statistiche in tempo reale.

Usando un iteratore, possiamo **analizzare il file pezzo per pezzo**, senza mai caricare tutto in memoria. Questo è un vantaggio chiave nella programmazione di basso livello su grandi dataset.

Nella cella seguente, viene mostrato un esempio concreto in Python.

## 🧰 Oggetti built-in iterabili

Python offre molte **strutture dati** che sono nativamente iterabili:

- Liste, tuple, insiemi e dizionari
- Stringhe
- Oggetti restituiti da funzioni come `range()`, `zip()`, `enumerate()`
- File aperti (iterano riga per riga)
- Oggetti definiti dall’utente che implementano `__iter__()`

### 📏 Oggetto di tipo `range`: Iterabile ma non Iteratore

- L’oggetto `range` rappresenta una sequenza di numeri ed è **iterabile**, il che significa che può restituire un iteratore tramite il metodo `__iter__()`.
- Tuttavia, `range` **non è di per sé un iteratore**, perché non implementa il metodo `__next__()`.
- Per scorrere gli elementi di un `range`, è necessario prima ottenere un iteratore da esso chiamando `__iter__()`.
- L’iteratore restituito da `range.__iter__()` implementa `__next__()` e permette di ottenere gli elementi uno per uno.

**Riassunto:**

| Tipo oggetto   | `__iter__()` | `__next__()` | Cos’è?         |
|----------------|--------------|--------------|----------------|
| `range`        | Sì           | No           | Iterabile      |
| `range.__iter__()` | Sì        | Sì           | Iteratore      |

### 🔗 Uso di `zip`: iteratore di tuple

- La funzione built-in `zip()` prende due o più iterabili e restituisce un **iteratore** che produce tuple composte dagli elementi corrispondenti di ogni iterabile.
- `zip` è un **iteratore** perché implementa `__next__()`, quindi può essere usato direttamente per ottenere gli elementi uno alla volta.
- Le tuple restituite da `zip` combinano i valori degli input posizionati allo stesso indice.

**Esempio di comportamento:**

- Input: liste `[1, 2, 3]` e `['a', 'b', 'c']`
- Output `zip`: (1, 'a'), (2, 'b'), (3, 'c')

### 🔢 Uso di `enumerate`: iteratore con indice

- `enumerate()` prende un iterabile e restituisce un **iteratore** che produce tuple `(indice, elemento)`.
- È molto utile quando si vuole accedere sia all’elemento sia alla sua posizione durante l’iterazione.
- Come `zip`, `enumerate` implementa `__next__()` e quindi è un iteratore pronto all’uso.

**Esempio di comportamento:**

- Input: lista `['mela', 'banana', 'ciliegia']`
- Output `enumerate`: (0, 'mela'), (1, 'banana'), (2, 'ciliegia')

### 🔄 Uso di `reversed()`: iteratore inverso

- La funzione built-in `reversed()` prende una sequenza (come una lista o una stringa) e restituisce un **iteratore** che attraversa gli elementi in ordine inverso.
- `reversed` è un iteratore perché implementa `__next__()`, quindi possiamo usarlo per scorrere gli elementi a ritroso uno alla volta.
- Non modifica l’oggetto originale, ma crea un iteratore che genera gli elementi in senso opposto.

**Esempio di comportamento:**

- Input: lista `[10, 20, 30]`
- Output `reversed`: 30, 20, 10

### 📋 `sorted()`: restituisce una nuova lista ordinata

- La funzione `sorted()` prende un iterabile e restituisce una **nuova lista** contenente gli elementi ordinati.
- La lista risultante è iterabile, ma **non è un iteratore**.
- Per ottenere un iteratore dalla lista ordinata, si può usare la funzione `iter()`.

### 🔧 `iter()`: creare un iteratore da un iterabile

- `iter()` è una funzione built-in che prende un oggetto iterabile e restituisce un **iteratore**.
- Questo iteratore può essere usato per ottenere gli elementi uno alla volta con `__next__()`.
- È il modo standard per trasformare un iterabile in un iteratore esplicitamente.

## 📌 Conclusione

Capire la differenza tra **iterabili** e **iteratori** permette di padroneggiare meglio il funzionamento dei cicli, delle comprensioni, delle funzioni di ordine superiore e dei generatori. Questo rende il programmatore capace non solo di usare Python in modo più idiomatico e potente, ma anche di creare oggetti personalizzati che si integrano perfettamente con il sistema di iterazione del linguaggio.

