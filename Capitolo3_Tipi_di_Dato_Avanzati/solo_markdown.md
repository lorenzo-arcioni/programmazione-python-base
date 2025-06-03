<a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo3_Tipi_di_Dato_Avanzati/1_Liste.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 📜 Liste

Le **liste** sono una delle strutture dati più importanti e versatili del linguaggio Python. Comprendere appieno il funzionamento delle liste è fondamentale per diventare programmatori competenti, in quanto le liste sono onnipresenti nella scrittura di algoritmi, nell'elaborazione di dati, nella manipolazione di sequenze e in generale in ogni tipo di programmazione procedurale e funzionale.

## 📚 Definizione generale

Una **lista** è una collezione **ordinata**, **indicizzata** e **mutabile** di elementi.  
In termini semplici:
- *Ordinata* significa che gli elementi sono memorizzati secondo l'ordine in cui vengono inseriti.
- *Indicizzata* indica che ogni elemento può essere identificato e accessibile tramite un indice numerico, a partire da zero.
- *Mutabile* significa che è possibile modificare il contenuto della lista (aggiungere, rimuovere o cambiare elementi) **dopo** la sua creazione.

Questo distingue le liste da altre collezioni come le **tuple** (che sono immutabili) o gli **insiemi** (che non sono ordinati né indicizzati).

Vediamo subito un primo esempio in python!

Per ottenere la lunghezza di una lista, utilizziamo la funzione `len()`. Esattamente come nelle stringhe, la funzione `len()` restituisce il numero di elementi nella lista.

## 🧱 Caratteristiche fondamentali

Elenchiamo ora alcune delle caratteristiche più importanti delle liste:

- Una lista può contenere **elementi eterogenei**, ovvero di tipi diversi: numeri, stringhe, booleani, oggetti complessi, altre liste, funzioni e perfino `None`.
- Le liste possono essere **nidificate**, cioè contenere al loro interno altre liste. Questo permette di rappresentare strutture complesse come matrici, tabelle o strutture ad albero.
- Le liste supportano **operazioni di slicing**, ovvero l'accesso a sotto-sequenze tramite intervalli (come abbiamo visto nelle stringhe).
- Essendo **mutabili**, le liste possono essere modificate in modo efficiente in memoria, senza dover creare una nuova lista per ogni cambiamento.

## 🔢 Indicizzazione

Ogni elemento di una lista è accessibile tramite un **indice**. L'indicizzazione in Python parte da `0`, quindi il primo elemento ha indice 0, il secondo indice 1, e così via.  
Gli indici possono anche essere **negativi**, il che permette di accedere agli elementi partendo dalla fine della lista: `-1` rappresenta l'ultimo elemento, `-2` il penultimo, e così via.

$$
\textit{Tutto esattamente come nelle stringhe!}
$$

L'indicizzazione consente un accesso diretto, costante in tempo (complessità $\mathcal O(1)$) a ciascun elemento della lista, una proprietà estremamente utile nelle strutture dati.

## ✂️ Slicing: sotto-liste e accessi parziali

Lo **slicing** è una tecnica per accedere a un sottoinsieme degli elementi di una lista.  
È molto utile per estrarre porzioni, eseguire operazioni su segmenti della lista o costruire nuove liste a partire da quelle esistenti.  
L'intervallo di slicing è sempre **inclusivo a sinistra** e **esclusivo a destra**.  
È possibile anche specificare un **passo** per saltare elementi.

### 🔁 `[::-1]` vs `reverse()` nelle liste

In Python esistono due modi principali per **invertire una lista**, ma funzionano in modo molto diverso.

#### 📌 `[::-1]` — slicing inverso

- ✅ Crea una **nuova lista** invertita.
- 🧠 È una **tecnica funzionale**, non modifica l’originale.
- 📦 Utile in espressioni rapide, ad esempio per stampare all’indietro.

#### 🛠️ `.reverse()` — metodo della lista

- ✅ Modifica la **lista in-place**, cioè direttamente.
- ⚠️ Non restituisce nulla (cioè restituisce `None`), quindi **non si può assegnare** il risultato.
- 💡 Più efficiente se non serve mantenere l’originale.

#### 🧠 Confronto finale

| Metodo        | Crea nuova lista | Modifica in-place | Restituisce risultato |
|---------------|------------------|-------------------|------------------------|
| `[::-1]`      | ✅               | ❌                | ✅                     |
| `.reverse()`  | ❌               | ✅                | ❌ (`None`)            |

Per il resto, valgono tutti i concetti di slicing che abbiamo visto nelle stringhe. Quindi siamo andati veloci sullo slicing! 😁

## ♻️ Mutabilità: aggiornare, modificare, inserire, rimuovere

