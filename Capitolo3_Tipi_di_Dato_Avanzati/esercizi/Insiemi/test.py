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
check('set_misto', set, {42, "ciao", True, None})
check('numeri_unici', set, {10, 20, 30, 40})
check('caratteri_unici', set, {'p', 'r', 'o', 'g', 'a', 'm', 'z', 'i', 'n', 'e'})
check('frutti', set, {"mela", "banana", "arancia"})
check('colori', set, {"rosso", "blu", "giallo"})
check('voti', set, {7, 6, 9})
check('ha_python', bool, True)
check('ha_ruby', bool, False)
check('set_unione', set, {1, 2, 3, 4, 5})
check('mammiferi_domestici', set, {"cane", "gatto"})
check('numeri_dispari', set, {1, 3, 5})

# Test esercizi 11–20
check('solo_una_materia', set, {"Alice", "Charlie", "Eve", "Frank"})
check('base_set', set, {1, 2, 3, 4, 5, 6})
check('originale', set, {"a", "b", "c"})
check('copia_set', set, {"a", "b", "c"})
check('sono_uguali', bool, True)
check('e_sottoinsieme', bool, True)
check('e_sovrainsieme', bool, True)
check('sono_disgiunti', bool, True)
check('da_svuotare', set, set())
check('frozen_numeri', frozenset, frozenset({10, 20, 30}))
check('numero_vocali', int, 5)

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")

# Test aggiuntivo per verificare che la copia sia indipendente
if hasattr(user, 'originale') and hasattr(user, 'copia_set'):
    # Modifichiamo il set originale per verificare l'indipendenza della copia
    user.originale.add("nuovo")
    if user.copia_set == {"a", "b", "c"}:
        print(f"{'Copia indipendente':<25} {GREEN}[OK]{RESET}")
    else:
        print(f"{'Copia indipendente':<25} {CROSS} La copia non è indipendente dall'originale")
        sys.exit(1)

# Test aggiuntivo per verificare che discard non sollevi eccezioni
try:
    test_set = {1, 2, 3}
    test_set.discard(10)  # elemento non presente
    print(f"{'Discard sicuro':<25} {GREEN}[OK]{RESET}")
except:
    print(f"{'Discard sicuro':<25} {CROSS} discard() dovrebbe essere sicuro anche con elementi non presenti")
    sys.exit(1)