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
        print(f"{name:<20} {GREEN}[OK]{RESET}")
    except AssertionError as e:
        print(f"{name:<20} {CROSS} {e}")
        sys.exit(1)

# Test esercizi 21–30
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

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")