La mutabilità delle liste consente operazioni estremamente versatili. È possibile:

- Cambiare direttamente il valore di un elemento in posizione nota.
- Aggiungere uno o più elementi alla fine della lista (concatenazione).
- Inserire elementi in una posizione specifica.
- Rimuovere elementi esistenti per posizione o per valore.
- Svuotare completamente la lista senza crearne una nuova.

La mutabilità rende le liste molto più dinamiche rispetto ad altre strutture dati, ma introduce anche il rischio di effetti collaterali se si lavora su **riferimenti** condivisi.

### 🔧 Operazioni fondamentali sulle Liste

Le liste permettono di **modificare, aggiungere, rimuovere e accedere** agli elementi con grande flessibilità. Vediamo alcune operazioni fondamentali che si eseguono frequentemente con una lista.

#### 📌 Esempio iniziale

Consideriamo la lista:

Questa lista contiene tre stringhe. Ogni elemento è accessibile tramite un **indice intero** (a partire da 0).

### 🔄 Modifica di un elemento

Consideriamo la lista:

In questo esempio, l’elemento in posizione 1 (cioè "banana") viene sostituito con "pera".  
Le liste in Python **supportano l’assegnazione diretta a un indice**, proprio perché sono **mutabili**.  
Questo è uno dei vantaggi principali rispetto alle tuple.

### ➕ Aggiunta di un elemento alla fine della lista

Consideriamo la lista:

Il metodo `append()` aggiunge un nuovo elemento **in fondo alla lista**, aumentandone la lunghezza di uno.  
È il metodo più usato per **espandere una lista** dinamicamente, ad esempio durante la lettura di input o l'elaborazione di dati.

### 📥 Inserimento in una posizione specifica

Consideriamo la lista:

Il metodo `insert(indice, valore)` permette di **inserire un nuovo elemento in una posizione precisa**, spostando in avanti gli elementi successivi.  
In questo caso, "fragola" viene inserita alla **posizione 1**, prima di "pera".

### ❌ Rimozione per valore

Consideriamo la lista:

Il metodo `remove(valore)` cerca il primo elemento che **corrisponde esattamente** al valore indicato e lo elimina dalla lista.  
⚠️ Se il valore non è presente, viene generato un errore `ValueError`, quindi può essere utile verificare prima che l'elemento sia effettivamente presente con l'operatore `in`.

### 📦 Stato finale della lista

Dopo tutte le operazioni sopra, il contenuto della lista sarà:

Ogni metodo ha agito in modo coerente sulla struttura della lista, modificandone dinamicamente il contenuto.

💡 Queste operazioni sono fondamentali nella programmazione Python, e vengono usate in moltissimi algoritmi e flussi di dati. Apprenderle a fondo ti permetterà di costruire strutture più complesse, come liste annidate, code, pile e strutture ibride.

## 🧮 Operazioni comuni sulle liste

Le liste sono tra le strutture più flessibili in Python, e conoscere le loro operazioni fondamentali è essenziale per qualsiasi programmatore. Di seguito vengono descritte le principali operazioni che si possono effettuare con una lista.

### 🔗 Concatenazione

La concatenazione consiste nell’unire due (o più) liste per formare una nuova lista che contiene tutti gli elementi delle liste originarie **nell’ordine in cui appaiono**.  
Questa operazione **non modifica le liste originali**, ma ne crea una nuova risultante. È molto utile quando si vogliono combinare dati provenienti da fonti diverse o strutturare insiemi più grandi a partire da sottoinsiemi.

Anche qui, esattamente come le stringhe!

#### Estensione con `exstend()`

Il metodo `extend()` permette di aggiungere **tutti gli elementi di una lista** alla fine di una lista esistente.

A differenza di `append()`, che aggiunge l’intero oggetto come singolo elemento, `extend()` “srotola” l’iterabile e inserisce ciascun elemento singolarmente.

Questo è molto utile quando vuoi unire due liste o aggiungere più elementi contemporaneamente senza creare una nuova lista.

### 🔁 Ripetizione

È possibile **replicare** gli elementi di una lista più volte, ottenendo una lista più lunga con sequenze ripetute.  
Questa operazione può servire a creare modelli, dati di test, o ad inizializzare strutture con pattern ripetuti.

### 🔍 Appartenenza

Con l’operazione di appartenenza si verifica se un determinato valore **è presente** all’interno della lista.  
È una delle operazioni più comuni, soprattutto per il controllo di input, la validazione di dati o la verifica di condizioni.  
L’operatore di appartenenza restituisce un valore booleano (`vero` o `falso`), ed è molto utile nei blocchi decisionali.

### 🔄 Scorrimento (iterazione)

