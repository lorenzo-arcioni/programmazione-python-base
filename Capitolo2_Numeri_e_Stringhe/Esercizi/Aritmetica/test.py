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
check('media', float, 6.666666666666667)
check('divisibile', bool, True)
check('e', int, 7)
check('f', int, 5)
check('decina', int, 7)
check('due_euro', int, 3)
check('uno_euro', int, 1)
check('somma_pari', bool, True)
check('area', float, 12.0)
check('risultato', int, 20)
check('doppio_negativo', int, -5)
check('doppio_positivo', int, -5)
check('binario', str, '0b11111111')
check('ottale', str, '0o377')
check('esadecimale', str, '0xff')

# Test esercizi 11–20
check('prezzo_iniziale_11', int, 120)
check('sconto_11', float, 18.0)
check('prezzo_finale_11', float, 102.0)

check('conto_12', int, 97)
check('amici_12', int, 4)
check('quota_12', int, 24)
check('avanzo_12', int, 1)

check('minuti_totali_13', int, 367)
check('ore_13', int, 6)
check('minuti_13', int, 7)

check('dimensione_file_14', int, 1500)
check('velocita_14', float, 2.5)
check('secondi_14', int, 600)
check('minuti_14', int, 10)
check('resto_secondi_14', int, 0)

check('numero_15', int, 48319)
check('cifra_centrale_15', int, 3)

check('iniziali_16', int, 1200)
check('finali_16', int, 1380)
check('crescita_percentuale_16', float, 15.0)

check('costo_annuo_17', int, 299)
check('rata_mensile_17', float, 24.92)

check('anno_18', int, 2024)
check('bisestile_18', bool, True)

check('x_19', int, 6)
check('y_19', int, 8)
check('distanza_19', float, 10.0)

check('secondi_totali_20', int, 7384)
check('ore_20', int, 2)
check('minuti_20', int, 3)
check('secondi_20', int, 4)

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")
