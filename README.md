# Programmazione in Python - Base 🐍 [Build in Progress...]

## Introduzione
🚀 **Benvenuti nel mondo della programmazione con Python!**  
Questo corso è progettato per guidarvi passo dopo passo nell'apprendimento dei concetti fondamentali della programmazione, tramite l'utilizzo di Python: il linguaggio di programmazione più popolare e potente del mondo. Che siate alle prime armi o vogliate consolidare le basi, qui troverete un mix perfetto di teoria e pratica, arricchito da esempi concreti e progetti stimolanti. Preparatevi a trasformare le vostre idee in codice! 💻✨

## 📚 Programma del Corso

| Capitolo | Titolo                       | Argomenti Chiave                                                               | Link                                                                 |
|----------|------------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------|
| 1        | Introduzione                 | Ambiente di sviluppo, primo programma, debugging                               | [Vai ➔](#-capitolo-1---introduzione)                                |
| 2        | Numeri e Stringhe            | Operazioni base, F-strings, mutabilità                                         | [Vai ➔](#-capitolo-2---numeri-e-stringhe)                           |
| 3        | Tipi di Dato Avanzati                   | Liste, Tuple, Set, Dizionari                                        | [Vai ➔](#-capitolo-3---tipi-di-dato-avanzati)                                   |
| 4        | Decisioni e Cicli                        | `if`, `while`, `for`, `enumerate`, `zip`, cicli annidati, etc.     | [Vai ➔](#-capitolo-4---cicli)                                       |
| 5        | Funzioni                     | Parametri, scope, lambda functions                                             | [Vai ➔](#-capitolo-5---funzioni)                                    |
| 6        | Gestione Eccezioni           | `try/except/finally`, eccezioni personalizzate                                 | [Vai ➔](#-capitolo-6---gestione-eccezioni)                          |
| 7        | File e Formati Dati          | Lettura/scrittura file, `CSV`, `JSON`, context manager                         | [Vai ➔](#-capitolo-7---file-e-formati-dati)                         |
| 8       | Oggetti e Classi             | OOP base, costruttore, metodi, decoratori                                      | [Vai ➔](#-capitolo-8---oggetti-e-classi)                           |
| 9       | Ereditarietà                 | Ereditarietà, polimorfismo, classi astratte, design pattern                    | [Vai ➔](#-capitolo-9---ereditarietà)                              |
| 10       | Ricorsione                   | Concetti base, backtracking, memoizzazione, divide et impera                   | [Vai ➔](#-capitolo-10---ricorsione)                                 |
| 11       | Ordinamento e Ricerca        | Algoritmi di ordinamento, ricerca binaria, analisi delle prestazioni           | [Vai ➔](#-capitolo-11---ordinamento-e-ricerca)                      |
| 12       | Librerie Standard Avanzate   | `math`, `datetime`, `os`, `sys`, `argparse`                                    | [Vai ➔](#-capitolo-12---librerie-standard-avanzate)                |
| 13       | Progetti Pratici             | Progetto finale, documentazione, test, versione, deploy                        | [Vai ➔](#-capitolo-13---progetti-pratici)                            |


*🔍 Utilizza i link per navigare rapidamente agli argomenti di interesse*

## Obiettivi 🎯
Immergiti in un percorso strutturato che trasformerà il tuo approccio alla programmazione. Ecco cosa **dominerai**:

### 🧩 Fondamenti della Programmazione  
- **Variabili e tipi di dati**:  
  - Assegna valori a variabili per salvare informazioni temporanee.  
  - Lavora con numeri interi (int), decimali (float), testi (str), valori logici (bool) e tipi complessi come liste e dizionari.  
  - Conosci le operazioni fondamentali su ciascun tipo (es. concatenazione per stringhe, somma per numeri, indexing per liste).  

- **Controllo del flusso**:  
  - Dirigi il comportamento del programma con strutture condizionali: if, elif, else.  
  - Crea ripetizioni e automatismi con cicli while (condizione) e for (iterazione su sequenze).  
  - Usa break e continue per controllare l'esecuzione all'interno dei cicli.  

- **Strutture dati avanzate**:  
  - **Liste** (list): contenitori ordinati e modificabili.  
  - **Dizionari** (dict): associazioni chiave-valore ideali per accessi rapidi.  
  - **Tuple** (tuple): simili alle liste ma immutabili.  
  - **Insiemi** (set): collezioni non ordinate di elementi unici.  
  - Utilizza queste strutture per organizzare e manipolare dati in modo efficiente.  

- **Funzioni e moduli**:  
  - Definisci funzioni con def per racchiudere codice riutilizzabile.  
  - Passa parametri, restituisci risultati con return.  
  - Importa moduli (import, from ... import) per sfruttare librerie esterne o organizzare meglio il codice.  
  - Conosci la differenza tra variabili locali e globali, e l’uso del concetto di **scope** (ambito).  

- **Gestione degli errori**:  
  - Proteggi il programma dagli errori inaspettati con try/except.  
  - Cattura errori specifici (ZeroDivisionError, ValueError, ecc.) per gestire comportamenti diversi.  
  - Usa finally per eseguire codice indipendentemente dall’esito.  
  - Crea eccezioni personalizzate per situazioni particolari con raise e classi derivate da Exception.  

- **Programmazione a Oggetti (OOP)**:  
  - Organizza il codice attorno a **oggetti**, che combinano **dati** (attributi) e **comportamenti** (metodi).  
  - Crea nuove **classi** con la parola chiave class, e istanzia oggetti con la sintassi oggetto = NomeClasse().  
  - Usa il metodo speciale __init__ per inizializzare gli oggetti.  
  - Incapsula il comportamento all'interno di metodi (def) legati a una classe, utilizzando self per accedere agli attributi.  
  - Applica concetti fondamentali come:  
    - **Incapsulamento**: nascondi i dettagli interni e proteggi i dati.  
    - **Ereditarietà**: crea nuove classi che riutilizzano codice da altre classi (class Figlia(Genitore):).  
    - **Polimorfismo**: usa metodi con lo stesso nome su oggetti diversi che si comportano in modo coerente.  
  - Favorisce la riusabilità, la chiarezza e la scalabilità del codice in progetti complessi.  

- **Gestione dei file**:  
  - Leggi e scrivi dati su file esterni per salvare o caricare informazioni persistenti.  
  - Usa la funzione open() con modalità come 'r' (lettura), 'w' (scrittura), 'a' (aggiunta) e 'b' (binario).  
  - Leggi i contenuti di un file con read(), readline() o readlines().  
  - Scrivi su file con write() o writelines().  
  - Utilizza il costrutto with open(...) as f: per aprire file in modo sicuro, garantendo la chiusura automatica.  
  - Lavora con file CSV, JSON e altri formati standard con i moduli csv, json e pickle.  
  - Attenzione alla gestione degli errori (es. file non trovato, permessi) con try/except.  

### 💡 Problem Solving Algoritmico  
- **Pensiero Algoritmico**:  
  - Scomporre un problema complesso in sottoproblemi più semplici.  
  - Identificare input, output e vincoli.  
  - Progettare soluzioni passo-passo, verificando la correttezza di ciascun passo.  
  - Riconoscere casi base e condizioni di terminazione nei problemi ricorsivi.  

- **Pattern ricorrenti**:  
  - Ricerca binaria  
  - Algoritmi greedy (scelte locali ottimali)  
  - Ricorsione e memoizzazione  
  - Programmazione dinamica  
  - Divide et impera  
  - Two pointers, sliding window  
  - Backtracking  

- **Ottimizzazione del codice**:  
  - Misura i tempi di esecuzione con `timeit`.  
  - Monitora l'uso della memoria con `tracemalloc`.  
  - Confronta soluzioni diverse in termini di complessità computazionale (tempo e spazio).  
  - Utilizza strutture dati efficienti (es. set, dict, heap, deque).  
  - Evita calcoli ripetuti (es. caching, memoization).

### 🌟 Preparazione al Futuro  
- **Propedeutico per percorsi specialistici**:  
  - **Data Science**: Analisi dataset, machine learning base con `scikit-learn`.  
  - **Sviluppo Web**: Introduzione a Flask/Django per API e siti dinamici.  
  - **Automazione**: Script per file system, web scraping e bot.  
  - **Game Development**: Logiche di gioco 2D con `Pygame`.  
- **Portfolio tecnico**: 10+ progetti dimostrabili per CV e colloqui.

### 🎁 Bonus Esclusivi  
- **Certificazione finale** con verifica delle competenze 🏅  
- **Accesso a repository privati** con codice template e soluzioni 🔐  
- **Community attiva** per collaborazioni e hackathon 👥  

**Perché scegliere questo corso?**

✅ **Project-Based Learning**: Ogni capitolo si conclude con un mini-progetto pratico  
✅ **Esercizi interattivi** con correzione automatica e feedback diretto dal docente  
✅ **Supporto 1:1** tramite ambiente virtuale dedicato per dubbi tecnici  
✅ **Aggiornamenti gratuiti** a vita su nuovi contenuti e tecnologie  
✅ **Lingua Italiana 🇮🇹**: L'intero corso è erogato interamente in lingua Italiana, il che non è poco!

**Trasforma le tue idee in codice... e il codice in carriera!** 🚀 

## A chi è rivolto?
🎓 **Studenti**: Perfetto per scuole superiori, università e aziende.  
🏫 **Insegnanti**: Materiale didattico pronto per lezioni in presenza o online.  
💻 **Autodidatti**: Strutturato per apprendere senza prerequisiti e senza scadenze. Impara al tuo ritmo!  
💼 **Professionisti**: Aggiorna le tue competenze con uno dei linguaggi più richiesti dal mercato!  

🌍 *Accessibile a tutti, con esempi chiari e un linguaggio semplice e intuitivo!*

## Descrizione dei Capitoli

### 📘 Capitolo 1 - Introduzione

In questo capitolo si introducono i concetti fondamentali dell'informatica: cosa sono i programmi, come funziona un computer e cosa significa programmare.  
Viene introdotto l'ambiente Google Colab e scritto il primo semplice programma.

| Sezione                    | Notebook                          | Link |
|----------------------------|-----------------------------------|------|
| Obiettivi del capitolo     | 0_Obiettivi.ipynb                 | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo1_Introduzione/0_Obiettivi_del_capitolo/0_Obiettivi.ipynb" target="_blank">0_Obiettivi.ipynb</a> |
| Concetti di base           | 1_Concetti_di_base.ipynb          | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo1_Introduzione/1_Concetti_di_base.ipynb" target="_blank">1_Concetti_di_base.ipynb</a> |
| Anatomia del computer      | 2_Anatomia_del_computer.ipynb     | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo1_Introduzione/2_Anatomia_del_computer.ipynb" target="_blank">2_Anatomia_del_computer.ipynb</a> |
| Pensiero computazionale    | 3_Pensiero_computazionale.ipynb   | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo1_Introduzione/3_Pensiero_computazionale.ipynb" target="_blank">3_Pensiero_computazionale.ipynb</a> |
| Linguaggio Python          | 4_Linguaggio_Python.ipynb         | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo1_Introduzione/4_Linguaggio_Python.ipynb" target="_blank">4_Linguaggio_Python.ipynb</a> |
| Google Colab               | 5_Google_Colab.ipynb              | <span style="color:red;">5_Google_Colab.ipynb</span> |
| Ambiente di programmazione | 6_Ambiente_di_programmazione.ipynb| <span style="color:red;">6_Ambiente_di_programmazione.ipynb</span> |
| Primo programma            | 7_Primo_programma.ipynb           | <span style="color:red;">7_Primo_programma.ipynb</span> |
| Errori comuni              | 8_Errori_comuni.ipynb             | <span style="color:red;">8_Errori_comuni.ipynb</span> |
| Debugging Base             | 9_Debugging_Base.ipynb            | <span style="color:red;">9_Debugging_Base.ipynb</span> |
| Virtual Environment        | 10_Virtual_Environment.ipynb      | <span style="color:red;">10_Virtual_Environment.ipynb</span> |
| Esercizi                   | 11_Esercizi.ipynb                 | <span style="color:red;">11_Esercizi.ipynb</span> |


**🎯 Obiettivo del Capitolo:**  
Comprendere la struttura di un computer, i concetti base della programmazione, scrivere semplici script Python in Colab e gestire ambienti di sviluppo.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Spiegare il funzionamento base di un computer  
- Applicare il pensiero computazionale a problemi semplici  
- Configurare un ambiente Python con Colab e virtual environment  
- Scrivere e debuggare programmi basilari  

### 📘 Capitolo 2 - Numeri e Stringhe

Questo capitolo introduce le variabili, i numeri, le stringhe e le operazioni aritmetiche.  
Si impara a gestire l’input/output e si toccano i primi concetti di grafica e le best practices per la scrittura di codice **Pythonico**.

| Sezione                | Notebook                      | Link |
|------------------------|-------------------------------|------|
| Obiettivi del capitolo | 0_Obiettivi.ipynb             | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo2_Numeri_e_Stringhe/0_Obiettivi.ipynb" target="_blank">0_Obiettivi.ipynb</a> |
| Variabili              | 1_Variabili.ipynb             | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo2_Numeri_e_Stringhe/1_Variabili.ipynb" target="_blank">1_Variabili.ipynb</a> |
| Aritmetica             | 2_Aritmetica.ipynb            | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo2_Numeri_e_Stringhe/2_Aritmetica.ipynb" target="_blank">2_Aritmetica.ipynb</a> |
| Stringhe               | 3_Stringhe.ipynb              | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo2_Numeri_e_Stringhe/3_Stringhe.ipynb" target="_blank">3_Stringhe.ipynb</a> |
| Grafica Intro          | 7_Grafica_intro.ipynb         | <span style="color:red;">4_Grafica_intro.ipynb</span> |
| Best Practices         | 10_Best_practices.ipynb       | <span style="color:red;">6_Best_practices.ipynb</span> |
| Esercizi               | 11_Esercizi.ipynb             | <span style="color:red;">7_Esercizi.ipynb</span> |


**🎯 Obiettivo del Capitolo:**  
Padroneggiare variabili, operazioni aritmetiche, manipolazione avanzata di stringhe e comprendere la natura mutabile/immutabile dei tipi di dati.

**Alla fine del capitolo lo studente sarà in grado di**:
- Utilizzare le variabili per memorizzare dati
- Gestire correttamente l'input e l'output di un programma
- Utilizzare operazioni aritmetiche per manipolare dati numerici
- Utilizzare e manipolare stringhe per rappresentare e gestire testi  
- Utilizzare f-string per formattazione avanzata  
- Distinguere tra oggetti mutabili e immutabili  
- Progettare algoritmi con operazioni miste numeriche/stringhe  
- Comprendere il funzionamento basilare della grafica
- Applicare best practices per codice pulito e leggibile

### 📘 Capitolo 3 - Tipi di Dato Avanzati

In questo capitolo si approfondiscono le principali strutture dati avanzate offerte da Python: **liste**, **tuple**, **set**, **dizionari**, ma anche tipi meno noti come **range**, **bytes**, **bytearray** e **memoryview**. Questi strumenti permettono di rappresentare, organizzare ed elaborare insiemi di dati in modo efficiente, e sono fondamentali per qualunque programma di media o alta complessità. Impareremo ad accedere, modificare, ordinare e iterare su collezioni di dati, comprendendo anche il ruolo dei tipi immutabili e mutabili.

| Sezione                     | Notebook                         | Link                                                                                                                                                             |
|-----------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo      | 0_Obiettivi.ipynb               | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo3_Tipi_di_Dato_Avanzati/0_Obiettivi.ipynb" target="_blank">0_Obiettivi.ipynb</a> |
| Liste                       | 1_Liste.ipynb                   | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo3_Tipi_di_Dato_Avanzati/1_Liste.ipynb" target="_blank">1_Liste.ipynb</a>                                                                                                                   |
| Tuple                       | 2_Tuple.ipynb                   | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo3_Tipi_di_Dato_Avanzati/2_Tuple.ipynb" target="_blank">2_Tuple.ipynb</a>                                                                                                                   |
| Set                         | 3_Set.ipynb                     | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo3_Tipi_di_Dato_Avanzati/3_Set.ipynb" target="_blank">3_Set.ipynb</a>                                                                                                                     |
| Dizionari                   | 4_Dizionari.ipynb               | <a href="https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo3_Tipi_di_Dato_Avanzati/4_Dizionari.ipynb" target="_blank">4_Dizionari.ipynb</a>                                                                                                               |
| Metodi e funzioni utili     | 5_Metodi_e_funz_utili_su_collezioni.ipynb | <span style="color:red;">5_Metodi_e_funz_utili_su_collezioni.ipynb</span>                                                                                       |
| Tipi speciali: range e byte | 6_Range_bytes_bytearray_memoryview.ipynb | <span style="color:red;">6_Range_bytes_bytearray_memoryview.ipynb</span>                                                                                        |
| Applicazioni pratiche       | 7_Applicazioni_pratiche.ipynb   | <span style="color:red;">7_Applicazioni_pratiche.ipynb</span>                                                                                                   |
| Best practices              | 8_Best_practices.ipynb          | <span style="color:red;">8_Best_practices.ipynb</span>                                                                                                         |
| Esercizi                    | 9_Esercizi.ipynb                | <span style="color:red;">9_Esercizi.ipynb</span>                                                                                                               |


**🎯 Obiettivo del Capitolo:**  
Diventare esperti nell’uso delle principali collezioni Python, sapendo scegliere quella più adatta al problema, manipolare dati in modo efficiente e scrivere codice leggibile e idiomatico. Approfondire anche strutture meno comuni per un controllo più fine della memoria e delle sequenze numeriche.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Utilizzare **liste** per memorizzare sequenze mutabili  
- Conoscere le **tuple** per rappresentare dati immutabili  
- Usare i **set** per eliminare duplicati ed effettuare operazioni insiemistiche  
- Costruire e manipolare **dizionari** per mappare coppie chiave-valore  
- Usare `range()` per generare sequenze numeriche efficienti  
- Comprendere e usare i tipi **bytes** e **bytearray** per gestire dati binari  
- Utilizzare `memoryview` per una gestione ottimizzata della memoria  
- Conoscere e applicare i principali metodi delle collezioni  
- Risolvere problemi pratici usando le strutture dati in modo integrato  
- Utilizzare **best practices** per scrivere codice pulito e leggibile

### 📘 Capitolo 4 - Decisioni e Cicli

In questo capitolo, affrontiamo la logica delle strutture decisionali: l’uso dell’`if`, degli operatori logici, delle condizioni multiple e delle espressioni booleane.  In questo capitolo si affrontano, inoltre, le strutture iterative, fondamentali per eseguire azioni ripetute nei programmi. Si parte dal ciclo `while`, passando per il ciclo `for` e gli algoritmi che richiedono ripetizione. Verranno anche trattati cicli annidati, gestione di stringhe con i cicli, simulazioni casuali e tecniche di conteggio.

| Sezione                    | Notebook                                                                        | Link                                                                                                                                                             |
|----------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo     | 0_Obiettivi.ipynb                                                              | <span style="color:red;">0_Obiettivi.ipynb</span> |
| If statement               | 1_If_statement.ipynb                                                            | <span style="color:red;">1_If_statement.ipynb</span>                                                                                                            |
| Ciclo while                | 2_Ciclo_while.ipynb                                                             | <span style="color:red;">2_Ciclo_while.ipynb</span>                                                                                                            |
| Ciclo for                  | 3_Ciclo_for.ipynb                                                               | <span style="color:red;">3_Ciclo_for.ipynb</span>                                                                                                              |
| Operatori logici e booleani| 4_Operatori_logici_booleani.ipynb                                               | <span style="color:red;">4_Operatori_logici_booleani.ipynb</span>                                                                                              |
| Cicli annidati             | 5_Cicli_annidati.ipynb                                                          | <span style="color:red;">5_Cicli_annidati.ipynb</span>                                                                                                         |
| Gestione stringhe con cicli| 6_Gestione_stringhe_con_cicli.ipynb                                            | <span style="color:red;">6_Gestione_stringhe_con_cicli.ipynb</span>                                                                                            |
| Simulazioni casuali        | 7_Simulazioni_casuali.ipynb                                                     | <span style="color:red;">7_Simulazioni_casuali.ipynb</span>                                                                                                    |
| Tecniche di conteggio      | 8_Tecniche_di_conteggio.ipynb                                                   | <span style="color:red;">8_Tecniche_di_conteggio.ipynb</span>                                                                                                  |
| Best practices             | 9_Best_practices.ipynb                                                          | <span style="color:red;">9_Best_practices.ipynb</span>                                                                                                         |
| Esercizi                   | 10_Esercizi.ipynb                                                               | <span style="color:red;">10_Esercizi.ipynb</span>                                                                                                              |


**🎯 Obiettivo del Capitolo:**  
Comprendere la logica condizionale e le strutture iterative in Python, saper scrivere programmi con decisioni multiple e ripetizioni efficaci, e applicare queste conoscenze per risolvere problemi complessi e simulazioni.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Usare le istruzioni `if`, `elif`, `else` per prendere decisioni multiple  
- Applicare operatori logici (`and`, `or`, `not`) e comprendere la valutazione booleana  
- Scrivere cicli `while` per eseguire ripetizioni basate su condizioni  
- Utilizzare cicli `for` per iterare su sequenze e intervalli  
- Gestire cicli annidati e operazioni complesse su dati multidimensionali  
- Iterare su stringhe e manipolare caratteri con i cicli  
- Realizzare semplici simulazioni casuali usando il modulo `random`  
- Applicare tecniche di conteggio e accumulo nei cicli  
- Implementare best practices per cicli e condizioni per migliorare leggibilità e performance  


### 📘 Capitolo 5 - Funzioni

In questo capitolo si approfondisce il concetto di funzione, uno degli strumenti fondamentali per organizzare, riutilizzare e testare il codice. Verranno trattati i parametri, i valori restituiti, le funzioni senza `return`, la visibilità delle variabili e le funzioni anonime.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/0_Obiettivi_del_capitolo/0_Obiettivi.ipynb) |
| Funzioni come scatole nere                  | 1_Funzioni_scatole_nere.ipynb                                            | [1_Funzioni_scatole_nere.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/1_Scatole_nere/1_Funzioni_scatole_nere.ipynb) |
| Realizzazione e collaudo di funzioni        | 2_Realizzazione_e_collaudo.ipynb                                         | [2_Realizzazione_e_collaudo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/2_Realizzazione/2_Realizzazione_e_collaudo.ipynb) |
| Passaggio di parametri                      | 3_Passaggio_parametri.ipynb                                              | [3_Passaggio_parametri.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/3_Passaggio_parametri/3_Passaggio_parametri.ipynb) |
| Valori restituiti                           | 4_Valori_restituiti.ipynb                                                | [4_Valori_restituiti.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/4_Valori_restituiti/4_Valori_restituiti.ipynb) |
| Funzioni che non restituiscono un valore    | 5_Funzioni_senza_return.ipynb                                            | [5_Funzioni_senza_return.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/5_Senza_return/5_Funzioni_senza_return.ipynb) |
| Soluzione di problemi: funzioni riutilizzabili | 6_Funzioni_riutilizzabili.ipynb                                        | [6_Funzioni_riutilizzabili.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/6_Riutilizzo_funzioni/6_Funzioni_riutilizzabili.ipynb) |
| Soluzione di problemi: miglioramenti successivi | 7_Miglioramenti_successivi.ipynb                                      | [7_Miglioramenti_successivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/7_Miglioramenti_successivi/7_Miglioramenti_successivi.ipynb) |
| Ambito di visibilità delle variabili        | 8_Scope_variabili.ipynb                                                  | [8_Scope_variabili.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/8_Scope/8_Scope_variabili.ipynb) |
| Funzioni anonime                            | 9_Lambda_funzioni_anonime.ipynb                                          | [9_Lambda_funzioni_anonime.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/10_Lambda/9_Lambda_funzioni_anonime.ipynb) |
| Riepilogo del capitolo                      | 10_Riepilogo.ipynb                                                       | [10_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/11_Riepilogo/10_Riepilogo.ipynb) |
| Esercizi                                    | 11_Esercizi.ipynb                                                        | [11_Esercizi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/12_Esercizi/11_Esercizi.ipynb) |
| Auto-valutazione                            | 12_Auto_valutazione.ipynb                                                | [12_Auto_valutazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo5_Funzioni/13_Auto_valutazione/12_Auto_valutazione.ipynb) |

**🎯 Obiettivo del Capitolo:**  
Scrivere funzioni per scomporre problemi complessi in sottoproblemi più semplici, migliorare la leggibilità e la manutenzione del codice, comprendere le funzioni anonime.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Definire e utilizzare funzioni con parametri e valore restituito.  
- Comprendere la differenza tra ambito locale e globale.  
- Scrivere funzioni per risolvere problemi specifici.  
- Usare funzioni anonime (lambda) per operazioni rapide e concise.

### 📘 Capitolo 6 - Liste

In questo capitolo vengono introdotte le liste e le tuple, due strutture dati fondamentali in Python. Le liste permettono di memorizzare collezioni ordinate di elementi e sono strumenti potenti per organizzare dati, realizzare algoritmi e risolvere problemi in modo efficiente.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/0_Obiettivi_del_capitolo/0_Obiettivi.ipynb) |
| Proprietà basilari delle liste              | 1_Proprieta_liste.ipynb                                                  | [1_Proprieta_liste.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/1_Proprieta/1_Proprieta_liste.ipynb) |
| Operazioni con le liste                     | 2_Operazioni_liste.ipynb                                                 | [2_Operazioni_liste.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/2_Operazioni/2_Operazioni_liste.ipynb) |
| Tuple: struttura e utilizzo                 | 3_Tuple.ipynb                                                            | [3_Tuple.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/3_Tuple/3_Tuple.ipynb) |
| List Comprehension                          | 4_List_comprehension.ipynb                                               | [4_List_comprehension.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/4_List_comprehension/4_List_comprehension.ipynb) |
| Algoritmi elementari su liste               | 5_Algoritmi_liste.ipynb                                                  | [5_Algoritmi_liste.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/5_Algoritmi/5_Algoritmi_liste.ipynb) |
| Utilizzo di liste nelle funzioni            | 6_Liste_funzioni.ipynb                                                   | [6_Liste_funzioni.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/6_Liste_funzioni/6_Liste_funzioni.ipynb) |
| Soluzione di problemi: adattamento algoritmi| 7_Adattamento_algoritmi.ipynb                                            | [7_Adattamento_algoritmi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/7_Adattamento_algoritmi/7_Adattamento_algoritmi.ipynb) |
| Soluzione di problemi: esperimenti concreti | 8_Esperimenti_concreti.ipynb                                             | [8_Esperimenti_concreti.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/8_Algoritmi_concreti/8_Esperimenti_concreti.ipynb) |
| Tabelle                                     | 9_Tabelle.ipynb                                                          | [9_Tabelle.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/9_Tabelle/9_Tabelle.ipynb) |
| Riepilogo del capitolo                      | 10_Riepilogo.ipynb                                                        | [10_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/10_Riepilogo/10_Riepilogo.ipynb) |
| Esercizi                                    | 11_Esercizi.ipynb                                                         | [11_Esercizi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/11_Esercizi/11_Esercizi.ipynb) |
| Auto-valutazione                            | 12_Auto_valutazione.ipynb                                                | [12_Auto_valutazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo6_Liste/12_Auto_valutazione/12_Auto_valutazione.ipynb) |

**🎯 Obiettivo del Capitolo**:  
Utilizzare le liste e le tuple per rappresentare e manipolare collezioni di dati; realizzare semplici algoritmi di elaborazione; comprendere strutture complesse come tabelle e tecniche avanzate come le list comprehension.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Creare e modificare liste e tuple in Python  
- Distinguere tra liste mutabili e tuple immutabili  
- Utilizzare list comprehension per creare liste in modo conciso  
- Implementare algoritmi efficienti che sfruttano le liste  
- Lavorare con tabelle come liste di liste  
- Integrare liste e tuple all'interno di funzioni  
- Applicare tecniche di manipolazione avanzata con cicli e condizioni 

### 📘 Capitolo 7 - Gestione delle Eccezioni

In questo capitolo impareremo a gestire errori e situazioni eccezionali in Python. Le eccezioni ci permettono di scrivere codice robusto che può reagire in modo controllato a problemi durante l'esecuzione.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo7_Eccezioni/0_Obiettivi/0_Obiettivi.ipynb) |
| Nozioni base sulle eccezioni            | 1_Nozioni_base_eccezioni.ipynb                                           | [1_Nozioni_base_eccezioni.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo7_Eccezioni/1_Nozioni_base/1_Nozioni_base_eccezioni.ipynb) |
| Applicazione: gestione errori complessa     | 2_Applicazione.ipynb                                                     | [2_Applicazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo7_Eccezioni/2_Applicazione/2_Applicazione.ipynb) |
| Riepilogo del capitolo                      | 3_Riepilogo.ipynb                                                        | [3_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo7_Eccezioni/3_Riepilogo/3_Riepilogo.ipynb) |
| Esercizi                                    | 4_Esercizi.ipynb                                                         | [4_Esercizi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo7_Eccezioni/4_Esercizi/4_Esercizi.ipynb) |
| Auto-valutazione                            | 5_Auto_valutazione.ipynb                                                 | [5_Auto_valutazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo7_Eccezioni/5_Auto_valutazione/5_Auto_valutazione.ipynb) |

**🎯 Obiettivo del Capitolo:**  
Acquisire competenze nella gestione degli errori e nel controllo del flusso di esecuzione attraverso il meccanismo delle eccezioni.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Implementare blocchi try/except/finally efficaci  
- Creare e gestire eccezioni personalizzate  
- Distinguere tra diversi tipi di errori  
- Applicare strategie di gestione errori in scenari reali  


### 📘 Capitolo 8 - File e Formati Dati

In questo capitolo approfondiremo la gestione di file e formati dati complessi. Impareremo a lavorare con diversi tipi di file e a utilizzare context manager per la gestione sicura delle risorse.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/0_Obiettivi/0_Obiettivi.ipynb) |
| Operazioni base su file di testo            | 1_Operazioni_file.ipynb                                                  | [1_Operazioni_file.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/1_Operazioni_file/1_Operazioni_file.ipynb) |
| Context Manager e with statement            | 2_Context_manager.ipynb                                                  | [2_Context_manager.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/2_Context_manager/2_Context_manager.ipynb) |
| Gestione file CSV                          | 3_CSV.ipynb                                                              | [3_CSV.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/3_CSV/3_CSV.ipynb) |
| Lavorare con JSON                          | 4_JSON.ipynb                                                             | [4_JSON.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/4_JSON/4_JSON.ipynb) |
| File binari e serializzazione              | 5_File_binari.ipynb                                                      | [5_File_binari.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/5_File_binari/5_File_binari.ipynb) |
| Argomenti da riga di comando               | 6_Argomenti_riga_comando.ipynb                                           | [6_Argomenti_riga_comando.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/6_Argomenti_riga_comando/6_Argomenti_riga_comando.ipynb) |
| Applicazione: convertitore di formati      | 7_Applicazione.ipynb                                                     | [7_Applicazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/7_Applicazione/7_Applicazione.ipynb) |
| Riepilogo del capitolo                      | 8_Riepilogo.ipynb                                                        | [8_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/8_Riepilogo/8_Riepilogo.ipynb) |
| Esercizi                                    | 9_Esercizi.ipynb                                                         | [9_Esercizi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/9_Esercizi/9_Esercizi.ipynb) |
| Auto-valutazione                            | 10_Auto_valutazione.ipynb                                                | [10_Auto_valutazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo8_File/10_Auto_valutazione/10_Auto_valutazione.ipynb) |

**🎯 Obiettivo del Capitolo:**  
Padroneggiare le operazioni su file e formati dati strutturati, utilizzare best practice per la gestione delle risorse e integrare dati esterni nei programmi.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Lavorare con file testuali, CSV e JSON  
- Utilizzare context manager per la gestione sicura delle risorse  
- Serializzare e deserializzare oggetti  
- Processare dati da diverse fonti esterne  
- Implementare semplici convertitori di formato  

### 📘 Capitolo 9 – Insiemi e dizionari

In questo capitolo esploreremo due strutture dati fondamentali in Python: gli insiemi (set) e i dizionari (dict). Questi strumenti permettono di gestire dati in modo efficiente, supportando operazioni avanzate come ricerche veloci, gestione di chiavi uniche e relazioni chiave-valore.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo9_Insiemi_Dizionari/0_Obiettivi/0_Obiettivi.ipynb) |
| 9.1 Insiemi                                 | 1_Insiemi.ipynb                                                          | [1_Insiemi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo9_Insiemi_Dizionari/1_Insiemi/1_Insiemi.ipynb) |
| 9.2 Dizionari                               | 2_Dizionari.ipynb                                                       | [2_Dizionari.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo9_Insiemi_Dizionari/2_Dizionari/2_Dizionari.ipynb) |
| 9.3 Strutture complesse                     | 3_Strutture_complesse.ipynb                                             | [3_Strutture_complesse.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo9_Insiemi_Dizionari/3_Strutture_complesse/3_Strutture_complesse.ipynb) |                            
| 9.4 Argomenti avanzati                      | 4_Argomenti_avanzati.ipynb                                              | [4_Argomenti_avanzati.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo9_Insiemi_Dizionari/4_Argomenti_avanzati/4_Argomenti_avanzati.ipynb) |
| Riepilogo del capitolo                      | 5_Riepilogo.ipynb                                                        | [5_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo9_Insiemi_Dizionari/5_Riepilogo/5_Riepilogo.ipynb) |
| Esercizi                                    | 6_Esercizi.ipynb                                                         | [6_Esercizi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo9_Insiemi_Dizionari/6_Esercizi/6_Esercizi.ipynb) |
| Auto-valutazione                            | 7_Auto_valutazione.ipynb                                                 | [7_Auto_valutazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo9_Insiemi_Dizionari/7_Auto_valutazione/7_Auto_valutazione.ipynb) |


🎯 **Obiettivo del Capitolo**:  
Padroneggiare l'uso di insiemi e dizionari per organizzare dati complessi, ottimizzare operazioni di ricerca e manipolare strutture annidate in Python.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Creare e modificare insiemi e dizionari con operazioni avanzate.  
- Applicare metodi specifici come `union()`, `intersection()`, `get()`, e `update()`.  
- Gestire strutture dati annidate (es. dizionari di liste).  
- Risolvere problemi reali sfruttando l'efficienza di set e dict.  
- Ottimizzare algoritmi tramite comprehension e ordinamento di dizionari.
- 
### 📘 Capitolo 10 – Oggetti e classi

In questo capitolo verrà approfondita la programmazione orientata agli oggetti (OOP) in Python, con un focus su concetti avanzati come ereditarietà, polimorfismo, incapsulamento e design pattern. Imparerai a progettare classi robuste, gestire relazioni tra oggetti e applicare principi OOP per risolvere problemi complessi.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/0_Obiettivi/0_Obiettivi.ipynb) |
| 10.1 Programmazione orientata agli oggetti   | 1_POO_Introduzione.ipynb                                                 | [1_POO_Introduzione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/1_POO/1_POO_Introduzione.ipynb) |
| 10.2 Creazione di classi e oggetti           | 2_Classi_Oggetti.ipynb                                                   | [2_Classi_Oggetti.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/2_Classi/2_Classi_Oggetti.ipynb) |
| 10.3 Ereditarietà e polimorfismo             | 3_Ereditarieta_Polimorfismo.ipynb                                        | [3_Ereditarieta_Polimorfismo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/3_OOP_Avanzato/3_Ereditarieta_Polimorfismo.ipynb) |
| 10.4 Incapsulamento e proprietà              | 4_Incapsulamento.ipynb                                                   | [4_Incapsulamento.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/4_Incapsulamento/4_Incapsulamento.ipynb) |
| 10.5 Classi astratte e interfacce            | 5_Classi_Astratte.ipynb                                                  | [5_Classi_Astratte.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/5_Classi_Astratte/5_Classi_Astratte.ipynb) |
| 10.6 Metodi statici e di classe              | 6_Metodi_Statici.ipynb                                                   | [6_Metodi_Statici.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/6_Metodi_Statici/6_Metodi_Statici.ipynb) |
| 10.7 Decoratori e magic methods              | 7_Decoratori_Magic.ipynb                                                 | [7_Decoratori_Magic.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/7_Decoratori/7_Decoratori_Magic.ipynb) |
| 10.8 Gestione delle eccezioni in OOP         | 8_Errori_OOP.ipynb                                                       | [8_Errori_OOP.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/8_Errori/8_Errori_OOP.ipynb) |
| 10.10 Design pattern (Singleton, Factory)     | 10_Design_Pattern.ipynb                                                   | [10_Design_Pattern.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/10_Design_Pattern/10_Design_Pattern.ipynb) |
| 10.10 Serializzazione di oggetti             | 10_Serializzazione.ipynb                                                 | [10_Serializzazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/10_Serializzazione/10_Serializzazione.ipynb) |
| 10.11 Metaclassi e reflection                | 11_Metaclassi.ipynb                                                      | [11_Metaclassi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/11_Metaclassi/11_Metaclassi.ipynb) |
| Riepilogo del capitolo                      | 0_Riepilogo.ipynb                                                        | [12_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/12_Riepilogo/0_Riepilogo.ipynb) |
| Esercizi di ripasso                         | 0_Esercizi_ripasso.ipynb                                                 | [13_Esercizi_ripasso.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/13_Esercizi/0_Esercizi_ripasso.ipynb) |
| Esercizi di programmazione                  | 1_Esercizi_programmazione.ipynb                                          | [14_Esercizi_programmazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/13_Esercizi/1_Esercizi_programmazione.ipynb) |
| Risposte alle domande di auto-valutazione   | 2_Soluzioni_commentate.ipynb                                             | [15_Soluzioni_commentate.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo10_Oggetti_Classi/14_Auto_valutazione/2_Soluzioni_commentate.ipynb) |

🎯 **Obiettivo del Capitolo**:  
Padroneggiare i principi avanzati della programmazione orientata agli oggetti, progettare architetture software modulari e applicare pattern risolutivi per problemi complessi.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Implementare ereditarietà, polimorfismo e incapsulamento.  
- Utilizzare classi astratte, interfacce e decoratori.  
- Applicare design pattern come Singleton e Factory.  
- Gestire la serializzazione e deserializzazione di oggetti.  
- Comprendere il ruolo delle metaclassi e della reflection.  
- Progettare sistemi OOP mantenibili e scalabili.

### 📘 Capitolo 11 – Ereditarietà

In questo capitolo esploreremo l’ereditarietà, uno dei pilastri della programmazione orientata agli oggetti. Approfondiremo la creazione di gerarchie di classi, il polimorfismo e l’utilizzo avanzato di costruttori e metodi sovrascritti. Inoltre, introdurremo concetti avanzati come l’ereditarietà multipla e i design pattern basati su gerarchie.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/0_Obiettivi/0_Obiettivi.ipynb) |
| 11.1 Gerarchie di ereditarietà              | 1_Gerarchie.ipynb                                                        | [1_Gerarchie.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/1_Gerarchie/1_Gerarchie.ipynb) |
| 11.2 Creazione di sottoclassi               | 2_Sottoclassi.ipynb                                                      | [2_Sottoclassi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/2_Sottoclassi/2_Sottoclassi.ipynb) |
| 11.3 Costruttori e super()                  | 3_Costruttori_Super.ipynb                                                | [3_Costruttori_Super.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/3_Costruttori/3_Costruttori_Super.ipynb) |
| 11.4 Sovrascrittura di metodi               | 4_Override.ipynb                                                         | [4_Override.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/4_Override/4_Override.ipynb) |
| 11.5 Polimorfismo dinamico                  | 5_Polimorfismo.ipynb                                                     | [5_Polimorfismo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/5_Polimorfismo/5_Polimorfismo.ipynb) |
| 11.6 Ereditarietà multipla e Mixin          | 6_Ereditarieta_Multipla.ipynb                                            | [6_Ereditarieta_Multipla.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/6_Multipla/6_Ereditarieta_Multipla.ipynb) |
| 11.7 Classi astratte e interfacce           | 7_Classi_Astratte.ipynb                                                  | [7_Classi_Astratte.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/7_Astratte/7_Classi_Astratte.ipynb) |
| 11.8 Design pattern: Template Method        | 8_Template_Method.ipynb                                                  | [8_Template_Method.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/8_Pattern/8_Template_Method.ipynb) |
| 11.9 Applicazione: gerarchia di forme       | 9_Forme_Geometriche.ipynb                                                | [9_Forme_Geometriche.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/9_Forme/9_Forme_Geometriche.ipynb) |
| Riepilogo del capitolo                      | 0_Riepilogo.ipynb                                                        | [0_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/11_Riepilogo/0_Riepilogo.ipynb) |
| Esercizi di ripasso                         | 0_Esercizi_ripasso.ipynb                                                 | [0_Esercizi_ripasso.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/11_Esercizi/0_Esercizi_ripasso.ipynb) |
| Esercizi di programmazione                  | 1_Esercizi_programmazione.ipynb                                          | [1_Esercizi_programmazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/11_Esercizi/1_Esercizi_programmazione.ipynb) |
| Risposte alle domande di auto-valutazione   | 2_Soluzioni_commentate.ipynb                                             | [2_Soluzioni_commentate.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo11_Ereditarieta/12_Auto_valutazione/2_Soluzioni_commentate.ipynb) |

🎯 **Obiettivo del Capitolo**:  
Padroneggiare l’ereditarietà in Python, progettare gerarchie complesse e applicare polimorfismo e design pattern per creare codice modulare e riutilizzabile.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Creare gerarchie di classi con sottoclassi e superclassi.  
- Utilizzare `super()` per gestire i costruttori in contesti ereditari.  
- Sovrascrivere metodi e sfruttare il polimorfismo dinamico.  
- Implementare ereditarietà multipla e classi astratte.  
- Applicare il pattern Template Method.  
- Progettare gerarchie per problemi reali (es. forme geometriche).

### 📘 Capitolo 12 – Ricorsione

In questo capitolo esploreremo la ricorsione, una tecnica di programmazione potente per risolvere problemi complessi suddividendoli in sotto-problemi più semplici. Approfondiremo casi d’uso, ottimizzazioni e applicazioni avanzate, confrontando anche approcci ricorsivi e iterativi.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/0_Obiettivi/0_Obiettivi.ipynb) |
| 12.1 Numeri triangolari ricorsivi           | 1_Numeri_Triangolari.ipynb                                               | [1_Numeri_Triangolari.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/1_Numeri_Triangolari/1_Numeri_Triangolari.ipynb) |
| 12.2 Pensare ricorsivamente                 | 2_Problem_Solving.ipynb                                                  | [2_Problem_Solving.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/2_Problem_Solving/2_Problem_Solving.ipynb) |
| 12.3 Funzioni ausiliarie ricorsive          | 3_Funzioni_Ausiliarie.ipynb                                              | [3_Funzioni_Ausiliarie.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/3_Funzioni_Ausiliarie/3_Funzioni_Ausiliarie.ipynb) |
| 12.4 Efficienza e limiti della ricorsione   | 4_Efficienza.ipynb                                                       | [4_Efficienza.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/4_Efficienza/4_Efficienza.ipynb) |
| 12.5 Generazione di permutazioni            | 5_Permutazioni.ipynb                                                     | [5_Permutazioni.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/5_Permutazioni/5_Permutazioni.ipynb) |
| 12.6 Algoritmi di backtracking              | 6_Backtracking.ipynb                                                     | [6_Backtracking.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/6_Backtracking/6_Backtracking.ipynb) |
| 12.7 Ricorsione mutua                       | 7_Ricorsione_Mutua.ipynb                                                 | [7_Ricorsione_Mutua.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/7_Ricorsione_Mutua/7_Ricorsione_Mutua.ipynb) |
| 12.8 Memoizzazione e ottimizzazione         | 8_Memoizzazione.ipynb                                                    | [8_Memoizzazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/8_Memoizzazione/8_Memoizzazione.ipynb) |
| 12.9 Ricorsione vs. Iterazione              | 9_Confronto_Iterazione.ipynb                                             | [9_Confronto_Iterazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/9_Confronto_Iterazione/9_Confronto_Iterazione.ipynb) |
| 12.10 Divide et Impera (es. QuickSort)      | 10_Divide_Impera.ipynb                                                   | [10_Divide_Impera.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/10_Divide_Impera/10_Divide_Impera.ipynb) |
| Riepilogo del capitolo                      | 0_Riepilogo.ipynb                                                        | [0_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/12_Riepilogo/0_Riepilogo.ipynb) |
| Esercizi di ripasso                         | 0_Esercizi_ripasso.ipynb                                                 | [0_Esercizi_ripasso.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/12_Esercizi/0_Esercizi_ripasso.ipynb) |
| Esercizi di programmazione                  | 1_Esercizi_programmazione.ipynb                                          | [1_Esercizi_programmazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/12_Esercizi/1_Esercizi_programmazione.ipynb) |
| Risposte alle domande di auto-valutazione   | 2_Soluzioni_commentate.ipynb                                             | [2_Soluzioni_commentate.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo12_Ricorsione/13_Auto_valutazione/2_Soluzioni_commentate.ipynb) |

🎯 **Obiettivo del Capitolo**:  
Padroneggiare la ricorsione per risolvere problemi complessi, ottimizzare soluzioni con tecniche avanzate e comprendere i trade-off tra approcci ricorsivi e iterativi.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Progettare algoritmi ricorsivi per problemi matematici e strutturati.  
- Applicare il backtracking e la ricorsione mutua.  
- Ottimizzare funzioni ricorsive con memoizzazione.  
- Confrontare efficienza e leggibilità di ricorsione vs. iterazione.  
- Implementare algoritmi divide et impera (es. QuickSort).  
- Risolvere esercizi pratici con pattern ricorsivi avanzati.

### 📘 Capitolo 13 – Ordinamento e Ricerca

In questo capitolo approfondiremo gli algoritmi di ordinamento e ricerca, analizzandone le prestazioni e le complessità. Impareremo a confrontare diverse strategie e a stimare i tempi di esecuzione per risolvere problemi in modo efficiente.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/0_Obiettivi/0_Obiettivi.ipynb) |
| 13.1 Ordinamento per selezione              | 1_Ordinamento_Selezione.ipynb                                            | [1_Ordinamento_Selezione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/1_Ordinamento_Selezione/1_Ordinamento_Selezione.ipynb) |
| 13.2 Misurazione prestazioni ordinamento    | 2_Misurazione_Prestazioni.ipynb                                          | [2_Misurazione_Prestazioni.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/2_Misurazione_Prestazioni/2_Misurazione_Prestazioni.ipynb) |
| 13.3 Analisi prestazioni selezione          | 3_Analisi_Prestazioni_Selezione.ipynb                                    | [3_Analisi_Prestazioni_Selezione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/3_Analisi_Prestazioni_Selezione/3_Analisi_Prestazioni_Selezione.ipynb) |
| 13.4 Ordinamento per fusione (merge sort)   | 4_Ordinamento_Fusione.ipynb                                              | [4_Ordinamento_Fusione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/4_Ordinamento_Fusione/4_Ordinamento_Fusione.ipynb) |
| 13.5 Analisi ordinamento fusione           | 5_Analisi_Fusione.ipynb                                                  | [5_Analisi_Fusione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/5_Analisi_Fusione/5_Analisi_Fusione.ipynb) |
| 13.6 Effettuare ricerche                    | 6_Ricerche.ipynb                                                         | [6_Ricerche.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/6_Ricerche/6_Ricerche.ipynb) |
| 13.7 Stima tempo di esecuzione              | 7_Stima_Tempo.ipynb                                                      | [7_Stima_Tempo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/7_Stima_Tempo/7_Stima_Tempo.ipynb) |
| Riepilogo del capitolo                      | 8_Riepilogo.ipynb                                                        | [8_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/8_Riepilogo/8_Riepilogo.ipynb) |
| Esercizi di ripasso                         | 9_Esercizi_Ripasso.ipynb                                                 | [9_Esercizi_Ripasso.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/9_Esercizi_Ripasso/9_Esercizi_Ripasso.ipynb) |
| Esercizi di programmazione                  | 10_Esercizi_Programmazione.ipynb                                         | [10_Esercizi_Programmazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/10_Esercizi_Programmazione/10_Esercizi_Programmazione.ipynb) |
| Risposte alle domande di auto-valutazione   | 11_Soluzioni_Autovalutazione.ipynb                                       | [11_Soluzioni_Autovalutazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo13_Ordinamento_Ricerca/11_Soluzioni_Autovalutazione/11_Soluzioni_Autovalutazione.ipynb) |

🎯 **Obiettivo del Capitolo**:  
Padroneggiare gli algoritmi di ordinamento e ricerca, analizzarne le prestazioni e applicare tecniche per stimare l’efficienza degli algoritmi in diversi scenari.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Implementare e confrontare algoritmi di ordinamento (selection sort, merge sort).  
- Misurare e analizzare le prestazioni degli algoritmi in termini di complessità temporale.  
- Applicare ricerche lineare e binaria in contesti pratici.  
- Stimare il tempo di esecuzione in base alla complessità (O(n), O(n²), O(n log n)).  
- Risolvere problemi utilizzando schemi algoritmici come il divide et impera.  
- Ottimizzare soluzioni attraverso l’analisi delle prestazioni.

### 📘 Capitolo 14 - Librerie Standard Avanzate

In questo capitolo esploreremo alcune librerie fondamentali della standard library di Python, imparando a sfruttarne le potenzialità per operazioni matematiche, gestione del tempo, interazione con il sistema operativo e creazione di programmi più professionali.

| Sezione                                     | Notebook                                                                 | Link                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obiettivi del capitolo                      | 0_Obiettivi.ipynb                                                        | [0_Obiettivi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/0_Obiettivi/0_Obiettivi.ipynb) |
| Fondamenti matematici (math/random)        | 1_Math_random.ipynb                                                      | [1_Math_random.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/1_Math_random/1_Math_random.ipynb) |
| Gestione date/ore (datetime)               | 2_Datetime.ipynb                                                         | [2_Datetime.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/2_Datetime/2_Datetime.ipynb) |
| Interazione con il sistema (os/sys)        | 3_Os_sys.ipynb                                                           | [3_Os_sys.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/3_Os_sys/3_Os_sys.ipynb) |
| Parsing argomenti (argparse)               | 4_Argparse.ipynb                                                         | [4_Argparse.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/4_Argparse/4_Argparse.ipynb) |
| Funzioni avanzate (**kwargs)               | 5_Kwargs.ipynb                                                           | [5_Kwargs.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/5_Kwargs/5_Kwargs.ipynb) |
| Compressione dati (zipfile/gzip)           | 6_Compressione.ipynb                                                     | [6_Compressione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/6_Compressione/6_Compressione.ipynb) |
| Riepilogo del capitolo                      | 7_Riepilogo.ipynb                                                        | [7_Riepilogo.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/7_Riepilogo/7_Riepilogo.ipynb) |
| Esercizi                                    | 8_Esercizi.ipynb                                                         | [8_Esercizi.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/8_Esercizi/8_Esercizi.ipynb) |
| Auto-valutazione                            | 9_Auto_valutazione.ipynb                                                 | [9_Auto_valutazione.ipynb](https://colab.research.google.com/github/lorenzo-arcioni/programmazione-python-base/blob/main/Capitolo14_Librerie/9_Auto_valutazione/9_Auto_valutazione.ipynb) |

**🎯 Obiettivo del Capitolo:**  
Padroneggiare l'uso di librerie specializzate per risolvere problemi complessi, gestire input/output avanzati e migliorare l'interazione con il sistema.

**Alla fine del capitolo lo studente sarà in grado di**:  
- Utilizzare funzioni matematiche avanzate e generare numeri casuali  
- Manipolare date e ore con precisione  
- Navigare nel filesystem e gestire variabili d'ambiente  
- Creare programmi con interfaccia a riga di comando professionale  
- Gestire parametri flessibili nelle funzioni con **kwargs  
- Comprimere/decomprimere file in diversi formati  
- Integrare multiplie librerie per soluzioni ibride

## Come usare il correttore automatico 🧪

Per ogni esercizio, dovrai scrivere il codice all’interno del file `main.py`.

Il file `test.py` si occupa di verificare automaticamente che le soluzioni siano corrette. Puoi eseguire il test così:

```python
python test.py
```

🔁 Se invece vuoi testare le **soluzioni proposte**, esegui:

```python
python test.py -s
```

📌 Durante l’esecuzione:
- Il correttore **nasconde l’output del tuo script** (es. eventuali `print()`).
- Ogni test superato viene indicato con `[OK]` in verde.
- In caso di errore, viene mostrato un messaggio ❌.

💡 Consiglio: prima di eseguire il test verifica il funzionamento del tuo script con:

```python
python main.py
```
In questo modo ti sarà più facile risolvere eventuali errori.

## Progetti pratici 🛠️
Qui trovi una selezione di progetti interattivi per mettere in pratica le tue abilità:

| Progetto                          | Descrizione                                                                 | Competenze sviluppate                    |
|-----------------------------------|-----------------------------------------------------------------------------|------------------------------------------|
| **📈 Analizzatore di Dati**       | Elabora dataset reali con Pandas e crea visualizzazioni dinamiche.          | Liste, funzioni, librerie esterne        |
| **🎮 Gioco dell'Indovina Numero** | Sviluppa un gioco interattivo con tentativi limitati e livelli di difficoltà. | Cicli, condizioni, gestione input/output |
| **📝 Gestore di Task**            | Crea un'app per organizzare task con salvataggio su file e notifiche.        | File I/O, dizionari, eccezioni           |
| **🌐 Web Scraper Base**           | Estrai dati da pagine web utilizzando BeautifulSoup e requests.             | HTTP requests, parsing HTML              |

🔗 **Collegamento ai progetti**: [Repository GitHub](https://github.com/lorenzo-arcioni/programmazione-python-base/tree/main/Progetti)

## Conclusione 🏁
🌟 **Hai completato il viaggio!**  
Ora possiedi gli strumenti per affrontare problemi complessi, automatizzare task e contribuire a progetti open source. Ricorda: la programmazione è una palestra mentale—continua a esercitarti e a esplorare nuove sfide!

## Prossimi passi
🛣️ **Dopo questo corso, esplora:**  
- **🔥 Python Avanzato**: Decoratori, generatori e ottimizzazione del codice.  
- **📊 Data Science con Python**: Analisi dati, Pandas e visualizzazioni.  
- **🤖 Machine Learning**: Modelli predittivi e reti neurali.  
- **🌐 Sviluppo Web**: Django, Flask e creazione di API.  

💡 *Consiglio: Partecipa ai progetti pratici per consolidare ciò che impari!*

## Risorse Aggiuntive 📚
- **Libri consigliati**: *"Python Crash Course"* di Eric Matthes, *"Automate the Boring Stuff"* di Al Sweigart.  
- **Community**: Partecipa a forum come [Stack Overflow](https://stackoverflow.com/) e [Reddit r/learnpython](https://www.reddit.com/r/learnpython/).  
- **Tool utili**: [PyCharm](https://www.jetbrains.com/pycharm/) (IDE avanzato), [Replit](https://replit.com/) (coding online).  

## Certificazione 🏅
Ottieni il **Certificato di Completamento** superando tutti gli esercizi e i progetti!  
🔗 [Richiedi il certificato](https://tuo-sito.com/certificato) (simulato).

## Community e Supporto 🤝
- **Gruppo Telegram**: Unisciti a [Python Base Community](https://t.me/link-finto) per confrontarti con altri studenti.  
- **Office Hour**: Sessioni live settimanali per dubbi e approfondimenti.  
- **Feedback**: Aiutaci a migliorare il corso compilando [questo form](https://tuo-sito.com/feedback).  

✨ *Il tuo successo è la mia missione!*
