## 🔁 SET 1 – Tracce di Esercizi sul ciclo `for`

---

### 🧪 Esercizio 1: Somma dei numeri pari da 1 a N

**Descrizione:**  
Scrivi un programma che chiede all’utente un numero intero positivo `N` e calcola la somma di tutti i numeri pari da 1 a `N` (incluso).

**Esempio 1**  
Input: 10  
Output: 30

**Esempio 2**  
Input: 7  
Output: 12

**Hint:** Usa una variabile somma e incrementala solo se il numero è divisibile per 2.

---

### 🧪 Esercizio 2: Tabellina di un numero

**Descrizione:**  
Chiedi all’utente un numero `n` e stampa la sua tabellina da 1 a 10, con il formato `n x i = risultato`.

**Esempio 1**  
Input: 5  
Output:  
5 x 1 = 5  
...  
5 x 10 = 50

**Esempio 2**  
Input: 3  
Output:  
3 x 1 = 3  
...  
3 x 10 = 30

**Hint:** Usa un ciclo da 1 a 10 e moltiplica `n * i`.

---

### 🧪 Esercizio 3: Conta multipli di 3 tra 1 e N

**Descrizione:**  
Scrivi un programma che chiede all’utente un numero `N` e conta quanti numeri tra 1 e `N` sono divisibili per 3.

**Esempio 1**  
Input: 10  
Output: 3

**Esempio 2**  
Input: 20  
Output: 6

**Hint:** Incrementa un contatore se `i % 3 == 0`.

---

### 🧪 Esercizio 4: Fattoriale di un numero

**Descrizione:**  
Scrivi un programma che calcola il fattoriale di un numero `n` inserito dall’utente. Il fattoriale di `n` è `n * (n-1) * ... * 1`.

**Esempio 1**  
Input: 5  
Output: 120

**Esempio 2**  
Input: 4  
Output: 24

**Hint:** Inizia da 1 e moltiplica progressivamente fino a `n`.

---

### 🧪 Esercizio 5: Somma delle cifre di un numero

**Descrizione:**  
Chiedi all’utente un numero intero positivo e calcola la somma delle sue cifre.

**Esempio 1**  
Input: 123  
Output: 6

**Esempio 2**  
Input: 409  
Output: 13

**Hint:** Usa una variabile temporanea e dividi per 10 per estrarre le cifre.

---

### 🧪 Esercizio 6: Stampa triangolo di asterischi

**Descrizione:**  
Chiedi un numero `n` e stampa un triangolo di altezza `n` con asterischi.

**Esempio 1**  
Input: 4  
Output:
```
*  
**  
***  
****
```

**Esempio 2**  
Input: 2  
Output: 
``` 
*  
**
```

**Hint:** Usa un ciclo esterno da 1 a `n` e uno interno per stampare gli asterischi.

---

### 🧪 Esercizio 7: Potenza di un numero (senza usare pow)

**Descrizione:**  
Calcola `base^esponente` con una moltiplicazione ripetuta.

**Esempio 1**  
Input: base = 2, esponente = 3  
Output: 8

**Esempio 2**  
Input: base = 5, esponente = 0  
Output: 1

**Hint:** Moltiplica `base` per sé stesso `esponente` volte.

---

### 🧪 Esercizio 8: Stampa numeri divisibili per 2 o 5 tra 1 e N

**Descrizione:**  
Chiedi all’utente un numero `N` e stampa tutti i numeri da 1 a `N` che sono divisibili per 2 o per 5.

**Esempio 1**  
Input: 10  
Output: 2 4 5 6 8 10

**Esempio 2**  
Input: 7  
Output: 2 4 5 6

**Hint:** Usa `if (i % 2 == 0 || i % 5 == 0)`.

---

### 🧪 Esercizio 9: Stampa dei quadrati dei numeri da 1 a N

**Descrizione:**  
Stampa i quadrati perfetti da 1 a `N` (es. 1, 4, 9, 16...).

**Esempio 1**  
Input: 5  
Output: 1 4 9 16 25

**Esempio 2**  
Input: 3  
Output: 1 4 9

**Hint:** Usa `i * i` per calcolare il quadrato di ogni numero.

---

### 🧪 Esercizio 10: Somma dei numeri dispari in un intervallo

**Descrizione:**  
Chiedi due numeri interi `a` e `b` (con `a < b`) e calcola la somma di tutti i numeri dispari tra `a` e `b`.

