import sys
import io
import contextlib
import importlib
import copy

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
CROSS = '\u274C'

@contextlib.contextmanager
def suppress_output():
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        yield

with suppress_output():
    user_module = 'solutions' if '-s' in sys.argv else 'main'
    user = importlib.import_module(user_module)

print(f"🔍 Modalità: {'SOLUZIONI' if '-s' in sys.argv else 'STUDENTE'}")

# Contatore per tenere traccia dei test falliti
failed_tests = 0
total_tests = 0

def check(name, expected_type, expected_value=Ellipsis):
    global failed_tests, total_tests
    total_tests += 1
    
    try:
        assert hasattr(user, name), f"❌ La variabile '{name}' non è definita"
        val = getattr(user, name)
        assert isinstance(val, expected_type), f"❌ '{name}' dovrebbe essere di tipo {expected_type.__name__}, ma è {type(val).__name__}"
        if expected_value is not Ellipsis:
            assert val == expected_value, f"❌ '{name}' dovrebbe avere valore {expected_value}, ma ha {val}"
        print(f"{name:<30} {GREEN}[OK]{RESET}")
    except AssertionError as e:
        failed_tests += 1
        print(f"{name:<30} {RED}{CROSS} {e}{RESET}")

# Test esercizi 1-5
check('matrice_originale', list, [[1, 2], [3, 4], [5, 6]])
check('copia_superficiale', list, [[1, 2], [3, 4], [5, 6]])
check('copia_profonda', list, [[1, 2], [3, 4], [5, 6]])

check('citta', list, ["Roma", "Milano", "Napoli", "Torino", "Bologna", "Bari"])
check('citta_ordinate', list, ["Bari", "Bologna", "Milano", "Napoli", "Roma", "Torino"])

check('numeri_da_ordinare', list, [85, 92, 78, 88, 65, 91])
check('numeri_decrescenti_1', list, [92, 91, 88, 85, 78, 65])

check('numeri_sorted', list, [1, 2, 3, 5, 8, 9])
check('numeri_originali', list, [1, 2, 3, 5, 8, 9])

check('lista_concatenata', list, [1, 2, 3, 4, 5, 6])

# Test esercizi 6-10
check('base_append', list, [1, 2, [3, 4, 5]])
check('base_extend', list, [1, 2, 3, 4, 5])

check('pattern_ripetuto', list, ["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"])

check('primo_indice_banana', int, 1)
check('conta_banana', int, 3)
check('ha_kiwi', bool, False)

check('elemento_centrale', int, 5)
check('seconda_riga', list, [4, 5, 6])

check('caratteri', list, ['P', 'y', 't', 'h', 'o', 'n'])
check('parola_ricostruita', str, "Python")

# Test esercizi 11-15
check('lunghezza_dopo_clear', int, 0)

