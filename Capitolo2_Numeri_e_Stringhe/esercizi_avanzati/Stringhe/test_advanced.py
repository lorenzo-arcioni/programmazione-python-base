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
    user_module = 'solutions_advanced' if '-s' in sys.argv else 'main_advanced'
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
check('email', str, "marco.rossi@università.it")
check('dominio', str, "università.it")

check('telefono', str, "+39-123 456.789")
check('telefono_pulito', str, "39123456789")

check('percorso', str, "/home/user/documento.pdf")
check('estensione', str, "pdf")

check('snake_case', str, "hello_world_python")
check('kebab_case', str, "hello-world-python")

check('nome_completo', str, "Marco Antonio Rossi")
check('prime_due_parole', str, "Marco Antonio")

check('parola', str, "Programmazione")
check('senza_vocali', str, "Prgrmmzn")

check('url_github', str, "https://github.com/utente123/repository")
check('username', str, "utente123")

check('testo_sporco', str, "  Ciao!!!   Mondo???  ")
check('testo_pulito', str, "Ciao Mondo")

check('tel_internazionale', str, "+39 123 456 789")
check('codice_paese', str, "39")

check('data_italiana', str, "15/03/2024")
check('data_iso', str, "2024-03-15")

# Test esercizi 11–20
check('email_11', str, "nome.cognome@dominio.com")
check('parte_locale_11', str, "nome.cognome")

check('url_12', str, "http://www.esempio.com")
check('dominio_pulito_12', str, "esempio.com")

check('timestamp_13', str, "2024-03-15 14:30:25")
check('ora_13', str, "14:30:25")

check('parola_14', str, "password")
check('censurata_14', str, "pa****rd")

check('percorso_15', str, "/documenti/report.docx")
check('nome_file_15', str, "report")

check('coordinate_16', str, "45.4642,9.1900")
check('latitudine_16', str, "45.4642")
check('longitudine_16', str, "9.1900")

check('user_agent_17', str, "Mozilla/5.0 (Windows NT 10.0)")
check('versione_17', str, "10.0")

check('hashtag_18', str, "#PythonProgramming")
check('testo_normale_18', str, "Python Programming")

check('url_completo_19', str, "https://www.esempio.com/pagina")
check('protocollo_19', str, "https")

check('cf_sporco_20', str, "rssmrc 85m15 f205x")
check('cf_pulito_20', str, "RSSMRC85M15F205X")

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")
