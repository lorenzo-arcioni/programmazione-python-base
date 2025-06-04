# 🔁 Cicli in Python

I cicli sono uno degli strumenti più potenti nella programmazione, permettendo di automatizzare processi ripetitivi e gestire operazioni complesse in modo efficiente. In Python, l’uso corretto dei cicli non solo migliora la leggibilità del codice, ma ne aumenta anche la manutenibilità e la scalabilità. Sono uno strumento fondamentale per evitare **ripetizioni inutili** nel codice e per risolvere problemi che richiedono **iterazione**, come ad esempio:

- stampare i numeri da 1 a 100,
- calcolare la somma degli elementi in una lista,
- elaborare una sequenza di dati elemento per elemento,
- chiedere ripetutamente un input valido all’utente.

## 📜 Perché Usare i Cicli?

- **Eliminare la ridondanza**: Evitare di scrivere codice ripetuto manualmente.
- **Gestione dinamica dei dati**: Lavorare con insiemi di dati di dimensioni variabili.
- **Automazione**: Eseguire task complessi senza intervento umano (es. analisi dati, scraping web).
- **Controllo di flusso**: Gestire scenari dove il numero di iterazioni dipende da condizioni runtime.

## 🧭 Tipi di cicli in Python

In Python esistono due principali tipi di ciclo:

1. **`for` loop**: quando sappiamo **quante volte** vogliamo ripetere un blocco di codice (iterazione su una sequenza).
2. **`while` loop**: quando vogliamo ripetere il blocco **finché** una certa condizione è vera.

## 🔁 Oggetti Iterabili in Python

In Python, un **oggetto iterabile** è un oggetto che può essere attraversato (cioè, iterato) elemento per elemento. Un iterabile è qualcosa che può **fornire un elemento alla volta** quando usato in un ciclo `for` o quando passato a funzioni come `list()`, `tuple()`, `set()` ecc.

Gli oggetti iterabili sono fondamentali nella programmazione Python e rappresentano una delle basi per lavorare con cicli, liste, generatori e molto altro.

### 🔹 Esempi di oggetti iterabili:

- Liste (`list`)
- Tuple (`tuple`)
- Stringhe (`str`)
- Dizionari (`dict`)
- Insiemi (`set`)
- Oggetti restituiti da funzioni come `range()`, `zip()`, `map()`, `filter()`, ecc.

Un iterabile è un oggetto che **implementa il metodo speciale `__iter__()`**, il quale restituisce un oggetto chiamato **iteratore**.

Un iteratore, a sua volta, implementa il metodo `__next__()`, che permette di ottenere il prossimo elemento nella sequenza.

### 🔍 Come riconoscere un oggetto iterabile

Un modo semplice per verificare se un oggetto è iterabile è provare a usarlo in un ciclo `for`, oppure usare la funzione `iter()` su di esso. Se non è iterabile, Python solleverà un errore `TypeError`.

### 🧠 Cosa succede dietro le quinte?

Quando scriviamo un ciclo `for` come il seguente:

```python
for elemento in sequenza:
    ...
```

Python internamente esegue le seguenti operazioni:

1. Chiama iter(sequenza) per ottenere un iteratore.
2. Chiama next() su quell’iteratore per ottenere il prossimo elemento.
3. Ripete finché non viene sollevata un’eccezione StopIteration, che segnala la fine dell’iterazione.

#### 🧪 Verifica manuale

Possiamo simulare manualmente questo processo usando iter() e next().

### 📌 Tutto ciò che è iterabile non è necessariamente un iteratore

È importante distinguere tra **iterabile** e **iteratore**:

- Un **iterabile** può essere trasformato in un iteratore usando `iter()`.
- Un **iteratore** è un oggetto che implementa `__next__()` e può essere consumato passo dopo passo.

Ogni volta che chiamiamo `iter()` su un iterabile, otteniamo un **nuovo iteratore indipendente**. Tuttavia, un iteratore è **esauribile**: una volta che ha restituito tutti i suoi elementi, non può essere riutilizzato.

## Ciclo `for`

```python
for variabile in sequenza:
    # blocco di codice da ripetere
```



