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
check('nome_completo', str, "Marco Rossi")
check('ripetuta', str, "ciaociaociaociaociao")
check('lunghezza', int, 19)
check('primo', str, "p")
check('ultimo', str, "e")
check('sottostringa', str, "cdef")
check('invertita', str, "nohtyp")
check('maiuscolo', str, "CIAO MONDO")
check('minuscolo', str, "ciao mondo")
check('solo_lettere', bool, True)
check('sostituita', str, "le cese sulle colline")
check('parole', list, ["Python", "è", "un", "linguaggio", "potente"])

# Test esercizi 11–20
check('testo_originale_11', str, "   Python è potente   ")
check('testo_pulito_11', str, "Python è potente")

check('frase_12', str, "La programmazione è fantastica")
check('conta_a_12', int, 6)

check('linguaggio_13', str, "Python")
check('inizia_py_13', bool, True)
check('finisce_on_13', bool, True)

check('testo_14', str, "abcdefghij")
check('ogni_secondo_14', str, "acegi")

check('frase_15', str, "ciao mondo python")
check('capitalizzata_15', str, "Ciao Mondo Python")

check('testo_16', str, "La programmazione è divertente")
check('posizione_pro_16', int, 3)

check('frase_17', str, "Artificial Intelligence")
check('acronimo_17', str, "AI")

check('parola_18', str, "Anna")
check('palindromo_18', bool, True)

check('nome_19', str, "Marco")
check('eta_19', int, 25)
check('frase_formattata_19', str, "Mi chiamo Marco e ho 25 anni")

check('codice_fiscale_20', str, "RSSMRC85M15F205X")
check('cognome_cf_20', str, "RSS")
check('nome_cf_20', str, "MRC")
check('anno_nascita_20', int, 85)

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")