**Esempio 1**  
Input: a = 1, b = 10  
Output: 25

**Esempio 2**  
Input: a = 4, b = 9  
Output: 21

**Hint:** Usa `if (i % 2 != 0)` per trovare i dispari tra `a` e `b`.

---

## 📚 SET 2 – Esercizi su Array Monodimensionali (con input da tastiera)

---

### 🧪 Esercizio 1: Somma degli elementi di un array

**Descrizione:**  
Chiedi all’utente di inserire `N` numeri interi in un array e stampa la somma di tutti gli elementi.

**Esempio 1**  
Input: 5 elementi → {1, 2, 3, 4, 5}  
Output: Somma = 15

**Esempio 2**  
Input: 3 elementi → {10, 20, 30}  
Output: Somma = 60

**Hint:** Scorri l’array e accumula la somma in una variabile.

---

### 🧪 Esercizio 2: Calcola la media degli elementi

**Descrizione:**  
Leggi `N` numeri interi in un array e calcola la loro media.

**Esempio 1**  
Input: 4 elementi → {2, 4, 6, 8}  
Output: Media = 5.0

**Esempio 2**  
Input: 2 elementi → {10, 5}  
Output: Media = 7.5

**Hint:** Usa `float somma` per ottenere un risultato decimale.

---

### 🧪 Esercizio 3: Trova il numero massimo

**Descrizione:**  
Dopo aver inserito `N` elementi in un array, stampa il valore massimo.

**Esempio 1**  
Input: 3 elementi → {1, 9, 4}  
Output: Massimo = 9

**Esempio 2**  
Input: 5 elementi → {-5, -2, -9, -1, -3}  
Output: Massimo = -1

**Hint:** Inizia con il primo elemento e confronta tutti gli altri.

---

### 🧪 Esercizio 4: Trova il numero minimo

**Descrizione:**  
Chiedi `N` numeri e trova il più piccolo.

**Esempio 1**  
Input: 4 elementi → {10, 2, 8, 6}  
Output: Minimo = 2

**Esempio 2**  
Input: 3 elementi → {-1, -10, -5}  
Output: Minimo = -10

**Hint:** Inizia con il primo elemento e aggiorna il minimo se trovi uno più piccolo.

---

### 🧪 Esercizio 5: Conta quanti numeri sono pari

**Descrizione:**  
Leggi `N` numeri e stampa quanti di questi sono pari.

**Esempio 1**  
Input: 5 elementi → {1, 2, 3, 4, 5}  
Output: 2 numeri pari

**Esempio 2**  
Input: 4 elementi → {6, 7, 8, 10}  
Output: 3 numeri pari

**Hint:** Usa `if (numero % 2 == 0)` per identificare i pari.

---

### 🧪 Esercizio 6: Stampa l’array al contrario

**Descrizione:**  
Dopo aver caricato un array di `N` numeri, stampalo al contrario.

**Esempio 1**  
Input: 3 elementi → {10, 20, 30}  
Output: 30 20 10

**Esempio 2**  
Input: 4 elementi → {1, 2, 3, 4}  
Output: 4 3 2 1

**Hint:** Usa un ciclo che parte da `N-1` fino a 0.

---

### 🧪 Esercizio 7: Conta quante volte compare un numero

**Descrizione:**  
Inserisci `N` numeri in un array, poi un numero `X`, e conta quante volte `X` appare.

**Esempio 1**  
Input: array = {1, 2, 3, 2, 4}, X = 2  
Output: 2 volte

**Esempio 2**  
Input: array = {5, 5, 5, 5, 5}, X = 5  
Output: 5 volte

**Hint:** Ogni volta che `array[i] == X`, incrementa un contatore.

---

### 🧪 Esercizio 8: Verifica se un numero è presente

**Descrizione:**  
Controlla se un numero `X` è presente in un array di `N` numeri.

**Esempio 1**  
Input: array = {3, 6, 9, 12}, X = 9  
Output: Presente

**Esempio 2**  
Input: array = {1, 2, 3, 4}, X = 5  
Output: Non presente

**Hint:** Usa una variabile booleana o esci dal ciclo con `break` quando trovi `X`.

---

### 🧪 Esercizio 9: Copia un array in un secondo array

**Descrizione:**  
Crea una copia esatta del primo array in un secondo array.

