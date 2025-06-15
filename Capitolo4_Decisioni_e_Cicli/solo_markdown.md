<a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo4_Decisioni_e_Cicli/4_Esercizi.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 🐍 Esercizi Python: Decisioni e Cicli

## 📚 Obiettivi del Notebook

Questo notebook contiene vari esercizi di difficoltà progressiva che combinano:

- ✅ **Statement condizionali** (`if`, `elif`, `else`, `match`)
- 🔁 **Iterabili** (`range`, `enumerate`, `zip`, `reversed`, etc.)
- 🏛️ **Funzioni built-in** (`sum`, `max`, `min`, etc)
- 🔂 **Cicli** (`for`, `while`)
- ⚙️ **Comprehension** (`list`, `set`, `dict` comprehension)
- 🧠 **Tutti gli argomenti visti finora**, con attenzione all'applicazione logica

Gli esercizi sono pensati per metterti alla prova su ogni aspetto appreso, **combinando più concetti insieme**.


## 🎯 Perché gli esercizi sono fondamentali?

Gli esercizi non sono un semplice "test di verifica". Sono **il cuore dell'apprendimento attivo**. Capire la teoria è **fondamentale**, ma è solo una parte: **la vera comprensione avviene quando la metti in pratica**.

### 📌 Ecco perché sono insostituibili:

- **🔁 Passare dalla teoria alla pratica**  
  Leggere, guardare e capire una lezione è solo l'inizio. Quando provi a risolvere un esercizio, ti confronti davvero con la logica del linguaggio.

- **🧠 Sviluppano il pensiero computazionale**  
  Ogni problema è un'occasione per ragionare come si arriva alla soluzione.

- **🧩 Collegano concetti diversi**  
  Gli esercizi ti obbligano a **combinare tra loro vari elementi del linguaggio**, proprio come nei problemi reali: ad esempio condizioni + liste + cicli + metodi + comprehension.

- **🪄 Rafforzano la memoria a lungo termine**  
  Scrivere codice con le proprie mani consolida davvero quello che hai studiato. La ripetizione attiva è la chiave per ricordare.

- **📈 Costruiscono autonomia e sicurezza**  
  Più esercizi risolvi, più ti sentirai padrone del linguaggio. Impari a fidarti delle tue intuizioni e a correggere i tuoi errori.


## 🚀 Come affrontare gli esercizi

Non leggere subito la soluzione:  
1. ✏️ **Prova a risolvere da solo**  
2. 🧠 **Analizza ogni errore come un'opportunità per imparare qualcosa di nuovo!**  
3. 📖 Solo alla fine, **confronta con la soluzione proposta**
4. 👀 La soluzione proposta **non è** l'unica soluzione al problema.   

👨‍💻 Solo scrivendo codice si impara a programmare.  
⚠️ Ricorda: ogni esercizio risolto incrementa la tua preparazione e la tua autonomia 🤓


## 📄 Esercizio 1: Classificatore di Numeri

### 📝 Traccia
Dato un numero intero, determina se è:
- Positivo, negativo o zero
- Pari o dispari (solo se non è zero)
- Piccolo (< 10), medio (10-100) o grande (> 100) in valore assoluto

Salva tutte le classificazioni in un dizionario, con chiavi: "segno", "parità", "grandezza", e stampalo.

## 📄 Esercizio 2: Spesa Strategica

### 📝 Traccia
Hai una lista della spesa che può contenere duplicati e un dizionario con i prezzi unitari di ogni prodotto.

1. Rimuovi i duplicati dalla lista della spesa.
2. Analizza questi **tre** articoli specifici: `'mandarino'`, `'latte'`, `'uova'`.
3. Calcola manualmente il totale parziale di questi tre articoli (solo se presenti).
4. Verifica se questi tre prodotti possono essere acquistati insieme con il budget disponibile.
5. Salva il risultato in un dizionario `verifica` con le seguenti chiavi:
   - `"prodotti"` → lista dei tre articoli selezionati **trovati** nella lista spesa
   - `"costo"` → totale calcolato
   - `"puoi_acquistare"` → `True` o `False` a seconda del confronto col budget

## 📄 Esercizio 3: Analizzatore di Testo Semplice

### 📝 Traccia
Hai un testo da analizzare. Il tuo obiettivo è:
- Calcolare:  
  - numero di caratteri  
  - numero di parole  
  - numero di frasi (solo considerando `.`, `!`, `?`)
- Classificare la **lunghezza** del testo 
  - `molto corto`: meno di 20 caratteri, 
  - `corto`: tra 20 e 49 caratteri, 
  - `medio`: tra 50 e 99 caratteri, 
  - `lungo`: oltre i 100 caratteri,

  usando `match` (per esercizio anche con gli `if`).