Le liste possono essere **iterate**, cioè percorse elemento per elemento, tipicamente tramite un ciclo.  
Durante lo scorrimento è possibile analizzare, trasformare, filtrare o aggregare i dati.  
L’iterazione è alla base di moltissimi algoritmi, come il calcolo di somme, medie, ricerche condizionate o trasformazioni.

Esamineremo in dettaglio questa caratteristica quando introdurremo i cicli!

### 📊 Ordinamento

È possibile ordinare gli elementi di una lista in **ordine crescente o decrescente**, se gli elementi sono confrontabili (numeri, stringhe, ecc.).  
Il metodo standard per ordinare una lista è il metodo `sort()`. 
Esistono anche criteri personalizzabili per l’ordinamento (come la lunghezza delle stringhe o funzioni definite dall’utente, li vedremo in seguito).

Approfondiremo gli ordinamenti in seguito!

### 📍 Ricerca

Serve per **trovare la posizione** (indice) del primo elemento che soddisfa un determinato requisito.  
La ricerca è fondamentale in strutture che richiedono l’identificazione della posizione, ad esempio per modifiche o accessi successivi.  
Se l’elemento non è presente, viene solitamente sollevata un’eccezione, quindi è buona norma combinarla con l’operazione di appartenenza.

### 🔢 Conteggio

È possibile contare **quante volte un certo valore** compare nella lista.  
Questa operazione è molto usata in analisi statistiche, generazione di report, costruzione di frequenze e grafici, oppure per verificare la ripetizione di un certo evento.


### 👀 Osservazioni

Queste operazioni costituiscono la base per implementare algoritmi più complessi e flessibili:  
- Le concatenazioni e ripetizioni permettono di **generare strutture su misura**.  
- Le ricerche, verifiche e conteggi abilitano **analisi e classificazioni**.  
- L’ordinamento è indispensabile per algoritmi di **ottimizzazione, ricerca binaria e ranking**.  
- L’iterazione permette di costruire **trasformazioni, aggregazioni e filtri**.

## 📈 Vantaggi delle liste

- Sono **semplici da usare** e supportano una sintassi molto leggibile.
- Permettono una **gestione dinamica** della memoria: si possono creare e modificare senza definire in anticipo la lunghezza.
- Sono altamente **versatili** e adatte a una vasta gamma di problemi.
- Hanno un **supporto nativo ottimizzato** all’interno del linguaggio Python.

## 🧬 Liste Annidate

Le **liste annidate** sono liste che **contengono altre liste** come elementi.  
Sono utili per rappresentare **strutture complesse** come matrici, tabelle o insiemi di dati organizzati.

🔹 Ogni elemento può essere una lista con contenuti e dimensioni differenti.  
🔹 Per accedere a un elemento interno, si usano più indici: prima si accede alla sottolista, poi all’elemento desiderato.

📌 Di seguito alcuni esempi pratici:

## ⚠️ Attenzione ai riferimenti condivisi

In Python, le liste sono oggetti **mutabili**. Quando assegni una lista a una nuova variabile con il simbolo `=`, **non** viene creata una nuova copia indipendente: entrambe le variabili **puntano allo stesso oggetto in memoria**. Di conseguenza, modificare la lista usando una variabile **modifica anche l'altra**, perché si sta operando sullo **stesso contenuto**.

### 🔁 Esempio di riferimento condiviso

Quando si fa un'assegnazione diretta come `lista2 = lista1`, entrambi i nomi fanno riferimento alla **stessa lista** in memoria. Qualsiasi modifica a uno dei due si rifletterà sull'altro.

### 🎯 Come evitare questo comportamento?

Per ottenere una **copia indipendente**, è necessario usare una **copia esplicita**:

- **Copia superficiale (shallow copy)**: copia solo il primo livello della lista.
  - `lista2 = lista1.copy()`
  - `lista2 = lista1[:]`
  - `import copy; lista2 = copy.copy(lista1)`

- **Copia profonda (deep copy)**: copia anche gli oggetti annidati, a qualsiasi livello.
  - `import copy; lista2 = copy.deepcopy(lista1)`

### Quindi attenzione alle liste annidate!

Se la lista contiene al suo interno altre liste o strutture complesse, una copia superficiale non basta: le sottoliste continueranno a essere condivise. In questi casi, è fondamentale usare `copy.deepcopy` per duplicare **l'intera struttura**.

## 🧩 `append()` vs `extend()` vs operatore `+`

### 📍 `append(elemento)`
- Aggiunge **un singolo elemento** in coda alla lista.
- L’elemento può essere di qualsiasi tipo (anche un’altra lista), che verrà inserita **come singolo elemento**.

