<a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo4_Decisioni_e_Cicli/3_For_e_While.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 🔁 Cicli in Python
I cicli sono uno degli strumenti più potenti nella programmazione, permettendo di automatizzare processi ripetitivi e gestire operazioni complesse in modo efficiente. In Python, l'uso corretto dei cicli non solo migliora la leggibilità del codice, ma ne aumenta anche la manutenibilità e la scalabilità. Sono uno strumento fondamentale per evitare **ripetizioni inutili** nel codice e per risolvere problemi che richiedono **iterazione**, come ad esempio:
- stampare i numeri da 1 a 100,
- calcolare la somma degli elementi in una lista,
- elaborare una sequenza di dati elemento per elemento,
- chiedere ripetutamente un input valido all'utente.

## 📜 Perché Usare i Cicli?
- **Eliminare la ridondanza**: Evitare di scrivere codice ripetuto manualmente.
- **Gestione dinamica dei dati**: Lavorare con insiemi di dati di dimensioni variabili.
- **Automazione**: Eseguire task complessi senza intervento humano (es. analisi dati, scraping web).
- **Controllo di flusso**: Gestire scenari dove il numero di iterazioni dipende da condizioni runtime.

## 🧭 Tipi di cicli in Python
In Python esistono due principali tipi di ciclo:
1. **`for` loop**: quando sappiamo **quante volte** vogliamo ripetere un blocco di codice (iterazione su una sequenza).
2. **`while` loop**: quando vogliamo ripetere il blocco **finché** una certa condizione è vera.

### 🧠 Cosa succede dietro le quinte?
Quando scriviamo un ciclo `for` come il seguente:
```python
for elemento in sequenza:
    ...
```
Python internamente esegue le seguenti operazioni:
1. Chiama `iter(sequenza)` per ottenere un iteratore. 
   - Se `iter()` riceve un oggetto che è già un iteratore, lo restituisce così com'è, senza creare un nuovo oggetto.
2. Chiama `next()` su quell'iteratore per ottenere il prossimo elemento.
3. Ripete finché non viene sollevata un'eccezione StopIteration, che segnala la fine dell'iterazione.

## 🔄 Ciclo `for`
Il ciclo `for` è ideale quando vogliamo iterare su una sequenza di elementi o quando conosciamo il numero di iterazioni da eseguire.

### Sintassi base
```python
for variabile in sequenza:
    # blocco di codice da ripetere
```

### Oggetti iterabili comuni
- **Liste**: `[1, 2, 3, 4, 5]`
- **Tuple**: `(1, 2, 3, 4, 5)`
- **Stringhe**: `"python"`
- **Dizionari**: `{"a": 1, "b": 2}`
- **Set**: `{1, 2, 3, 4, 5}`
- **Range**: `range(10)`

### 🔢 La funzione `range()`
`range()` è una funzione integrata che genera una sequenza numerica e viene spesso utilizzata nei cicli `for`.

**Sintassi:**
- `range(stop)`: da 0 a stop-1
- `range(start, stop)`: da start a stop-1
- `range(start, stop, step)`: da start a stop-1 con incremento step

### 📊 Iterazione su dizionari
Quando iteriamo su un dizionario, possiamo accedere a:
- **Chiavi**: `dict.keys()`
- **Valori**: `dict.values()`
- **Coppie chiave-valore**: `dict.items()`

Anche nei cicli è presente il concetto di **unpacking**. Possiamo infatti scomporre direttamente elementi iterabili (come tuple, liste o dizionari) in variabili separate durante l'iterazione, rendendo il codice più chiaro e conciso.

Vediamo ora un esempio elggermente più complesso.

### 🎯 Enumerate
La funzione `enumerate()` è utile quando abbiamo bisogno sia dell'indice che del valore durante l'iterazione.

### 🔗 Zip
La funzione `zip()` permette di iterare su più sequenze contemporaneamente, combinando elementi alla stessa posizione.

## ⏰ Ciclo `while`
Il ciclo `while` continua ad eseguire un blocco di codice finché una condizione rimane vera.

### Sintassi base
```python
while condizione:
    # blocco di codice da ripetere
    # importante: modificare la condizione per evitare loop infiniti
```

### ⚠️ Attenzione ai loop infiniti
Un loop infinito si verifica quando la condizione del `while` non viene mai modificata o rimane sempre vera. È importante includere sempre una logica che modifichi la condizione per permettere l'uscita dal ciclo.

### 🎮 Pattern comuni con `while`
- **Validazione input**: Continuare a chiedere input finché non è valido
- **Menu interattivi**: Mostrare opzioni finché l'utente non sceglie di uscire
- **Elaborazione batch**: Processare dati finché non sono finiti

## 🚪 Controllo del flusso nei cicli