**Esempio 1**  
Input: {1, 2, 3, 4}  
Output: Copia = {1, 2, 3, 4}

**Esempio 2**  
Input: {5, 10, 15}  
Output: Copia = {5, 10, 15}

**Hint:** Usa un ciclo e assegna `array2[i] = array1[i]`.

---

### 🧪 Esercizio 10: Somma di due array

**Descrizione:**  
Dati due array `A` e `B` di dimensione `N`, crea un terzo array `C` dove ogni elemento `C[i] = A[i] + B[i]`.

**Esempio 1**  
Input: A = {1, 2, 3}, B = {4, 5, 6}  
Output: C = {5, 7, 9}

**Esempio 2**  
Input: A = {10, 20}, B = {1, 2}  
Output: C = {11, 22}

**Hint:** Somma gli elementi corrispondenti con un ciclo da 0 a N-1.

---

## 🔍 SET 3 – Esercizi su Ricerca Sequenziale, Massimo e Minimo

---

### 🧪 Esercizio 1: Ricerca di un valore in un array

**Descrizione:**  
Inserisci `N` numeri in un array e chiedi all’utente un numero `X`. Verifica se `X` è presente nell’array e stampa l’indice della sua prima occorrenza, oppure un messaggio se non è trovato.

**Esempio 1**  
Input: array = {4, 7, 9, 2, 5}, X = 9  
Output: Trovato all’indice 2

**Esempio 2**  
Input: array = {1, 3, 6, 8}, X = 10  
Output: Non trovato

**Hint:** Usa una variabile `trovato` e confronta ogni elemento.

---

### 🧪 Esercizio 2: Ricerca dell’elemento minimo

**Descrizione:**  
Leggi `N` numeri e stampa il valore minimo e il suo indice.

**Esempio 1**  
Input: {5, 2, 8, 1, 6}  
Output: Minimo = 1, indice = 3

**Esempio 2**  
Input: {-3, -1, -4, -2}  
Output: Minimo = -4, indice = 2

**Hint:** Confronta ogni elemento con il minimo corrente.

---

### 🧪 Esercizio 3: Ricerca del massimo e del minimo

**Descrizione:**  
Dopo aver caricato un array, stampa il valore massimo e minimo e i rispettivi indici.

**Esempio 1**  
Input: {3, 6, 9, 1, 7}  
Output: Max = 9 (2), Min = 1 (3)

**Esempio 2**  
Input: {4, 4, 4}  
Output: Max = 4 (0), Min = 4 (0)

**Hint:** Tieni traccia sia del valore che dell’indice.

---

### 🧪 Esercizio 4: Conta quante volte appare il valore massimo

**Descrizione:**  
Trova il massimo nell’array e conta quante volte compare.

**Esempio 1**  
Input: {2, 5, 3, 5, 5}  
Output: Max = 5, Occorrenze = 3

**Esempio 2**  
Input: {10, 20, 30}  
Output: Max = 30, Occorrenze = 1

**Hint:** Prima trova il massimo, poi fai un secondo ciclo per contarlo.

---

### 🧪 Esercizio 5: Ricerca dell’ultimo indice di un valore

**Descrizione:**  
Cerca l'ultima posizione in cui appare un numero `X`.

**Esempio 1**  
Input: array = {1, 2, 3, 2, 5}, X = 2  
Output: Ultimo indice = 3

**Esempio 2**  
Input: array = {4, 4, 4, 4}, X = 4  
Output: Ultimo indice = 3

**Hint:** Aggiorna l’indice ogni volta che trovi `X`.

---

### 🧪 Esercizio 6: Conta quante volte appare un valore negativo

**Descrizione:**  
Conta quanti numeri negativi ci sono in un array di `N` elementi.

**Esempio 1**  
Input: {-1, 2, -3, 4}  
Output: 2 negativi

**Esempio 2**  
Input: {0, 5, 7}  
Output: 0 negativi

**Hint:** Verifica `if (array[i] < 0)`.

---

### 🧪 Esercizio 7: Trova la seconda occorrenza di un numero

**Descrizione:**  
Cerca la seconda posizione in cui un numero `X` compare nell’array.

**Esempio 1**  
Input: array = {3, 1, 2, 1, 5}, X = 1  
Output: Seconda occorrenza all’indice 3

**Esempio 2**  
Input: array = {6, 7, 8, 9}, X = 7  
Output: Seconda occorrenza non trovata

