# 🧩 Funzioni

Le **funzioni** sono uno dei concetti fondamentali della programmazione. Servono a **suddividere un programma in blocchi logici**, ognuno dei quali svolge un compito specifico.

In termini semplici, una funzione è un **insieme di istruzioni** che possiamo **riutilizzare** ogni volta che serve, senza doverle riscrivere da capo.

## 🤔 Perché usare le funzioni?

Immagina di dover calcolare la media di una lista di numeri in vari punti del tuo programma. Se scrivessi le stesse istruzioni ogni volta, il codice diventerebbe **lungo, ripetitivo e difficile da leggere**.

Le funzioni permettono di:

- 📦 **Raggruppare** le istruzioni che compiono un'azione precisa.
- 🔁 **Riutilizzare** quel blocco ogni volta che serve, semplicemente chiamandolo.
- 🧹 **Migliorare la leggibilità** del codice, rendendolo più ordinato e più facile da capire.
- 🛠️ **Facilitare la manutenzione**: se devi correggere un errore o migliorare una parte, ti basta modificare la funzione, e il cambiamento avrà effetto ovunque essa sia usata.


## 🔧 Com’è fatta una funzione?

Una funzione in Python è composta da:

1. **Parola chiave `def`** → Va inserita prima del nome della funzione.
2. **Un nome** → per poterla richiamare nel codice.
3. **Una lista di parametri (opzionale)** → per passare dei dati alla funzione.
4. **Un corpo** → che contiene le istruzioni da eseguire.
5. **Un valore restituito (opzionale)** → che può essere usato nel resto del programma.

💬 Detto altrimenti: una funzione può **ricevere informazioni**, **fare qualcosa con esse** e **restituire un risultato**.

Vediamo subito un esempio pratico. 

### 🧪 Esempio
Immagginiamo di avere due numeri e di voler calcolare la loro somma.

`somma_due_numeri(numero1, numero2)` è la funzione che prende in input due numeri (due variabili di tipo numerico), ne calcola la somma, e restituisce il risultato.

### 🧪 Esempio
Immagginiamo di avere una lista e di voler calcolare la media armonica degli elementi al suo interno.

Ricordiamo però prima come è definita la media armonica.

*La **media armonica** di una lista di $n$ numeri positivi si calcola con la formula:*

$$
\text{Media armonica}(lista) = \frac{n}{\sum_{i=1}^{n} \frac{1}{x_i}}
$$

### 🧾 Analisi dell’esempio

- `media_armonica` è la funzione.
- `lista_numeri` è il **parametro**: accetterà una lista di numeri al momento della chiamata.
- `[4, 5, 5]` è l’**argomento** passato alla funzione.
- Il risultato è calcolato usando la formula della media armonica.

📌 In questo modo, possiamo riutilizzare la funzione per **qualsiasi lista di numeri positivi**, cambiando solo l’argomento.

## 📥 Parametri e argomenti

Quando definiamo una funzione, possiamo **dichiarare dei parametri**, cioè **variabili che accetteranno dei valori** ogni volta che la funzione viene chiamata. Questi valori si chiamano **argomenti**.

👉 Esempio concettuale:

- La funzione si aspetta due numeri (i parametri).
- Quando la chiamiamo, gliene passiamo due (gli argomenti).
- La funzione usa quei numeri per fare un calcolo.

Se una funzione **non ha bisogno di dati in ingresso**, possiamo definirla **senza parametri**.

Quindi, 

👉 I **parametri** si dichiarano nella **definizione** della funzione.  

```python
def funzione(parametro_1, parametro_2):
```

👉 Gli **argomenti** sono i **valori reali** che passiamo alla funzione **quando la chiamiamo**.

```python
funzione(argomento_1, argomento_2)
```

### 🧠 Osservazioni importanti

- Una funzione può avere **zero, uno o più parametri**.
- Gli argomenti che passiamo **devono corrispondere** (per numero e ordine) ai parametri previsti dalla funzione.
- Una funzione può essere riutilizzata più volte con **argomenti diversi**, proprio grazie alla flessibilità dei parametri.

### 📐 Annotazioni di tipo

In Python possiamo **specificare il tipo atteso di ciascun parametro** usando i due punti `:`. Questo si chiama annotazione di tipo e rende il codice più leggibile e sicuro.

- `a: int` → il parametro a dovrebbe essere un intero

- `-> int` → la funzione dovrebbe restituire un intero

⚠️ Python non obbliga a rispettare questi tipi (non è un linguaggio strettamente tipizzato), ma strumenti esterni come editor, IDE e controlli statici possono segnalare errori se il tipo è errato.

Infatti, come possiamo notare, la funzione `somma` non dà errore se passiamo due stringhe come argomenti invece che due interi.

### 🔢 Ordine degli argomenti

L’ordine degli argomenti è **fondamentale**: quando chiamiamo una funzione, Python **abbina il primo argomento al primo parametro**, il secondo al secondo, e così via.

> ⚠️ Cambiare l’ordine degli argomenti può cambiare il significato della funzione!

### 🧰 Argomenti di default