### `break` - Uscita immediata
L'istruzione `break` interrompe immediatamente il ciclo e passa alla prima istruzione dopo il blocco del ciclo.

### `continue` - Saltare alla prossima iterazione
L'istruzione `continue` salta il resto del codice nel ciclo corrente e passa direttamente alla prossima iterazione.

### `else` nei cicli
Python offre una caratteristica unica: la clausola `else` nei cicli. Il blocco `else` viene eseguito solo se il ciclo termina naturalmente (senza `break`).

## 🔄 Cicli annidati
I cicli annidati sono cicli all'interno di altri cicli. Sono utili per lavorare con strutture dati bidimensionali come matrici o per combinazioni multiple.

### Considerazioni sulla performance
- I cicli annidati aumentano la complessità temporale
- Un ciclo annidato con due livelli ha complessità O(n²)
- Usare con cautela per grandi dataset

## 🎯 Funzioni utili con i cicli

### `any()` e `all()`
- **`any()`**: Restituisce `True` se almeno un elemento dell'iterabile è vero
- **`all()`**: Restituisce `True` se tutti gli elementi dell'iterabile sono veri

## 🚀 Best Practices

### Efficienza e Performance
- **Evitare modifiche durante l'iterazione**: Non modificare la struttura dati mentre la si itera
- **Usare generatori**: Per grandi dataset, considera l'uso di generatori invece di liste
- **Scegliere il ciclo giusto**: Usa `for` per iterazioni note, `while` per condizioni

### Leggibilità del codice
- **Nomi delle variabili descrittivi**: Usa nomi che descrivono il contenuto
- **Evitare cicli troppo annidati**: Massimo 2-3 livelli di annidamento
- **Utilizzare le comprehension**: Quando appropriate, rendono il codice più pythonic

### Gestione degli errori
- **Validare gli input**: Assicurarsi che gli oggetti siano iterabili
- **Gestire eccezioni**: Catturare possibili errori durante l'iterazione
- **Evitare loop infiniti**: Sempre includere una condizione di uscita

## 🎯 Quando usare quale ciclo?

### Usa `for` quando:
- Devi iterare su una sequenza di elementi
- Conosci il numero di iterazioni
- Lavori con range numerici
- Usi enumerate, zip, o altre funzioni built-in

### Usa `while` quando:
- La condizione di terminazione è complessa
- Non sai quante iterazioni servono
- Implementi logic di retry o validazione
- Gestisci input dell'utente

## 🔧 Debugging dei cicli

### Tecniche comuni
- **Print statements**: Stampare valori durante l'iterazione
- **Contatori**: Tenere traccia del numero di iterazioni
- **Breakpoint**: Usare debugger per fermare l'esecuzione
- **Logging**: Registrare informazioni per analisi successive

### Errori frequenti
- **IndexError**: Accesso a indici non validi
- **KeyError**: Accesso a chiavi inesistenti nei dizionari
- **TypeError**: Tentativo di iterare su oggetti non iterabili
- **Loop infiniti**: Condizioni che non cambiano mai

## ✅ Conclusioni

In questo notebook abbiamo esplorato in profondità il mondo dei **cicli** in Python, uno strumento essenziale per scrivere codice efficiente e leggibile.

Abbiamo imparato:

- A comprendere **perché** e **quando** usare i cicli per automatizzare operazioni ripetitive e lavorare con insiemi di dati
- La differenza tra i due principali tipi di ciclo in Python: **`for` loop** e **`while` loop**, e i contesti d’uso ideali per ciascuno
- Come funziona il ciclo `for` **dietro le quinte**, tramite iteratori e la funzione `next()`
- A utilizzare la funzione **`range()`** per generare sequenze numeriche e iterare su di esse
- A iterare su oggetti come **liste**, **tuple**, **stringhe**, **set** e **dizionari**, sfruttando anche il concetto di **unpacking**
- L'uso avanzato delle funzioni **`enumerate()`** e **`zip()`** per iterazioni più ricche e leggibili
- Come strutturare un ciclo `while` e i pattern più comuni d’uso, facendo attenzione ai **loop infiniti**
- I meccanismi di controllo del flusso con le istruzioni **`break`**, **`continue`**, e la clausola **`else`** nei cicli
- L'importanza e le considerazioni sulle **performance** nell'uso di cicli annidati
- Come sfruttare le funzioni **`any()`** e **`all()`** per controlli rapidi e leggibili sugli elementi iterati
- Le **best practices** per scrivere cicli più leggibili, sicuri ed efficienti
- Tecniche di **debugging** utili per identificare e risolvere errori comuni nei cicli

💡 I cicli sono uno strumento potente e indispensabile per affrontare problemi di ogni complessità.

➡️ Continua con gli esercizi o il prossimo capitolo per mettere in pratica quanto appreso!

<a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo4_Decisioni_e_Cicli/4_Esercizi.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

