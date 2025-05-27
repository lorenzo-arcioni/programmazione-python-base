# Esercizio 1: Calcola la media geometrica di quattro numeri
a = 2
b = 8
c = 4
d = 16
media_geometrica = (a * b * c * d) ** (1/4)

# Esercizio 2: Verifica se un numero a quattro cifre è un palindromo
numero = 1331
prima_cifra = numero // 1000
ultima_cifra = numero % 10
seconda_cifra = (numero // 100) % 10
terza_cifra = (numero // 10) % 10
palindromo = (prima_cifra == ultima_cifra) and (seconda_cifra == terza_cifra)

# Esercizio 3: Calcola l'ipotenusa di un triangolo rettangolo con cateti 15 e 20
cateto_a = 15
cateto_b = 20
ipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5

# Esercizio 4: Estrai tutte le cifre da un numero a cinque cifre
numero = 67489
prima_cifra = numero // 10000
seconda_cifra = (numero // 1000) % 10
terza_cifra = (numero // 100) % 10
quarta_cifra = (numero // 10) % 10
quinta_cifra = numero % 10

# Esercizio 5: Calcola il numero di secondi in 2 giorni, 5 ore, 30 minuti e 45 secondi
giorni = 2
ore = 5
minuti = 30
secondi = 45
secondi_totali = giorni * 24 * 3600 + ore * 3600 + minuti * 60 + secondi

# Esercizio 6: Determina se la somma dei quadrati di due numeri è maggiore del loro prodotto moltiplicato per 3
x = 7
y = 9
confronto = (x**2 + y**2) > (3 * x * y)

# Esercizio 7: Calcola l'area di un trapezio con basi 12 e 8 e altezza 5
base_maggiore = 12
base_minore = 8
altezza = 5
area_trapezio = ((base_maggiore + base_minore) * altezza) / 2

# Esercizio 8: Risolvi l'espressione: ((a + b) * c - d) / (e + f)
a = 6
b = 4
c = 3
d = 8
e = 2
f = 3
risultato_espressione = ((a + b) * c - d) / (e + f)

# Esercizio 9: Calcola il resto della divisione di 2^10 per 7
base = 2
esponente = 10
divisore = 7
resto_potenza = (base ** esponente) % divisore

# Esercizio 10: Converti 5.75 ore in ore, minuti e secondi
ore_decimali = 5.75
ore_intere = int(ore_decimali)
minuti_da_decimali = int((ore_decimali - ore_intere) * 60)
secondi_da_decimali = int(((ore_decimali - ore_intere) * 60 - minuti_da_decimali) * 60)

# Esercizio 11: Calcolo dell'interesse semplice
capitale_11 = 2500
tasso_11 = 4.5
tempo_11 = 2.5
interesse_11 = (capitale_11 * tasso_11 * tempo_11) / 100
montante_11 = capitale_11 + interesse_11

# Esercizio 12: Problema della pizza
diametro_12 = 32
lato_quadratino_12 = 4
area_pizza_12 = 3.14159 * (diametro_12/2)**2
area_quadratino_12 = lato_quadratino_12**2
quadratini_12 = int(area_pizza_12 / area_quadratino_12)

# Esercizio 13: Calcola la velocità finale di un oggetto in caduta libera
g_13 = 9.81
altezza_13 = 45
velocita_finale_13 = (2 * g_13 * altezza_13) ** 0.5

# Esercizio 14: Converti una temperatura da Fahrenheit a Celsius e poi a Kelvin
fahrenheit_14 = 86
celsius_14 = (fahrenheit_14 - 32) * 5/9
kelvin_14 = celsius_14 + 273.15

# Esercizio 15: Calcola il numero formato invertendo le cifre di un numero a quattro cifre
numero_15 = 6274
cifra_1 = numero_15 // 1000
cifra_2 = (numero_15 // 100) % 10
cifra_3 = (numero_15 // 10) % 10
cifra_4 = numero_15 % 10
numero_invertito_15 = cifra_4 * 1000 + cifra_3 * 100 + cifra_2 * 10 + cifra_1

# Esercizio 16: Calcola la percentuale di sconto necessaria per ridurre un prezzo da 180€ a 135€
prezzo_originale_16 = 180
prezzo_scontato_16 = 135
percentuale_sconto_16 = ((prezzo_originale_16 - prezzo_scontato_16) / prezzo_originale_16) * 100

# Esercizio 17: Calcola il volume di una sfera con raggio 6 cm
raggio_17 = 6
pi_17 = 3.14159
volume_sfera_17 = (4/3) * pi_17 * (raggio_17**3)

# Esercizio 18: Determina se un numero è divisibile sia per 6 che per 8
numero_18 = 144
divisibile_6_e_8 = (numero_18 % 6 == 0) and (numero_18 % 8 == 0)

# Esercizio 19: Calcola la diagonale di un rettangolo con dimensioni 9x12
lunghezza_19 = 12
larghezza_19 = 9
diagonale_19 = (lunghezza_19**2 + larghezza_19**2) ** 0.5

# Esercizio 20: Calcola quanti chilometri percorre la Terra intorno al Sole in un giorno
distanza_sole_20 = 150000000
giorni_anno_20 = 365.25
circonferenza_orbita_20 = 2 * 3.14159 * distanza_sole_20
km_al_giorno_20 = circonferenza_orbita_20 / giorni_anno_20