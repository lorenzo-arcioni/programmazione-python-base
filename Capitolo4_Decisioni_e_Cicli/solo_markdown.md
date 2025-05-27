<a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo3_Decisioni/1_If_statement.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 🧠 Decisioni in Python

Le **decisioni** permettono al programma di **scegliere** tra due o più azioni in base a una **condizione logica**.

Questo è un concetto fondamentale nella programmazione: molte volte, vogliamo che il nostro programma si comporti in modo diverso a seconda dei **dati in ingresso**, dello **stato del sistema**, o di qualsiasi altra **situazione contingente**.

Ad esempio:
- Se l'utente ha inserito una password corretta, possiamo farlo accedere. Mentre se l'utente ha inserito una password sbagliata, possiamo mostrare un messaggio di errore.
- Se una temperatura è sopra una certa soglia, possiamo inviare un allarme.
- Se un numero è pari o dispari, possiamo decidere un'azione diversa.

## 🔁 Control Flow: il flusso di controllo

Le decisioni fanno parte di un insieme più ampio chiamato **control-flow statements**. Il **flusso di controllo** (in inglese *control flow*) è il percorso che il programma segue durante la sua esecuzione.

In Python (e in tutti i linguaggi di programmazione), possiamo controllare il flusso di esecuzione del codice tramite tre principali costrutti:
1. **Sequenza**: le istruzioni vengono eseguite una dopo l'altra, in ordine.
2. **Decisioni (condizionali)**: eseguiamo blocchi di codice solo se una certa condizione è vera.
3. **Cicli (iterazioni)**: ripetiamo blocchi di codice finché una condizione è vera o per un certo numero di volte.

Questo capitolo si concentra sul secondo punto: le **decisioni** tramite le istruzioni `if`, `elif` ed `else`.

Imparare a controllare il flusso del programma è essenziale per scrivere codice che **risponda in modo intelligente** alle diverse situazioni e che sia **adattabile**, **efficiente** e **leggibile**.

### 🔢 Operatori di confronto

Gli **operatori di confronto** sono usati per confrontare due valori. Le espressioni che li utilizzano restituiscono sempre un valore booleano: `True` se la condizione è vera, `False` altrimenti.

Sono fondamentali per esprimere condizioni all'interno di costrutti come `if`.

| Operatore | Significato       | Esempio            |
|-----------|-------------------|--------------------|
| `==`      | Uguale            | $5 == 5$ → `True`  |
| `!=`      | Diverso           | $4\ \text{!=} \ 3$ → `True`  |
| `<`       | Minore            | $2 < 5$ → `True`   |
| `>`       | Maggiore          | $5 > 2$ → `True`   |
| `<=`      | Minore o uguale   | $3 <= 3$ → `True`  |
| `>=`      | Maggiore o uguale | $6 >= 7$ → `False` |

## ✅ Il costrutto `if`

Il costrutto `if` è il modo più semplice e diretto per prendere una decisione in Python.

La sintassi generale è:

```python
if condizione: 
    blocco di codice indentato
```