Quando definiamo una funzione, possiamo **assegnare un valore di default** a uno o più parametri. In questo modo, la funzione può essere chiamata **anche senza fornire tutti gli argomenti**.

```python
def saluta(nome, lingua='it'):
```

- Se non specifichiamo `lingua`, verrà usato il valore `'it'`.
- Possiamo comunque passare un valore diverso durante la chiamata.

I parametri con valore di default devono essere scritti **dopo** quelli obbligatori.

### 🏷️ Argomenti con nome (keyword arguments)

È possibile specificare gli argomenti usando il nome del parametro, anche **fuori ordine**:

```python
saluta(lingua='en', nome='Alice')
```

Questo approccio rende il codice più leggibile, soprattutto se ci sono molti parametri.

### 🧭 Riepilogo

| Tipo di argomento | Descrizione |
|-------------------|-------------|
| Posizionale        | Viene assegnato in base all’ordine |
| Di default         | Ha un valore predefinito se non viene passato |
| Con nome (keyword) | Viene assegnato esplicitamente usando `nome=valore` |


## 📤 Valore di ritorno

Una funzione può **restituire un risultato** al codice che l’ha invocata. Questo risultato si chiama **valore di ritorno** (*return value*).

### 🎯 A cosa serve il valore di ritorno?

Restituire un valore da una funzione è utile perché permette di:

- **Salvare il risultato in una variabile**, così possiamo usarlo in un secondo momento nel programma.
- **Usarlo direttamente in un’altra espressione**, ad esempio in un calcolo matematico o come input di un'altra funzione.
- **Visualizzarlo o elaborarlo** in modi differenti, a seconda delle necessità del programma.

### 🧠 Cosa succede se non restituiamo nulla?

Se una funzione **non specifica esplicitamente un valore di ritorno**, Python restituisce automaticamente un valore speciale chiamato `None`. Questo valore rappresenta l'assenza di un risultato, ed è spesso utilizzato per indicare che la funzione ha semplicemente svolto un compito (come stampare un messaggio), ma **non produce un valore da usare altrove**.

## 🧭 Importante: `print` e `return` non sono la stessa cosa

- `print` serve a **mostrare qualcosa sullo schermo**, per farlo leggere all’utente.
- `return` serve a **restituire un valore al programma**, così che possa essere **usato** o **memorizzato**.

Anche se il risultato visivo può sembrare simile, i due meccanismi hanno scopi molto diversi.

Quando una funzione **usa `return`**, il valore torna al punto del programma in cui la funzione era stata chiamata. Questo è ciò che rende le funzioni **riutilizzabili e componibili**, perché possono fornire risultati su cui continuare a lavorare.

Da notare che quando eseguiamo il **return** all'interno di una funzione, questa **ritorna immediatamente** al punto in cui è stata chiamata, ignorando qualsiasi altra istruzione che eventualmente si trovasse dopo il return stesso.

Questo significa che:

- Tutte le istruzioni dopo il **return** non vengono eseguite.
- Il valore specificato nel return viene “trasportato” fuori dalla funzione.
- Se la funzione non ha un return esplicito, alla fine restituisce automaticamente il valore speciale `None`.

### Perché questo è importante?

- Il **return** permette di decidere **quando e cosa** restituire come risultato, anche in base a condizioni specifiche.
- Si può usare per uscire **anticipatamente** da una funzione quando, ad esempio, si incontra un errore o una condizione particolare.
- Garantisce che la funzione produca sempre un valore coerente (o nessun valore) al chiamante.

### Esempi tipici di utilizzo del return anticipato

- Verifica di input non valido per fermare subito l’esecuzione.
- Uscita da una funzione dopo aver trovato il risultato desiderato (come in una ricerca).
- Suddivisione di casi diversi usando più return in punti differenti della funzione.

## 🧭 Chiamare una funzione

Una volta definita, una funzione può essere **chiamata** nel nostro programma, scrivendo il suo nome e, se richiesti, passando gli argomenti tra parentesi tonde.

Chiamare una funzione significa **far partire il suo codice** e ottenere, se previsto, un risultato.

### 📌 Cosa succede quando chiamiamo una funzione?

1. Python **sospende temporaneamente** l’esecuzione del programma nel punto in cui si trova la chiamata.
2. Viene eseguito **tutto il codice contenuto nella funzione**, riga dopo riga.
3. Se la funzione contiene un’istruzione `return`, viene restituito il valore specificato e l’esecuzione della funzione termina. Se non c'è l'istruzione `return`, la funzione restituisce automaticamente `None`.
4. Python **riprende l’esecuzione del programma** nel punto in cui la funzione era stata chiamata, utilizzando eventualmente il valore restituito (che viene sostituito alla chiamata della funzione).

### 🧠 Esempio esplicativo:

**Cosa succede passo dopo passo:**