check('elementi_pari', list, [0, 2, 4, 6, 8])
check('elementi_centrali', list, [2, 3, 4, 5, 6, 7])
check('lista_invertita', list, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
check('ogni_terzo', list, [1, 4, 7])

check('lista_master', list, [1, 2, 3, 4])
check('lista_riferimento', list, [1, 2, 3, 4])
check('lista_copia', list, [1, 2, 3])

check('compiti', list, ["studiare", "fare_sport", "dormire"])
check('elemento_rimosso', str, "mangiare")

check('righe', list, [[0, 0, 0, 0], [0, 0, 99, 0], [0, 0, 0, 0]])

# Test esercizi 16-20
check('numeri_reverse', list, [6, 2, 9, 5, 1, 4, 1, 3])
check('numeri_decrescenti_2', list, [9, 6, 5, 4, 3, 2, 1, 1])

check('parole', list, ["Python", "linguaggio", "potente"])
check('numero_parole', int, 3)

check('prezzo_presente', bool, True)
check('indice_prezzo', int, 1)

check('e_vuota_1', bool, True)
check('e_vuota_2', bool, False)
check('e_vuota_3', bool, True)
check('e_vuota_4', bool, False)

check('backup_dati', list, [["user1", ["nuova_password", "email1"]], ["user2", ["password2", "email2"]]])

# Riepilogo dei test base
print(f"\n📊 Riepilogo test base:")
print(f"Test completati: {total_tests}")
print(f"Test superati: {total_tests - failed_tests}")
print(f"Test falliti: {failed_tests}")

if failed_tests == 0:
    print(f"\n{GREEN}✅ Tutti i test base superati!{RESET}")
else:
    print(f"\n{RED}❌ {failed_tests} test falliti{RESET}")

# Test avanzati per verificare comportamenti specifici
print("\n🔬 Test avanzati:")

advanced_failed = 0
advanced_total = 0

def advanced_check(description, condition, error_msg):
    global advanced_failed, advanced_total
    advanced_total += 1
    
    if condition:
        print(f"{description:<30} {GREEN}[OK]{RESET}")
    else:
        advanced_failed += 1
        print(f"{description:<30} {RED}{CROSS} {error_msg}{RESET}")

# Verifica indipendenza copia superficiale vs profonda
if hasattr(user, 'copia_superficiale') and hasattr(user, 'matrice_originale'):
    user.matrice_originale[0][0] = 999
    advanced_check(
        "Copia superficiale condivisa",
        user.copia_superficiale[0][0] == 999,
        "La copia superficiale dovrebbe condividere i riferimenti interni"
    )
else:
    advanced_failed += 1
    advanced_total += 1
    print(f"{'Copia superficiale condivisa':<30} {RED}{CROSS} Variabili necessarie non trovate{RESET}")

# Test copia profonda
if hasattr(user, 'copia_profonda'):
    advanced_check(
        "Copia profonda indipendente",
        user.copia_profonda[0][0] == 1,
        "La copia profonda dovrebbe essere completamente indipendente"
    )
else:
    advanced_failed += 1
    advanced_total += 1
    print(f"{'Copia profonda indipendente':<30} {RED}{CROSS} Variabile copia_profonda non trovata{RESET}")

# Test riferimenti condivisi
if hasattr(user, 'lista_riferimento') and hasattr(user, 'lista_master'):
    advanced_check(
        "Riferimento condiviso",
        user.lista_riferimento is user.lista_master,
        "lista_riferimento dovrebbe puntare allo stesso oggetto"
    )
else:
    advanced_failed += 1
    advanced_total += 1
    print(f"{'Riferimento condiviso':<30} {RED}{CROSS} Variabili necessarie non trovate{RESET}")

if hasattr(user, 'lista_copia') and hasattr(user, 'lista_master'):
    advanced_check(
        "Copia indipendente",
        user.lista_copia is not user.lista_master,
        "lista_copia dovrebbe essere un oggetto diverso"
    )
else:
    advanced_failed += 1
    advanced_total += 1
    print(f"{'Copia indipendente':<30} {RED}{CROSS} Variabili necessarie non trovate{RESET}")

# Verifica che l'originale dei dati sensibili non sia stato modificato
if hasattr(user, 'dati_sensibili'):
    advanced_check(
        "Originale non modificato",
        user.dati_sensibili[0][1][0] == "password1",
        "L'originale non dovrebbe essere stato modificato"
    )
else:
    advanced_failed += 1
    advanced_total += 1
    print(f"{'Originale non modificato':<30} {RED}{CROSS} Variabile dati_sensibili non trovata{RESET}")

# Riepilogo finale
print(f"\n📊 Riepilogo finale:")
print(f"Test base: {total_tests - failed_tests}/{total_tests}")
print(f"Test avanzati: {advanced_total - advanced_failed}/{advanced_total}")
print(f"Totale: {(total_tests + advanced_total) - (failed_tests + advanced_failed)}/{total_tests + advanced_total}")

if failed_tests + advanced_failed == 0:
    print(f"\n{GREEN}🎉 Tutti i test superati con successo!{RESET}")
    sys.exit(0)
else:
    print(f"\n{RED}⚠️  Alcuni test non sono stati superati. Controlla i dettagli sopra.{RESET}")
    sys.exit(1)