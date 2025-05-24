# Esercizio 1: Calcola la media aritmetica di tre numeri interi
a = 4
b = 10
c = 6
media = (a + b + c) / 3

# Esercizio 2: Verifica se un numero è divisibile per 3 e per 5
numero = 30
divisibile = (numero % 3 == 0) and (numero % 5 == 0)

# Esercizio 3: Usa solo operatori aritmetici (+ e -) per scambiare i valori tra due variabili
e = 5
f = 7
e = e + f
f = e - f
e = e - f

# Esercizio 4: Estrai la cifra delle decine da un numero a tre cifre
numero = 472
decina = (numero // 10) % 10

# Esercizio 5: Calcola il numero minimo di monete da 2 euro e 1 euro per dare resto di 7€
resto = 7
due_euro = resto // 2
uno_euro = resto % 2

# Esercizio 6: Determina se la somma di tre numeri è pari
g = 4
h = 7
i = 3
somma_pari = ((g + h + i) % 2 == 0)

# Esercizio 7: Calcola l’area di un triangolo rettangolo di base 6 e altezza 4
base = 6
altezza = 4
area = (base * altezza) / 2

# Esercizio 8: Applica due operazioni combinate in una riga prima aggiungendo 2 a "risultato", e poi moltiplicandolo per 4
risultato = 3
risultato += 2
risultato *= 4

# Esercizio 9: Verifica il comportamento di -(-l) e +(+l) con l = -5
l = -5
doppio_negativo = -(-l)
doppio_positivo = +(+l)

# Esercizio 10: Rappresenta il numero 255 in base binaria, ottale e esadecimale
valore = 255
binario = bin(valore)
ottale = oct(valore)
esadecimale = hex(valore)

# Esercizio 11: Calcolo dello sconto applicato
# Un negozio applica uno sconto del 15% su un prodotto che costa 120€. Calcola il prezzo scontato.
prezzo_iniziale_11 = 120
sconto_11 = prezzo_iniziale_11 * 0.15
prezzo_finale_11 = prezzo_iniziale_11 - sconto_11

# Esercizio 12: Suddivisione del conto tra amici
# Quattro amici spendono in totale 97€. Dividi il conto equamente e calcola i centesimi avanzati.
conto_12 = 97
amici_12 = 4
quota_12 = conto_12 // amici_12
avanzo_12 = conto_12 % amici_12

# Esercizio 13: Converti minuti in ore e minuti
# Converti 367 minuti in ore e minuti.
minuti_totali_13 = 367
ore_13 = minuti_totali_13 // 60
minuti_13 = minuti_totali_13 % 60

# Esercizio 14: Calcolo del tempo di download
# Un file da 1500 MB viene scaricato a 2.5 MB/s. Calcola il tempo in minuti e secondi.
dimensione_file_14 = 1500
velocita_14 = 2.5
secondi_14 = int(dimensione_file_14 / velocita_14)
minuti_14 = secondi_14 // 60
resto_secondi_14 = secondi_14 % 60

# Esercizio 15: Estrarre la cifra centrale da un numero a cinque cifre
# Da 48319 estrai la cifra centrale (cioè 3).
numero_15 = 48319
cifra_centrale_15 = (numero_15 // 100) % 10

# Esercizio 16: Calcolo del tasso di crescita percentuale
# Una popolazione cresce da 1200 a 1380 abitanti. Calcola il tasso di crescita.
iniziali_16 = 1200
finali_16 = 1380
crescita_percentuale_16 = ((finali_16 - iniziali_16) / iniziali_16) * 100

# Esercizio 17: Calcolo della rata mensile di un abbonamento
# Un servizio costa 299€ per un anno. Calcola la rata mensile arrotondata a due decimali.
costo_annuo_17 = 299
rata_mensile_17 = round(costo_annuo_17 / 12, 2)

# Esercizio 18: Verifica se un anno è bisestile
# Un anno è bisestile se è divisibile per 4 ma non per 100, tranne se è anche divisibile per 400.
anno_18 = 2024
bisestile_18 = (anno_18 % 4 == 0 and anno_18 % 100 != 0) or (anno_18 % 400 == 0)

# Esercizio 19: Calcolo della distanza tra due punti (0,0) e (x,y)
# Calcola la distanza euclidea tra l’origine e il punto (6, 8).
x_19 = 6
y_19 = 8
distanza_19 = (x_19**2 + y_19**2) ** 0.5

# Esercizio 20: Trasforma un numero di secondi in ore, minuti e secondi
# Converti 7384 secondi nel formato h:m:s.
secondi_totali_20 = 7384
ore_20 = secondi_totali_20 // 3600
minuti_20 = (secondi_totali_20 % 3600) // 60
secondi_20 = secondi_totali_20 % 60