**Hint:** Conta quante volte `X` appare e memorizza l’indice.

---

### 🧪 Esercizio 8: Trova il valore massimo tra i pari

**Descrizione:**  
Trova il valore massimo tra i numeri pari presenti nell’array.

**Esempio 1**  
Input: {1, 4, 2, 9, 6}  
Output: Max pari = 6

**Esempio 2**  
Input: {1, 3, 5}  
Output: Nessun pari trovato

**Hint:** Verifica se un numero è pari prima del confronto.

---

### 🧪 Esercizio 9: Ricerca di un valore approssimato (±1)

**Descrizione:**  
Dato un numero `X`, verifica se esiste un numero nell’array che sia uguale a `X`, oppure `X+1` o `X-1`.

**Esempio 1**  
Input: array = {2, 5, 7, 9}, X = 8  
Output: Trovato(7), Trovato (9)

**Esempio 2**  
Input: array = {1, 3, 5}, X = 4  
Output: Trovato (3), Trovato (5)

**Hint:** Confronta ogni elemento con `X`, `X+1` e `X-1`.

---

### 🧪 Esercizio 10: Conta quante volte due numeri consecutivi sono uguali

**Descrizione:**  
Conta le coppie di elementi consecutivi uguali in un array.

**Esempio 1**  
Input: {2, 2, 3, 3, 3, 4}  
Output: 3 coppie

**Esempio 2**  
Input: {1, 2, 3}  
Output: 0 coppie

**Hint:** Confronta ogni `array[i]` con `array[i+1]`.

## 🔃 SET 4 – Esercizi su Ordinamenti (Selection Sort, Insertion Sort, Bubble Sort)

---

### 🧪 Esercizio 1: Ordina un array con Bubble Sort (crescente)

**Descrizione:**  
Leggi `N` numeri da tastiera e ordina l’array in ordine crescente usando Bubble Sort.

**Esempio 1**  
Input: {4, 2, 1, 3}  
Output: {1, 2, 3, 4}

**Esempio 2**  
Input: {10, 5, 8}  
Output: {5, 8, 10}

---

### 🧪 Esercizio 2: Ordina un array con Bubble Sort (decrescente)

**Descrizione:**  
Stesso esercizio precedente, ma ordina in ordine decrescente.

**Esempio 1**  
Input: {3, 1, 2}  
Output: {3, 2, 1}

**Esempio 2**  
Input: {7, 4, 9}  
Output: {9, 7, 4}

---

### 🧪 Esercizio 3: Selection Sort (crescente)

**Descrizione:**  
Ordina un array usando Selection Sort in ordine crescente.

**Esempio 1**  
Input: {5, 1, 4, 2}  
Output: {1, 2, 4, 5}

**Esempio 2**  
Input: {8, 3, 7}  
Output: {3, 7, 8}

---

### 🧪 Esercizio 4: Selection Sort (decrescente)

**Descrizione:**  
Usa Selection Sort per ordinare un array in ordine decrescente.

**Esempio 1**  
Input: {2, 4, 1, 3}  
Output: {4, 3, 2, 1}

**Esempio 2**  
Input: {10, 7, 15}  
Output: {15, 10, 7}

---

### 🧪 Esercizio 5: Insertion Sort (crescente)

**Descrizione:**  
Ordina un array con Insertion Sort in ordine crescente.

**Esempio 1**  
Input: {5, 3, 4, 2}  
Output: {2, 3, 4, 5}

**Esempio 2**  
Input: {9, 7, 6}  
Output: {6, 7, 9}

---

### 🧪 Esercizio 6: Insertion Sort (decrescente)

**Descrizione:**  
Stesso esercizio di prima, ma in ordine decrescente.

**Esempio 1**  
Input: {1, 2, 3}  
Output: {3, 2, 1}

**Esempio 2**  
Input: {5, 10, 7}  
Output: {10, 7, 5}

---

### 🧪 Esercizio 7: Bubble Sort – stampa array dopo ogni passaggio

**Descrizione:**  
Durante il Bubble Sort, stampa l’array dopo ogni scambio di passaggio.

**Esempio 1**  
Input: {3, 2, 1}  
Output:  
Passo 1: {2, 3, 1}  
Passo 2: {2, 1, 3}  
Passo 3: {1, 2, 3}

**Esempio 2**  
Input: {4, 1}  
Output:  
Passo 1: {1, 4}

---