- Python stampa: `Prima della chiamata della funzione`
- Python incontra `saluta("Alice")`, sospende il flusso principale e entra nella funzione.
- Dentro `saluta`, stampa: `Ciao, Alice!`
- La funzione restituisce la stringa `"Saluto inviato a Alice"`.
- Python riprende il flusso principale e assegna il valore restituito alla variabile `messaggio`.
- Python stampa: `Dopo la chiamata della funzione`
- Infine, stampa il contenuto di `messaggio`: `Saluto inviato a Alice`

### 🔄 Più chiamate della stessa funzione

Una funzione può essere chiamata più volte con argomenti diversi:

Ogni chiamata è indipendente e produce un risultato basato sugli argomenti passati.

### ⚠️ Attenzione

- Se dimentichi di mettere le parentesi tonde `()` dopo il nome della funzione, non la chiami ma **ottieni solo un riferimento alla funzione stessa**.


- Per **eseguire realmente** la funzione devi includere le parentesi e, se richiesti, gli argomenti.

## 📌 Differenza tra definizione e chiamata

È importante non confondere:

- **Definizione** → serve a **creare** la funzione, specificandone nome, parametri e corpo.
- **Chiamata** → serve a **usare** la funzione, cioè farla eseguire.

Una funzione può essere **definita una sola volta**, ma **chiamata quante volte vuoi**, anche in punti diversi del programma.

## 🧼 Scope delle variabili

Lo **scope** (ambiente) di una variabile definisce **dove** essa è accessibile nel codice. In Python, esistono principalmente due scope:

- **Scope locale**: variabili create all'interno di una funzione.
- **Scope globale**: variabili create al di fuori di tutte le funzioni, visibili in tutto il modulo.

### 🔒 Scope locale: variabili dentro la funzione

Quando dichiariamo una variabile **all'interno** di una funzione, questa vive solo per la durata della funzione stessa. 

- La variabile è **creata quando la funzione viene chiamata**.
- Esiste solo durante l'esecuzione della funzione.
- Scompare non appena la funzione termina.
- Non è accessibile al di fuori della funzione (tentare di usarla fuori genera un errore).

Questo permette alle funzioni di avere variabili “private” che non interferiscono con il resto del programma.

### 🌍 Scope globale: variabili fuori dalla funzione

Le variabili definite **fuori** da tutte le funzioni sono dette **globali**. 

- Sono visibili e accessibili da qualunque punto del programma, incluse le funzioni.
- Possono essere **lette** dentro una funzione senza problemi.

Tuttavia, **modificare una variabile globale dentro una funzione senza una dichiarazione esplicita** causa un problema: Python interpreta la variabile come una **locale** e, se la si usa prima di assegnarle un valore, si ottiene un errore.


Questo genera un errore `UnboundLocalError` perché Python pensa che `x` dentro la funzione sia una variabile locale, ma viene usata prima di essere inizializzata.

### 📌 Modificare variabili globali dentro funzioni

Se vuoi **modificare una variabile globale** dentro una funzione, devi usare la parola chiave speciale `global` per indicare a Python che ti riferisci alla variabile globale e non a una nuova locale.

### 📌 Buone pratiche

- **Evita di modificare variabili globali dentro le funzioni.** Questo può creare confusione e errori difficili da trovare.
- Preferisci **passare variabili come parametri** e usare il valore di ritorno per aggiornare i dati.
- Mantieni le funzioni indipendenti e senza effetti collaterali.

### 🧩 Riassumendo

| Scope       | Dove si definisce       | Visibilità                        | Durata                         | Modifica dentro funzione      |
|-------------|-------------------------|---------------------------------|-------------------------------|------------------------------|
| Locale      | Dentro funzione         | Solo dentro la funzione          | Solo durante l'esecuzione      | Sempre possibile              |
| Globale     | Fuori da tutte le funzioni | In tutto il modulo (file)        | Per tutta la durata del programma | Solo con `global` o `nonlocal` |

## 🎯 Obiettivi delle funzioni

Scrivere funzioni serve a:

- **Semplificare il codice** suddividendo il problema in sottocompiti.
- **Evitare ripetizioni**, grazie al riutilizzo.
- **Aumentare la leggibilità**: ogni funzione ben scritta descrive in modo chiaro cosa fa.
- **Facilitare la collaborazione**: in progetti di gruppo, diversi membri possono occuparsi di funzioni diverse.

## 🧪 Buone pratiche

- 📛 Dai nomi chiari e descrittivi alle funzioni.
- ✂️ Crea funzioni brevi, che svolgono un solo compito.
- 📚 Documenta ogni funzione, spiegando cosa fa, quali parametri accetta e cosa restituisce.
- 🔄 Usa i parametri e il valore di ritorno per **rendere le funzioni riutilizzabili in contesti diversi**.

## ✅ Conclusione

In questa introduzione abbiamo visto che:

- Le **funzioni** servono a **organizzare e semplificare** il codice.
- Una funzione ha **parametri in ingresso** e può **restituire un risultato**.
- Le funzioni migliorano la **leggibilità, la manutenibilità e il riuso** del codice.
- È essenziale comprendere la **differenza tra definizione e chiamata**, e il concetto di **scope**.

➡️ Nel prossimo passo vedremo **cosa sono le funzioni anonime** in Python!


