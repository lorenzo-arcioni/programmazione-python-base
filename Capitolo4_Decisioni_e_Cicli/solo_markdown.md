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

### 🧠 Cosa succede dietro le quinte?

Quando scriviamo un ciclo `for` come il seguente:

```python
for elemento in sequenza:
    ...
```

Python internamente esegue le seguenti operazioni:

1. Chiama `iter(sequenza)` per ottenere un iteratore. 
   - Se `iter()` riceve un oggetto che è già un iteratore, lo restituisce così com'è, senza creare un nuovo oggetto.
2. Chiama `next()` su quell’iteratore per ottenere il prossimo elemento.
3. Ripete finché non viene sollevata un’eccezione StopIteration, che segnala la fine dell’iterazione.

## Ciclo `for`

```python
for variabile in sequenza:
    # blocco di codice da ripetere
```



Any All

