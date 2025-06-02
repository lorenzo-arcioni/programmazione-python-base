# 🔐 Tuple

Le **tuple** sono una struttura dati fondamentale in Python, utilizzata per rappresentare collezioni **ordinate** e **immutabili** di elementi.  
Sono strettamente imparentate con le **liste**, ma con una caratteristica chiave: **non possono essere modificate dopo la creazione**.

Comprendere le tuple è essenziale, non solo per memorizzare dati fissi, ma anche per strutturare valori che non devono cambiare accidentalmente.  
Sono spesso utilizzate per rappresentare:

- **Coordinate** (es. posizione in uno spazio 2D o 3D),
- **Valori multipli di ritorno da una funzione**,
- **Record immutabili** (es. dati anagrafici non modificabili),

## 📚 Definizione generale

Una **tupla** è una collezione:

- ✅ Ordinata: gli elementi vengono mantenuti nell’ordine in cui sono stati definiti;
- ✅ Indicizzata: è possibile accedere agli elementi tramite l’indice (es. `tupla[0]`);
- 🚫 Immutabile: una volta creata, **non è possibile aggiungere, rimuovere o modificare** gli elementi;
- ✅ Permette duplicati: possono comparire più volte gli stessi valori;
- ✅ Eterogenea: può contenere oggetti di tipo diverso (interi, stringhe, liste, altre tuple…).


> ✨ Questo rende le tuple **più sicure**, **più veloci**, e adatte a rappresentare **dati costanti**, come le coordinate di un punto, parametri fissi, o record che non devono cambiare.

## 🧪 Esempio base

Ecco come si definisce e si utilizza una tupla in Python:

📌 Nota: anche se le parentesi tonde `()` sono il modo più comune per definire una tupla, **Python riconosce una tupla anche senza parentesi**, se gli elementi sono separati da virgole:

Approfondiremo questo concetto tra poco!

Attenzione alla sintassi: una tupla con un solo elemento richiede la virgola finale!

🧠 È una trappola comune: la virgola è ciò che definisce una tupla, non le parentesi.

## 🔢 Indicizzazione e slicing

Le tuple supportano le stesse tecniche di accesso tramite indice e slicing viste per liste e stringhe:

## ♻️ Immutabilità

La differenza fondamentale tra tuple e liste è proprio questa: le tuple non possono essere modificate.

## 📦 Packing e unpacking

Python permette di **"impacchettare" (packing)** valori in una tupla e **"spacchettarli" (unpacking)** facilmente, rendendo il codice più leggibile e conciso.

### 📦 Packing (impacchettamento)

Il *packing* consiste nel **creare una tupla** a partire da più valori:

📌 Anche se non usi le parentesi tonde, Python interpreta la virgola come creazione di una tupla.

### 🧯 Unpacking (spacchettamento)

L’unpacking consiste nell’**assegnare gli elementi della tupla a variabili distinte**:

⚠️ Il numero di variabili a sinistra deve **corrispondere** al numero di elementi nella tupla, altrimenti si genera un errore.

### 🪄 Unpacking con l'operatore `*`

Puoi usare l’operatore `*` per catturare più elementi in una lista:

> ✨ L’unpacking è molto usato nelle funzioni, nei cicli e per scrivere codice elegante e chiaro.

## 🔍 Operazioni disponibili sulle tuple

Sebbene le tuple siano **immutabili**, possiamo comunque svolgere diverse operazioni utili su di esse:

### 📏 Lunghezza con `len()`

### 🔍 Accesso agli elementi tramite indice

### 🧪 Appartenenza con `in`

### ➕ Concatenazione

### 🔁 Ripetizione

## 🛠️ Tutti i metodi disponibili per le tuple

Le tuple supportano **solo due metodi integrati**:

- `.count(x)` → Conta quante volte `x` appare nella tupla.
- `.index(x)` → Restituisce l’indice della **prima occorrenza** di `x`.

> ⚠️ Al contrario delle liste, **non** puoi usare metodi come `.append()`, `.remove()` o `.sort()` perché modificherebbero la struttura.

## 🧠 Tuple sono hashable

Un oggetto si dice **hashable** quando possiede una caratteristica molto importante: **il suo valore non cambia durante la sua vita**, e quindi può essere associato a un codice numerico fisso chiamato **hash**.

