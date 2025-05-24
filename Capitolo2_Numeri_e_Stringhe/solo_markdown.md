# 🧬 Le Stringhe

In Python, una **stringa** (o *string*) è una sequenza ordinata e immutabile di caratteri Unicode. Questo significa che ogni carattere in una stringa ha una posizione ben definita (indicizzata) e che, una volta creata, una stringa **non può essere modificata direttamente**: tutte le operazioni che sembrano "modificare" una stringa restituiscono in realtà una **nuova stringa**.

Le stringhe sono fondamentali nella programmazione: rappresentano testi, parole, frasi, ma anche dati non testuali come codici, identificativi e persino contenuti di file.

## 🔤 Sintassi di base

Una stringa può essere definita in diversi modi, usando:
- **Apici singoli**: `'ciao'`
- **Apici doppi**: `"ciao"`
- **Triple virgolette** (singole o doppie): `'''ciao'''` oppure `"""ciao"""`, utili per stringhe su più righe (*multilinea*).

Python non distingue tra apici singoli e doppi: entrambi sono equivalenti. Questo consente una maggiore flessibilità, ad esempio per includere virgolette all'interno di una stringa senza dover usare il carattere di escape `\`.

## 🔡 Caratteri Speciali nelle Stringhe

In Python, i caratteri speciali sono rappresentati da sequenze di escape, che iniziano con una barra rovesciata (`\`) seguita da un carattere con un significato particolare.

### Principali Sequenze di Escape

- `\n` : Nuova linea (line break)
- `\t` : Tabulazione orizzontale
- `\\` : Backslash letterale
- `\'` : Apostrofo
- `\"` : Virgolette doppie
- `\r` : Ritorno carrello
- `\b` : Backspace
- `\f` : Form feed
- `\ooo` : Valore ottale
- `\xhh` : Valore esadecimale

Queste sequenze sono utili per includere caratteri non stampabili o che altrimenti avrebbero un significato speciale nel codice, come ad esempio le virgolette o il carattere di nuova linea.

### 🧵 Stringhe raw (`r"..."`)

Le **stringhe raw** (grezze) si definiscono anteponendo una `r` o `R` davanti alle virgolette: `r"testo"`.  
Queste stringhe **non interpretano i caratteri di escape**, come `\n`, `\t`, ecc.

Sono molto utili, ad esempio, quando si scrivono **percorsi di file su Windows** o **espressioni regolari**, perché evitano la doppia scrittura delle barre rovesciate (`\\`).

#### Esempi di confronto:

- `"C:\\Users\\Nome"` interpreta `\\` come `\`
- `r"C:\Users\Nome"` lascia la barra singola così com'è

### 📏 La funzione `len()`

La funzione `len()` restituisce la lunghezza di una stringa, cioè il numero totale di caratteri che contiene.  
Ad esempio,

È molto utile per conoscere la dimensione della stringa e per lavorare con indici validi.

# 🔢 Indicizzazione e Slicing delle Stringhe

In Python, le **stringhe** sono sequenze ordinate di caratteri. Ogni carattere occupa una posizione numerica chiamata **indice**, che può essere positivo (da sinistra verso destra, partendo da 0) o negativo (da destra verso sinistra, partendo da -1).

## 🎯 Indicizzazione

L'indicizzazione permette di accedere a un singolo carattere di una stringa. La sintassi è:

- $s[i]$ → restituisce il carattere all'indice $i$

Esempio:

Gli **indici negativi** permettono di accedere ai caratteri partendo dalla fine della stringa: $-1$ corrisponde all’ultimo carattere, $-2$ al penultimo, e così via. Questo è utile per lavorare con la coda di una stringa **senza conoscerne la lunghezza**.

### Attenzione

- Se l'indice non esiste, Python restituisce un errore di tipo `IndexError`.
- Se l'indice non e' intero, Python restituisce un errore di tipo `TypeError`.
- Se la stringa è vuota, Python restituisce un errore di tipo `IndexError`.

## ✂️ Slicing

Lo slicing consente di ottenere **sottostringhe** specificando un intervallo di indici. La sintassi generale è:

- $s[inizio:fine:passo]$

Dove:
- $inizio$ è l'indice da cui si parte (incluso)
- $fine$ è l'indice fino a cui si arriva (escluso)
- $passo$ indica ogni quanti caratteri prendere (default è $1$)

Esempi:

### 🧩 Perché `s[2:4:-1]` restituisce una stringa vuota?

Quando si usa uno slicing con passo negativo (ad esempio `-1`), l'indice iniziale deve essere maggiore dell'indice finale per estrarre caratteri andando all'indietro.  
Nel caso di `s[2:4:-1]`, l'indice iniziale (2) è minore dell'indice finale (4), quindi non viene selezionato nessun carattere e la stringa risultante è vuota (`''`).

Infatti, invertendo il 4 con il 2,

### 🔄 Perché `s[::-1]` funziona?

Con `s[::-1]` entrambi gli indici `start` e `end` sono omessi:  
- Quando il passo è negativo, Python assume per default `start = len(s) - 1` (l’ultimo carattere)  
- e `end = -len(s) - 1` (virtualmente prima del primo carattere).  

Poiché `start > end` e il passo è -1, Python scorre all’indietro tutta la stringa, restituendo la versione invertita.

### ✅ Suggerimenti

- Usa `$len(s)$` per ottenere la lunghezza della stringa.
- Lo slicing **non** genera errore se gli indici sono fuori range: restituirà semplicemente la parte disponibile.
- Il `passo` può essere negativo per ottenere la stringa in ordine inverso.

## ➕ Operazioni su stringhe

Le **stringhe** in Python supportano varie operazioni grazie alla loro natura di sequenze.  
Ecco le due operazioni più comuni:

- **Concatenazione (`+`)**  
  Permette di unire due o più stringhe in una nuova stringa.  
  ➤ Esempio: $"Hello" + " " + "World"$ produce la stringa $"Hello World"$.

- **Ripetizione (`*`)**  
  Permette di ripetere una stringa un certo numero di volte.  
  ➤ Esempio: $"ha" * 3$ produce la stringa $"hahaha"$.

> 🔒 Ricorda: le stringhe sono **immutabili**, quindi ogni operazione restituisce una **nuova** stringa senza modificare l'originale.

## 🚫 Immutabilità delle stringhe

Le stringhe non possono essere modificate direttamente. Qualsiasi operazione restituisce una **nuova stringa**.


## 🛠️ Metodi delle Stringhe

In Python, le stringhe non solo supportano operazioni da sequenza (come l'indicizzazione e lo slicing), ma offrono anche una vasta gamma di **metodi specifici**.  
Questi metodi consentono di trasformare, cercare, modificare e verificare il contenuto delle stringhe in modo molto efficace.  
Essendo **immutabili**, ogni metodo restituisce una nuova stringa (o altro valore) lasciando inalterata quella originale.

Vediamo una panoramica dei metodi più comuni, suddivisi per categoria.

### 🔠 Modifica del contenuto: `upper()`, `lower()`, `title()`, `capitalize()`

Questi metodi trasformano il contenuto della stringa modificandone il **case** (cioè maiuscole/minuscole):

- `$str.upper()$` → Tutti i caratteri in **maiuscolo**  
- `$str.lower()$` → Tutti i caratteri in **minuscolo**  
- `$str.title()$` → Ogni parola con l'iniziale maiuscola  
- `$str.capitalize()$` → Solo il primo carattere della stringa in maiuscolo

### 🔍 Ricerca e sostituzione: `find()`, `replace()`

- `str.find(sub)` → Restituisce l’indice della **prima occorrenza** di `sub` o `-1` se non trovata  
- `str.replace(old, new)` → Restituisce una nuova stringa dove **tutte** le occorrenze di `old` sono sostituite con `new`

dove `sub`, `old` e `new` sono stringhe.

### ✂️ Suddividere e unire stringhe: `split()`, `join()`

- `str.split(sep)` → Divide la stringa in una lista di sottostringhe usando `sep` come delimitatore  
- `sep.join(lista)` → Unisce una lista di stringhe in una singola stringa, separandole con `sep`

### ✂️ Rimozione di spazi: `strip()`, `rstrip()`, `lstrip()`

- `str.strip()` → Rimuove spazi (e caratteri di nuova riga) da **entrambe** le estremità  
- `str.rstrip()` → Solo dalla **destra**  
- `str.lstrip()` → Solo dalla **sinistra**

### 🧪 Test di contenuto: `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`

Questi metodi restituiscono **valori booleani**:

- `str.isalpha()` → True se tutti i caratteri sono **lettere**  
- `str.isdigit()` → True se tutti i caratteri sono **cifre**  
- `str.isalnum()` → True se tutti i caratteri sono lettere o cifre  
- `str.isspace()` → True se contiene **solo spazi o caratteri di spaziatura**

## 🧾 Formattazione delle stringhe

Python offre diverse modalità per incorporare valori dinamici all'interno delle stringhe. Le principali tecniche di formattazione sono:

1. **Operatori con `%`** – vecchio stile, simile al C.
2. **Metodo `.format()`** – introdotto in Python 2.6/3.0, più leggibile e potente.
3. **f-string (formatted string literals)** – introdotte in Python 3.6, offrono una sintassi concisa e leggibile.

Vediamo ciascun metodo con esempi.

### 🎯 Formattazione con `%`

L'operatore `%` consente di inserire valori in una stringa utilizzando dei segnaposto:

- `%s` → stringa
- `%d` → intero
- `%f` → float

Questa tecnica è ancora usata (in C ad esempio), ma è considerata meno flessibile e più soggetta a errori rispetto ai metodi più moderni.

### 🧩 Formattazione con `.format()`

Il metodo `.format()` consente di inserire valori nei segnaposto `{}` all'interno della stringa. È possibile:

- Usare l'ordine degli argomenti
- Specificare indici
- Usare argomenti nominati

È più leggibile e versatile del vecchio metodo con `%`.

### ⚡ f-string (Formatted String Literals)

Le f-string sono stringhe che iniziano con `f` e permettono di inserire direttamente espressioni Python nei segnaposto `{}`.

Sono concise, efficienti e leggibili. Possono anche contenere espressioni complesse o chiamate a funzioni.

## 🔚 Inizio, Fine e Conteggio di Sottostringhe

Python offre metodi molto utili per controllare se una stringa **inizia**, **termina** o **contiene** una certa sottostringa, o per **contarne le occorrenze**.

### 🚀 `startswith()` e `endswith()`

- `s.startswith(prefix)` → restituisce `True` se la stringa `s` **inizia con** `prefix`
- `s.endswith(suffix)` → restituisce `True` se la stringa `s` **termina con** `suffix`

Entrambi accettano anche tuple di stringhe per controllare più alternative.

📌 **Esempi:**

### 🔍 `in` → Controllo di sottostringa

- `substr in s` → restituisce `True` se la sottostringa `substr` è **contenuta** nella stringa $s$

📌 **Esempi:**

### 🔢 `count()` → Conteggio di occorrenze

- `s.count(substr)` → restituisce **quante volte** `substr` appare in `s`

📌 **Esempi:**

## 📚 Ottenere aiuto e scoprire metodi

Python offre strumenti molto utili per esplorare gli oggetti e scoprire quali metodi o attributi possiedono.

- La funzione `dir()` restituisce una lista di tutti i metodi e attributi disponibili per un oggetto.
- La funzione `help()` fornisce la documentazione dettagliata su un metodo o un oggetto specifico.

Questi strumenti sono essenziali per imparare a usare efficacemente le librerie e i tipi di dato, specialmente quando si inizia a lavorare con nuovi oggetti o moduli.

## 🧵 Pattern Matching con il modulo `re` (regex)

Il modulo `re` permette di usare **espressioni regolari (regex)** per cercare, sostituire o verificare schemi all'interno di stringhe.

### ✨ Funzioni principali del modulo `re`:

- `re.search(p, s)` — Cerca la **prima corrispondenza** del pattern `p` nella stringa `s`.
- `re.findall(p, s)` — Restituisce **tutte le corrispondenze** trovate.
- `re.sub(p, r, s)` — Sostituisce in `s` tutte le corrispondenze di `p` con `r`.
- `re.match(p, s)` — Verifica se la stringa `s` **inizia** con il pattern `p`.

### 🔤 Alcuni simboli utili nei pattern:

- `\d` → una cifra (`0-9`)
- `\w` → un carattere alfanumerico (`a-z`, `A-Z`, `0-9`, `_`)
- `.` → qualunque carattere (eccetto newline)
- `^` → inizio stringa
- `$` → fine stringa
- `+` → uno o più elementi
- `*` → zero o più elementi

🧪 I pattern si scrivono spesso come **stringhe raw**: `r"..."`  
Così non serve raddoppiare i backslash (es: `r"\d+"` invece di `"\\d+"`).

### ℹ️ Nota

Le regex sono molto potenti anche solo con i costrutti di base.  
Per esplorare ed esercitarsi, si consiglia: [regex101.com](https://regex101.com)

## 🧮 Confronto tra Stringhe e Ordinamento

In Python è possibile **confrontare** due stringhe utilizzando gli operatori di confronto standard:  
`==`, `!=`, `<`, `>`, `<=`, `>=`.

### 🔤 Come funziona il confronto?

Python confronta le stringhe **carattere per carattere**, in base ai **codici Unicode** dei caratteri.  
Questo significa che:

- `"a" < "b"` perché il codice Unicode di `"a"` è minore di quello di `"b"`.
- `"abc" < "b"` perché il confronto parte dal primo carattere: `"a"` è minore di `"b"`.
- `"Z"` è **minore** di `"a"` perché le lettere maiuscole vengono **prima** delle minuscole in Unicode.

### 📚 Ordine Unicode

Ecco alcuni codici Unicode comuni:

- `"A"` → 65
- `"Z"` → 90
- `"a"` → 97
- `"z"` → 122

Puoi verificarli con `ord()`

### 🔢 Funzione `ord()`

La funzione `ord()` prende un singolo carattere (stringa di lunghezza 1) e restituisce il suo **codice Unicode** come numero intero.

Questo codice rappresenta la posizione del carattere nella tabella Unicode, che Python usa per confrontare e ordinare le stringhe.

**Esempio:**

- `ord('A')` restituisce 65
- `ord('a')` restituisce 97

È molto utile per capire l'ordine lessicografico e fare confronti basati sui valori numerici dei caratteri.

## Tabella Unicode dei Caratteri Comuni

La tabella sottostante mostra alcuni caratteri comuni insieme ai loro codici Unicode in formato esadecimale e decimale, come visualizzati dalla funzione ord() in Python.
<br>
<img src="https://naveenr.net/content/images/2017/03/ascii-codes.gif" alt="Tabella Unicode" width="600"/>

Descrizione:

- La colonna `Char` mostra il simbolo visualizzato.

- Le colonne `Hex` e `Dec` rappresentanca il valore Unicode del carattere (es. `41` per 'A').

- La funzione `ord()` restituisce il codice Unicode in forma decimale (es. `65` per 'A').

- Unicode è uno standard che assegna un numero univoco a ogni carattere, indipendentemente dalla piattaforma, programma o lingua.

Questa tabella è utile per comprendere come Python rappresenta internamente i caratteri e come funziona la codifica Unicode.

## 📜 Stringhe Multilinea

In Python, le stringhe multilinea permettono di scrivere testi che si estendono su più righe, mantenendo la formattazione originale.

### Come si definiscono?

Si usano le **triple virgolette** (singole o doppie):

```python
'''testo 

su più 

righe

'''

"""
testo 
su più 
righe
"""

```

Questa sintassi è molto comoda per:

- Documentare funzioni (docstring)
- Scrivere blocchi di testo lunghi
- Includere caratteri di nuova linea senza usare `\n`

### Caratteristiche

- Mantengono gli spazi e i ritorni a capo esattamente come scritti.
- Possono contenere sia apici singoli che doppi senza bisogno di escape.
- Sono immutabili come tutte le stringhe in Python.

## ✅ Conclusioni

In questo notebook abbiamo esplorato in profondità il mondo delle **stringhe** in Python, un tipo di dato fondamentale per la programmazione.

Abbiamo imparato:

- Come **definire** e **rappresentare** stringhe, anche su più righe con le **stringhe multilinea** (triple virgolette)
- A usare i **caratteri speciali** e le **stringhe raw** per gestire sequenze di escape e percorsi
- A lavorare con **indicizzazione** e **slicing** per accedere e manipolare sottostringhe in modo flessibile
- Le principali **operazioni** sulle stringhe: concatenazione (`+`), ripetizione (`*`), e gli operatori di confronto (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Il concetto di **immutabilità** delle stringhe, che implica che ogni modifica crea una nuova stringa
- I principali **metodi utili** per trasformazione, ricerca, suddivisione e verifica (`upper()`, `split()`, `replace()`, `isalpha()` ecc.)
- Le diverse **modalità di formattazione** delle stringhe: con l’operatore `%`, il metodo `.format()`, e le moderne f-string
- Come ottenere **aiuto** e scoprire i metodi disponibili con le funzioni `dir()` e `help()`
- I fondamenti del **pattern matching** con il modulo `re`, per espressioni regolari semplici e potenti

💡 Le stringhe in Python sono strumenti estremamente potenti e versatili per lavorare con testi, dati strutturati, input/output e molto altro.

➡️ Continua con gli esercizi o il prossimo capitolo  per mettere in pratica quanto appreso!

