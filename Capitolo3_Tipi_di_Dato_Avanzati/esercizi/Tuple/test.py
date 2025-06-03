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
check('tupla_mista', tuple, (42, "ciao", True, None))
check('primo_elemento', int, 10)
check('ultimo_elemento', int, 50)
check('secondo_da_fine', int, 40)
check('primi_tre', tuple, ('a', 'b', 'c'))
check('ultimi_due', tuple, ('f', 'g'))
check('elementi_pari', tuple, ('a', 'c', 'e', 'g'))
check('tupla_invertita', tuple, ('g', 'f', 'e', 'd', 'c', 'b', 'a'))
check('persona', tuple, ("Mario", 25, "Ingegnere"))
check('x', int, 10)
check('y', int, 20)
check('primo', int, 1)
check('mezzo', list, [2, 3, 4, 5])
check('ultimo', int, 6)
check('tupla_singola', tuple, (42,))
check('tupla_concatenata', tuple, (1, 2, 3, 4, 5, 6))
check('tupla_ripetuta', tuple, (0, 1, 0, 1, 0, 1))

# Test esercizi 11–20
check('ha_python', bool, True)
check('ha_ruby', bool, False)

check('conta_otto', int, 3)
check('conta_sette', int, 2)

check('indice_banana', int, 1)
check('indice_mela', int, 0)

check('numero_colori', int, 5)

check('numeri_lista', list, [1, 2, 3, 4, 5])
check('lettere_tupla', tuple, ('a', 'b', 'c', 'd'))

check('nome', str, "Mario")
check('anno_corso', tuple, (2000, "Informatica"))
check('anno', int, 2000)
check('corso', str, "Informatica")

check('punto_2d', tuple, (5, 10))
check('punto_3d', tuple, (1, 2, 3))

check('nome_18', str, "Alice")
check('cognome_18', str, "Bianchi")
check('anno_nascita', int, 1995)
check('citta', str, "Milano")
check('professione', str, "Ingegnere")
check('stipendio', int, 50000)

check('hash_numeri', int)

check('valore_diagonale', str, "diagonale")

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")

# Test aggiuntivi per verificare proprietà specifiche delle tuple

# Verifica che le tuple siano realmente immutabili
print(f"{'Test immutabilità':<25}", end=' ')
try:
    test_tupla = (1, 2, 3)
    test_tupla[0] = 999  # Questo dovrebbe generare un errore
    print(f"{CROSS} Le tuple dovrebbero essere immutabili!")
    sys.exit(1)
except TypeError:
    print(f"{GREEN}[OK]{RESET}")

# Verifica che la tupla con un elemento abbia effettivamente la virgola
print(f"{'Test tupla singola':<25}", end=' ')
if hasattr(user, 'tupla_singola'):
    if len(user.tupla_singola) == 1 and isinstance(user.tupla_singola, tuple):
        print(f"{GREEN}[OK]{RESET}")
    else:
        print(f"{CROSS} La tupla singola deve avere esattamente un elemento e essere di tipo tuple")
        sys.exit(1)

# Verifica che la tupla sia hashable
print(f"{'Test hashable':<25}", end=' ')
if hasattr(user, 'tupla_numeri'):
    try:
        hash(user.tupla_numeri)
        print(f"{GREEN}[OK]{RESET}")
    except TypeError:
        print(f"{CROSS} La tupla dovrebbe essere hashable")
        sys.exit(1)

# Verifica che la tupla con lista non sia hashable
print(f"{'Test non-hashable':<25}", end=' ')
if hasattr(user, 'tupla_con_lista'):
    try:
        hash(user.tupla_con_lista)
        print(f"{CROSS} La tupla contenente una lista NON dovrebbe essere hashable")
        sys.exit(1)
    except TypeError:
        print(f"{GREEN}[OK]{RESET}")

print(f"\n{GREEN}🎯 Tutti i test sulle tuple completati con successo!{RESET}")