Python valuta la **condizione** (che è un'espressione booleana) e, **se il risultato è `True`**, esegue il blocco di codice sottostante. In caso contrario, lo **salta**.

### 🔍 Esempio semplice

Poiché $5 > 3$ è una condizione vera, l'istruzione `print` verrà eseguita. Al contrario:


### ℹ️ Note importanti

- Il blocco di codice **deve essere indentato** (generalmente con 4 spazi): l'indentazione è fondamentale in Python e definisce i blocchi logici di codice.
- La **condizione** deve restituire un valore booleano (`True` o `False`). Può essere una semplice espressione confrontando numeri, stringhe, variabili, o anche combinazioni più complesse.
- Quando siamo in presenza di una singola istruzione dopo l'`if`, è possibile scriverla anche senza l'indentazione:

```python
if condizione: unica istruzione
```

### ✅ Esempi di condizioni valide

### ➕ Clausola `else`

Serve a specificare un blocco di codice da eseguire **quando la condizione è falsa**.

```python
if condizione:
    Blocco A
else:
    Blocco B
```

Quindi, quando `condizione` ritorna il valore booleano `False`, il **Blocco A** non viene eseguito, mentre il **Blocco B** si!

Esempio:

### 🔁 Clausola `elif`

Serve per testare **più condizioni diverse**:

```python
if condizione1:
    Blocco A
elif condizione2:
    Blocco B
elif condizione3:
    Blocco C
else:
    Blocco D
```

Quindi, Python esamina le condizioni **una alla volta**:

1. Se `condizione1` è vera, esegue **solo il Blocco A** e ignora tutto il resto.
2. Se `condizione1` è falsa ma `condizione2` è vera, esegue il **Blocco B**, e così via.
3. L'`else` finale è **opzionale**, e viene eseguito solo se **tutte le condizioni precedenti sono false**.

✅ È utile quando vuoi controllare **casi distinti**, come ad esempio valutare un voto:

In questo esempio, il programma stampa `"Buono"` perché `85 >= 75` è la prima condizione vera.

## 🔗 Operatori logici

Gli **operatori logici** permettono di combinare più condizioni insieme per costruire espressioni complesse.

- `cond1 and cond2` → Restituisce `True` solo se **entrambe** le condizioni sono vere.
- `cond1 or cond2` → Restituisce `True` se **almeno una** delle due condizioni è vera.
- `not cond` → Inverte il valore logico: se `cond` è `True`, diventa `False`, e viceversa.

Questi operatori vengono spesso usati insieme agli `if` per prendere decisioni basate su **più condizioni**.

Attenzione alla **precedenza degli operatori**:
- `not` ha la precedenza più alta,
- seguito da `and`,
- e infine `or`.

### 📊 Tabella della verità per gli operatori logici

In queste tabelle vediamo come si comportano gli operatori logici `not`, `and` e `or` a seconda dei valori booleani delle condizioni coinvolte. Sono fondamentali per costruire condizioni complesse nei blocchi decisionali (`if`, `elif`, `while`, ecc.).

Gli operatori logici restituiscono sempre un valore booleano (`True` o `False`) e seguono le regole della logica proposizionale.

Nelle tabelle, `A` e `B` sono condizioni con valore booleano.

#### 🔹 Operatore `not`

L'operatore `not` **nega** il valore della condizione: se è `True`, diventa `False` e viceversa.

| `A`     | `not A` |
|---------|---------|
| `True`  | `False` |
| `False` | `True`  |

#### 🔸 Operatore `and`

L'operatore `and` restituisce `True` **solo se entrambe le condizioni** sono vere. Se anche solo una è falsa, il risultato è `False`.

| `A`     | `B`     | `A and B` |
|---------|---------|-----------|
| `True`  | `True`  | `True`    |
| `True`  | `False` | `False`   |
| `False` | `True`  | `False`   |
| `False` | `False` | `False`   |

#### 🔸 Operatore `or`

L'operatore `or` restituisce `True` **se almeno una** delle condizioni è vera. Restituisce `False` solo se **entrambe** sono false.

| `A`     | `B`     | `A or B` |
|---------|---------|----------|
| `True`  | `True`  | `True`   |
| `True`  | `False` | `True`   |
| `False` | `True`  | `True`   |
| `False` | `False` | `False`  |

Queste tabelle aiutano a prevedere il comportamento del programma quando si usano condizioni multiple. È buona pratica usare le parentesi per rendere più chiara la priorità delle operazioni logiche, anche se Python segue delle regole precise su quali operatori vengono valutati prima.

Vediamo subito un esempio!

### 🔗 Confronti concatenati

In Python è possibile concatenare più confronti in un'unica espressione, proprio come in matematica. Ad esempio:

- $4 < 6 < 8$, che equivale a: $(4 < 6)\ \text{and}\ (6 < 8)$ → entrambe le condizioni devono essere vere.

Questa scrittura è più leggibile e Python la interpreta nel modo matematicamente corretto.

## ↩️ Istruzioni su più righe con il carattere `\`

In Python, se una singola istruzione è troppo lunga e si vuole scriverla su più righe per migliorare la leggibilità, si può usare il carattere di **continuazione di linea** `\` alla fine di una riga.

Questo permette a Python di considerare le righe successive come parte della stessa istruzione.

**Nota**: è importante che dopo la barra rovesciata \ non ci siano spazi o altri caratteri diversi da `\n`.

Alternativamente, si possono usare le parentesi tonde () per scrivere espressioni su più righe senza usare \.

## 🎯 Valori booleani impliciti

Python considera alcuni valori come `False` anche senza usare `==`:

| Valore       | Bool |
|--------------|------|
| `0`         | `False` |
| `""`        | `False` |
| `None`      | `False` |

Tutti gli altri valori (del tipo di quelli in tabella) → `True`.

Esempio:

## ✅ Conclusioni

In questo notebook abbiamo approfondito il meccanismo delle **decisioni condizionali** in Python, pilastro fondamentale del control flow.

Abbiamo esplorato:

- La struttura base delle decisioni con `if`, `elif` ed `else`
- Gli **operatori di confronto** (`==`, `!=`, `<`, `>`, `<=`, `>=`) 
- Gli **operatori logici** (`and`, `or`, `not`) e le relative tabelle della verità
- I **confronti concatenati** (es. `4 < x < 10`)
- La gestione dei **valori booleani impliciti** (truthy/falsy values)
- L'importanza dell'**indentazione** per definire i blocchi di codice
- Tecniche per migliorare la leggibilità con condizioni complesse

💡 Padroneggiare le strutture condizionali permette di scrivere codice **dinamico** e **reattivo**, in grado di prendere decisioni intelligenti basate sui dati in input. 

➡️ **Prosegui con il prossimo notebook sui cicli iterativi** per scoprire come automatizzare operazioni ripetitive:
<a href="https://colab.research.google.com/github/percorso/esempio/blob/main/4_Cicli.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