- Verificare se il testo **contiene numeri**
- Sia $n = \text{numero di lettere della prima parola}$, calcola $Somma = n + \text{numero di parole del testo ottenuto escludendo gli ultimi } n \text{ caratteri}$.
  - Esempio
    ```python
    testo = "Ciao! Questo è un esempio di testo. Contiene 123 caratteri speciali: @#$."
    prima_parola = testo.split()[0] = "Ciao!"
    testo_ridotto = testo[:-len(prima_parola)] = "Ciao! Questo è un esempio di testo. Contiene 123 caratteri speciali:"
    parole_testo_ridotto = testo_ridotto.split() = ['Ciao!', 'Questo', 'è', 'un', 'esempio', 'di', 'testo.', 'Contiene', '123', 'caratteri', 'speciali:']
    somma = len(prima_parola) + len(parole_testo_ridotto)
    ```
- Costruire una **tupla dei risultati** contenente tutte queste informazioni.

## 📄 Esercizio 4: Contatore di Vocali

### 📝 Traccia
Data una stringa, conta quante volte appare ogni vocale (a, e, i, o, u) usando un ciclo `for`.
Salva i risultati in un dizionario e stampa solo le vocali che appaiono almeno una volta.

## 📄 Esercizio 5: Tabellina con Range

### 📝 Traccia
Crea la tabellina di un numero dato utilizzando `range()` e stampa i risultati in formato elegante.
Inoltre, salva in una lista tutti i risultati pari della tabellina.

Infine, stampa i risultati. L'output deve essere in questo formato

## 📄 Esercizio 6: Analisi Lista Numeri

### 📝 Traccia
Data una lista di numeri, usa un ciclo `for` con `enumerate()` per:
- Trovare la posizione del numero più grande
- Contare quanti numeri sono maggiori della media
- Creare una nuova lista con i numeri delle posizioni pari (indice 0, 2, 4, ...)
- Stampare tutti i risultati.

Qui sotto, un esempio di input e di output:

### 📄 Esercizio 7: Dizionario Invertito

#### 📝 Traccia
Dato un dizionario con nomi di studenti e i loro voti, usa un ciclo `for` per:
- Creare un dizionario invertito dove le chiavi sono i voti e i valori sono liste di studenti
- Trovare il voto più frequente
- Contare quanti studenti hanno la sufficienza (voto >= 6)
- Stampare i risultati

Qui sotto, un esempio di input e di output.

## 📄 Esercizio 8: Pattern con Nested For

### 📝 Traccia
Crea un pattern triangolare usando cicli `for` annidati:
- Il triangolo (rettangolo a sx) deve avere `n` righe
- Ogni riga `i` deve contenere `i` asterischi
- Calcola anche il numero totale di asterischi stampati

Per un esempio di output, eseguire la cella *soluzione*.

### 📄 Esercizio 9: Indovina il Numero

#### 📝 Traccia
Simula un gioco dove l'utente deve indovinare un numero segreto.
Usa un ciclo `while` per continuare fino a quando non indovina.
Per simulare l'input utente, usa una lista di tentativi predefiniti.

Anche qui, esegui la cella soluzione per un esempio do output. Ma mi raccomando, non sbirciare più di tanto 😉


## 📄 Esercizio 10: Countdown con Condizioni

### 📝 Traccia
Crea un countdown da un numero iniziale a 0, ma:
- Salta i numeri multipli di 3
- Se incontri un numero che finisce per 7, fermati immediatamente
- Conta quanti numeri hai effettivamente stampato

Ecco qui un esempio di output:

### 📄 Esercizio 11: Accumula fino a Soglia

#### 📝 Traccia
Data una lista di numeri, usa un ciclo `while` per:
- Sommare i numeri uno alla volta
- Fermarsi quando la somma supera una soglia data
- Tenere traccia di quanti numeri sono stati sommati
- Stampa i risultati

Ecco un esempio di esecuzione:

### 📄 Esercizio 12: Ricerca con While

#### 📝 Traccia
Data una lista di parole, cerca la prima parola che:
- Ha più di 5 caratteri
- Contiene la lettera 'a'
- Non inizia con una maiuscola

Stampa la parola trovata e il numero di parole controllate fino a quel punto.

**Hint.** sono congiunzioni di condizioni, quindi si usa `and`!

Usa un ciclo `while` e conta quante parole hai controllato prima di trovare quella giusta.

### 📄 Esercizio 13: Sequenza di Fibonacci con While

#### 📝 Traccia
Genera la sequenza di Fibonacci usando un ciclo `while` fino a quando non raggiungi un numero maggiore di 100. 

*La successione di Fibonacci è una sequenza di numeri in cui ogni numero è la somma dei due numeri precedenti, iniziando da 0 e 1. La sequenza è 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...*

Inoltre: 

- Salva tutti i numeri pari della sequenza in una lista separata
- Conta quanti numeri della sequenza sono divisibili per 3
- Stampa la sequenza di Fibonacci, la sua lunghezza, i numeri pari e il numero di numeri divisibili per 3 nella sequenza.

Anche qui, esegui la cella *soluzione* per un esempio di esecuzione.

