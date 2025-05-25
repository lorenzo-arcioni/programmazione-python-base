import sys
import io
import contextlib
import importlib

# ANSI escape codes per il colore verde
GREEN = '\033[92m'
RESET = '\033[0m'
CROSS = '\u274C'

# Nasconde temporaneamente stdout/stderr per l'import iniziale
@contextlib.contextmanager
def suppress_output():
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        yield

# 1) Importa il modulo senza mostrare eventuali print di setup
with suppress_output():
    if '-s' in sys.argv:
        user_module = 'solutions'
        mode = "SOLUZIONI"
    else:
        user_module = 'main'
        mode = "STUDENTE"
    user = importlib.import_module(user_module)

print(f"🔍 Modalità: {mode}")

# 2) Funzione di controllo per variabili
def check(name, expected_type, expected_value=Ellipsis):
    try:
        assert hasattr(user, name), f"❌ La variabile '{name}' non è definita"
        val = getattr(user, name)
        assert isinstance(val, expected_type), (
            f"❌ '{name}' dovrebbe essere di tipo {expected_type.__name__}, ma è {type(val).__name__}"
        )
        if expected_value is not Ellipsis:
            assert val == expected_value, (
                f"❌ '{name}' dovrebbe avere valore {expected_value}, ma ha {val}"
            )
        print(f"{name:<10} {GREEN}[OK]{RESET}")
    except AssertionError as e:
        print(f"{name:<10} {CROSS} {e}")
        sys.exit(1)

# 3) Controllo delle variabili
check('a', int, 42)
check('b', float, 3.14)
check('c', bool, True)
check('D', str, "ciao")
check('e', type(None), None)
check('f', complex, 2 + 3j)
check('g', bytes, b"hello")

# 4) Funzione per controllare l'output dei print
def check_output(expected_lines):
    buf = io.StringIO()
    # Catturiamo tutti i print del modulo ricaricato
    with contextlib.redirect_stdout(buf):
        importlib.reload(user)
    output = buf.getvalue().strip().splitlines()

    for expected in expected_lines:
        try:
            assert any(expected in line for line in output), f"❌ Output mancante: '{expected}'"
            print(f"print: '{expected}' {GREEN}[OK]{RESET}")
        except AssertionError as e:
            print(f"print      {CROSS} {e}")
            sys.exit(1)

# 5) Controllo dei print attesi
expected_prints = [
    "<class 'complex'>",              # da print(type(f))
    str(id(getattr(user, 'a'))),     # da print(id(a))
    "True",                           # da print(x == y)
    "False"                           # da print(x is y)
]
check_output(expected_prints)

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")