Le **tuple sono oggetti hashable**, il che significa che possono essere utilizzate come **chiavi nei dizionari** o come **elementi nei set**.

Gli oggetti immutabili in Python, come le **tuple**, le **stringhe** e i **numeri**, sono tipicamente hashable, mentre quelli mutabili, come le liste o i dizionari, non lo sono.

> ✅ Una tupla è hashable **solo se tutti i suoi elementi sono hashable**.

Questo implica che:

- Se la tupla contiene solo valori immutabili e hashable (es. numeri, stringhe, altre tuple), allora la tupla stessa è hashable.
- Se invece contiene almeno un elemento non hashable (es. liste, dizionari, set), allora non è hashable e non può essere usata come chiave o elemento di un set.

Essere hashable significa:

- Possedere un valore di hash stabile, calcolabile con `hash()`.
- Consentire un accesso rapido in strutture dati basate su hash (dizionari, set).
- Avere una struttura immutabile che non cambia durante l’esecuzione del programma.

## 🧱 Tuple annidate

Le tuple possono contenere **altre tuple** o strutture dati nidificate al loro interno.  
Questo permette di rappresentare dati complessi mantenendo l’immutabilità e l’ordinamento.

### Caratteristiche principali:

- Le tuple annidate sono utili per rappresentare **record composti**, come un insieme di informazioni correlate.
- È possibile accedere agli elementi annidati usando più indici.
- L’immutabilità vale per tutti i livelli della tupla annidata.

### Esempio tipico:

Una tupla che contiene una tupla al suo interno può rappresentare un **record** con dati raggruppati, ad esempio una persona con nome, cognome e una tupla con anno e corso di iscrizione.

> 🧠 Le tuple annidate permettono una struttura dati compatta, chiara e immutabile.

## ♻️ Conversione tra lista e tupla

In Python, è spesso utile convertire tra **liste** e **tuple** per sfruttare le caratteristiche di entrambi i tipi di dati.

### Perché convertire?

- Le **liste** sono mutabili e comode per modifiche, aggiunte o rimozioni di elementi.
- Le **tuple** sono immutabili e più sicure quando non si vuole permettere modifiche.

### Come convertire?

- Da lista a tupla: usando la funzione `tuple()`.
- Da tupla a lista: usando la funzione `list()`.

> 🔄 La conversione crea una nuova struttura dati, lasciando invariata quella originale.z

## 🔚 Conclusioni

Le **tuple** sono una struttura dati estremamente utile e versatile in Python, soprattutto quando si ha bisogno di una collezione **immutabile** e **ordinata** di elementi.  
La loro immutabilità le rende ideali per rappresentare dati **costanti**, sicuri da modifiche accidentali, e permette di utilizzarle come **chiavi nei dizionari** o come **elementi nei set** grazie alla loro proprietà di essere **hashable** (purché tutti gli elementi contenuti siano a loro volta hashable).

| Caratteristica         | Tuple                                 | Liste                               |
|-----------------------|-------------------------------------|-----------------------------------|
| Mutabilità            | 🚫 Immutabili                        | ✅ Mutabili                       |
| Sintassi              | `(1, 2, 3)` oppure `1, 2, 3`        | `[1, 2, 3]`                       |
| Metodi disponibili    | Solo `.count()`, `.index()`          | Molti: `.append()`, `.remove()`, `.sort()`, ecc. |
| Hashable              | ✅ Solo se tutti gli elementi sono hashable | 🚫 Non hashable                   |
| Performance           | Più veloci e meno spazio in memoria | Leggermente più lente             |
| Uso tipico            | Dati costanti, chiavi dizionario, valori di ritorno multipli | Collezioni modificabili, manipolazioni dati |
| Conversione           | Puoi convertirle in liste con `list()` | Puoi convertirle in tuple con `tuple()` |

Quindi, usa le **tuple** quando vuoi:

- Salvaguardare dati che non devono cambiare.
- Usare sequenze come chiavi di dizionari o elementi di set.
- Avere un contenitore più leggero e performante rispetto alla lista.

Per tutto il resto, dove serve modificare, aggiungere o rimuovere elementi, le **liste** rimangono la scelta migliore.

✨ Comprendere le differenze tra tuple e liste e saperle usare in modo appropriato è una competenza chiave per scrivere codice Python più robusto, leggibile e performante.