### 🧪 Esercizio 8: Verifica se l’array è già ordinato

**Descrizione:**  
Controlla se un array è già ordinato in modo crescente.

**Esempio 1**  
Input: {1, 2, 3}  
Output: Ordinato

**Esempio 2**  
Input: {4, 2, 5}  
Output: Non ordinato

---

### 🧪 Esercizio 9: Conta quanti scambi fa Bubble Sort

**Descrizione:**  
Conta quante volte avviene uno scambio durante Bubble Sort.

**Esempio 1**  
Input: {3, 2, 1}  
Output: 3 scambi

**Esempio 2**  
Input: {1, 2, 3}  
Output: 0 scambi

---

### 🧪 Esercizio 10: Ordina e poi stampa il massimo e il minimo

**Descrizione:**  
Usa Bubble Sort per ordinare un array e poi stampa primo e ultimo elemento (min e max).

**Esempio 1**  
Input: {5, 3, 1, 4}  
Output: Min = 1, Max = 5

**Esempio 2**  
Input: {10, 20, 15}  
Output: Min = 10, Max = 20

## Esercizi Verifica

<img src="./WhatsApp Image 2025-05-26 at 13.26.43.jpeg">

### Problema 1

Assumiamo di avere gia il vettore di numeri $a[\ ]$ e il numero di elementi $nMax$ e vogliamo calcolare il minimo, il massimo, la media e la somma degli elementi.

```c++
// PROBLEMA 1: Calcolo statistiche di un vettore
#include <iostream>
using namespace std;
int main() {
    
    // Calcolo minimo, massimo, somma
    int minimo = a[0];
    int massimo = a[0];
    int somma = 0;
    
    for(int i = 0; i < nMax; i++) {
        if(a[i] < minimo) minimo = a[i];
        if(a[i] > massimo) massimo = a[i];
        somma += a[i];
    }
    
    double media = (double)somma / nMax;
    
    cout << "Valore minimo: " << minimo << endl;
    cout << "Valore massimo: " << massimo << endl;
    cout << "Media degli elementi: " << media << endl;
    cout << "Somma degli elementi: " << somma << endl;
    
    return 0;
}
```

### Problema 2

```c++
// PROBLEMA 2: Ricerca binaria
#include <iostream>
using namespace std;
int main() {
    int n;
    cout << "Inserisci il numero di elementi: ";
    cin >> n;
    
    int arr[n];
    cout << "Inserisci " << n << " elementi ordinati:" << endl;
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int target;
    cout << "Inserisci il valore da cercare: ";
    cin >> target;
    
    // Ricerca binaria
    int left = 0, right = n - 1;
    int posizione = -1;
    
    while(left <= right) {
        int mid = (left + right) / 2;
        
        if(arr[mid] == target) {
            posizione = mid;
            break;
        }
        else if(arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    
    if(posizione != -1) {
        cout << "Elemento trovato alla posizione: " << posizione << endl;
    } else {
        cout << "Elemento non trovato" << endl;
    }
    
    return 0;
}
```

### Problema 3
Assumiamo di avere gia il vettore di numeri $a[\ ]$ e il numero di elementi $nMax$ e vogliamo stampare tutti gli elementi minori di 0.

```c++
// PROBLEMA 3: Stampa elementi minori di 0
#include <iostream>
using namespace std;
int main() {
   
    cout << "Elementi minori di 0:" << endl;
    bool trovato = false;
    
    for(int i = 0; i < nMax; i++) {
        if(a[i] < 0) {
            cout << a[i] << " ";
            trovato = true;
        }
    }
    
    if(!trovato) {
        cout << "Nessun elemento minore di 0";
    }
    cout << endl;
    
    return 0;
}
```

### Problema 4

Assumiamo di avere gia il vettore di numeri $a[\ ]$ e il numero di elementi $nMax$ e vogliamo stampare il doppio di ogni elemento.

```c++
// PROBLEMA 4: Stampa doppio di ogni elemento
#include <iostream>
using namespace std;
int main() {
    
    cout << "Il doppio di ogni elemento:" << endl;
    for(int i = 0; i < nMax; i++) {
        cout << (a[i] * 2) << " ";
    }
    cout << endl;
    
    return 0;
}
```

### Conclusioni

Se le assunzioni non dovessero essere ammesse, bisogna richiedere in input tutti i dati necessari per risolvere i problemi, come fatto nel problema 2.