### 📍 `extend(iterabile)`
- Estende la lista aggiungendo **uno per uno** tutti gli elementi della lista fornita.
- In pratica “srotola” la lista da aggiungere, inserendo i suoi elementi singolarmente.

### 📍 Operatore `+`
- Crea una **nuova lista** concatenando le due liste.
- Non modifica le liste originali, ma restituisce una nuova lista risultante dalla somma degli elementi di entrambe.

---

### 📌 Differenze principali:

| Metodo/Operatore | Modifica la lista originale? | Tipo di aggiunta                  | Restituisce nuova lista? |
|------------------|------------------------------|---------------------------------|-------------------------|
| `append()`       | Sì                           | Un singolo elemento (anche lista come elemento singolo) | No                      |
| `extend()`       | Sì                           | Tutti gli elementi di un iterabile, uno per uno         | No                      |
| `+`              | No                           | Nuova lista, concatenazione di due liste                 | Sì                      |

## Ordinamento con `sort()` e `sorted()`

In Python esistono due modi principali per ordinare una lista:

- **`list.sort()`**: è un metodo che ordina la lista **in-place**, cioè modifica direttamente la lista originale senza crearne una nuova.  
  Questo significa che non restituisce nulla (`None`), ma cambia l’ordine degli elementi della lista su cui viene chiamato.

- **`sorted()`**: è una funzione built-in che prende un iterabile (come una lista) e **restituisce una nuova lista ordinata**, lasciando intatto l’originale.  
  È utile quando si vuole mantenere la lista originale invariata e ottenere una copia ordinata.

### Differenze principali:

| Caratteristica          | `list.sort()`                   | `sorted()`                      |
|------------------------|--------------------------------|--------------------------------|
| Modifica la lista       | Sì (in-place)                  | No                             |
| Restituisce             | `None`                        | Nuova lista ordinata            |
| Può ordinare qualsiasi iterabile | No, solo liste               | Sì, qualsiasi iterabile         |
| Uso comune              | Quando si vuole modificare la lista originale | Quando serve una copia ordinata senza modificare l’originale |

Entrambi accettano parametri opzionali molto utili:

- `key=`: funzione per estrarre una chiave di ordinamento da ogni elemento (ad esempio, ordinare per lunghezza di una stringa o per un attributo di un oggetto).
- `reverse=True`: per invertire l’ordinamento, ottenendo una lista ordinata in ordine decrescente.

⚠️ **Consiglio pratico:**  
Usa `sort()` quando vuoi ordinare e basta, senza necessità di mantenere la lista originale.  
Usa `sorted()` quando hai bisogno di conservare la lista originale o quando vuoi ordinare tipi diversi da liste.

## 🔄 Casting a lista da stringa

Spesso può essere utile **convertire una stringa in una lista** di caratteri.  
In Python, questo si ottiene facilmente usando la funzione `list()` applicata a una stringa:

Ogni carattere della stringa diventa un elemento della lista, mantenendo l’ordine originale.
Questa operazione è utile quando si vogliono manipolare singoli caratteri, ad esempio per filtri, modifiche o analisi.

⚠️ Nota: il casting con list() da stringa crea una lista di singoli caratteri, non di parole.
Per ottenere una lista di parole da una frase, è meglio usare il metodo `.split()`.

## 🧹 Metodo clear()

Il metodo `clear()` permette di svuotare completamente una lista, rimuovendo tutti gli elementi in modo efficiente.
La lista rimane presente, ma diventa vuota.

⚠️ Ricorda che `clear()` modifica la lista originale in-place e non restituisce nulla (None).

## 🔚 Conclusioni

Le **liste** sono una struttura dati fondamentale in Python, grazie alla loro flessibilità, mutabilità e facilità d'uso.  
In questo capitolo abbiamo visto:

- La definizione di lista come collezione ordinata, indicizzata e mutabile.
- Come accedere agli elementi tramite indicizzazione e slicing.
- Le operazioni di modifica, aggiunta, inserimento e rimozione di elementi.
- La differenza tra metodi `append()`, `extend()` e l’operatore `+`.
- L’importanza di comprendere i riferimenti condivisi e come fare copie superficiali o profonde.
- Le principali operazioni comuni come concatenazione, ripetizione, ricerca, conteggio e ordinamento.
- Il casting da stringa a lista e il metodo `clear()` per svuotare le liste.

Conoscere bene le liste e il loro comportamento è essenziale per scrivere codice Python efficace e performante, e costituisce la base per affrontare strutture dati più complesse e algoritmi avanzati.

Nel prossimo capitolo approfondiremo le **tuple** e vedremo come si differenziano dalle liste, in particolare in termini di immutabilità e prestazioni.

