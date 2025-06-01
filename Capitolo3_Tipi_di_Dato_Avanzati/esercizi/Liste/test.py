import sys
import io
import contextlib
import importlib

GREEN = '\033[92m'
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

def check(name, expected_type, expected_value=Ellipsis):
    try:
        assert hasattr(user, name), f"❌ La variabile '{name}' non è definita"
        val = getattr(user, name)
        assert isinstance(val, expected_type), f"❌ '{name}' dovrebbe essere di tipo {expected_type.__name__}, ma è {type(val).__name__}"
        if expected_value is not Ellipsis:
            assert val == expected_value, f"❌ '{name}' dovrebbe avere valore {expected_value}, ma ha {val}"
        print(f"{name:<25} {GREEN}[OK]{RESET}")
    except AssertionError as e:
        print(f"{name:<25} {CROSS} {e}")
        sys.exit(1)

# Test esercizi 1–10
check('lista_mista', list, [42, "ciao", True, None])
check('primo_elemento', int, 10)
check('ultimo_elemento', int, 50)
check('secondo_da_fine', int, 40)
check('primi_tre', list, ['a', 'b', 'c'])
check('ultimi_due', list, ['f', 'g'])
check('elementi_pari', list, ['a', 'c', 'e', 'g'])
check('lista_invertita', list, ['g', 'f', 'e', 'd', 'c', 'b', 'a'])
check('frutti', list, ["mela", "pera", "arancia"])
check('animali', list, ["cane", "gatto", "elefante"])
check('colori', list, ["rosso", "giallo", "verde", "blu"])
check('voti', list, [7, 6, 8, 9, 8])
check('lista_concatenata', list, [1, 2, 3, 4, 5, 6])
check('base', list, [1, 2, 3, 4, 5, 6])
check('lista_append', list, [1, 2, [3, 4]])
check('lista_extend', list, [1, 2, 3, 4])

# Test esercizi 11–20
check('pattern_11', list, [0, 1])
check('lista_ripetuta_11', list, [0, 1, 0, 1, 0, 1, 0, 1])

check('linguaggi_12', list, ["Python", "Java", "C++", "JavaScript"])
check('ha_python_12', bool, True)
check('ha_ruby_12', bool, False)

check('numeri_13', list, [1, 2, 5, 8, 9])

check('numeri_originali_14', list, [5, 2, 8, 1, 9])
check('numeri_ordinati_14', list, [1, 2, 5, 8, 9])

check('frutta_15', list, ["mela", "banana", "arancia", "banana"])
check('indice_banana_15', int, 1)

check('lettere_16', list, ['a', 'b', 'a', 'c', 'a', 'b'])
check('conta_a_16', int, 3)

check('lista_originale_17', list, [1, 2, 3, 4])
check('lista_copia_17', list, [1, 2, 3, 4])

check('parola_18', str, "Python")
check('caratteri_18', list, ['P', 'y', 't', 'h', 'o', 'n'])

check('da_svuotare_19', list, [])

check('matrice_20', list, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
check('elemento_centrale_20', int, 5)
check('prima_riga_20', list, [1, 2, 3])

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")

# Test aggiuntivo per verificare che la copia sia indipendente
if hasattr(user, 'lista_originale_17') and hasattr(user, 'lista_copia_17'):
    # Modifichiamo la lista originale per verificare l'indipendenza della copia
    user.lista_originale_17.append(999)
    if user.lista_copia_17 == [1, 2, 3, 4]:
        print(f"{'Copia indipendente':<25} {GREEN}[OK]{RESET}")
    else:
        print(f"{'Copia indipendente':<25} {CROSS} La copia non è indipendente dall'originale")
        sys.exit(1)