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

def check_dict_has_key(dict_name, key, expected_value=Ellipsis):
    try:
        assert hasattr(user, dict_name), f"❌ Il dizionario '{dict_name}' non è definito"
        dict_val = getattr(user, dict_name)
        assert isinstance(dict_val, dict), f"❌ '{dict_name}' dovrebbe essere un dizionario"
        assert key in dict_val, f"❌ '{dict_name}' dovrebbe contenere la chiave '{key}'"
        if expected_value is not Ellipsis:
            assert dict_val[key] == expected_value, f"❌ '{dict_name}[{key}]' dovrebbe avere valore {expected_value}, ma ha {dict_val[key]}"
        test_name = f'{dict_name}["{key}"]'
        print(f"{test_name:<25} {GREEN}[OK]{RESET}")
    except AssertionError as e:
        test_name = f'{dict_name}["{key}"]'
        print(f"{test_name:<25} {CROSS} {e}")
        sys.exit(1)

# Test esercizi 1–10
check('persona', dict)
check('nome_studente', str, "Marco")
check('voto_studente', int, 28)
check('prezzo_prodotto', float, 899.99)
check('sconto', int, 0)
check_dict_has_key('libro', 'pagine', 328)
check_dict_has_key('animale', 'età', 5)
check('porta', int, 8080)
check_dict_has_key('configurazione', 'porta', 8080)

# Verifica che "pere" sia stato rimosso da inventario
try:
    assert hasattr(user, 'inventario'), "❌ Il dizionario 'inventario' non è definito"
    inventario = getattr(user, 'inventario')
    assert "pere" not in inventario, "❌ 'pere' dovrebbe essere stato rimosso da inventario"
    print(f"{'inventario (no pere)':<25} {GREEN}[OK]{RESET}")
except AssertionError as e:
    print(f"{'inventario (no pere)':<25} {CROSS} {e}")
    sys.exit(1)

check('punteggio_bob', int, 87)
# Verifica che Bob sia stato rimosso da punteggi
try:
    assert hasattr(user, 'punteggi'), "❌ Il dizionario 'punteggi' non è definito"
    punteggi = getattr(user, 'punteggi')
    assert "Bob" not in punteggi, "❌ 'Bob' dovrebbe essere stato rimosso da punteggi"
    print(f"{'punteggi (no Bob)':<25} {GREEN}[OK]{RESET}")
except AssertionError as e:
    print(f"{'punteggi (no Bob)':<25} {CROSS} {e}")
    sys.exit(1)

check_dict_has_key('base_config', 'porta', 8080)
check_dict_has_key('base_config', 'debug', True)
check('dict_unito', dict, {"a": 1, "b": 2, "c": 3, "d": 4})

# Test esercizi 11–20
check('ha_pizza', bool, True)
check('ha_sushi', bool, False)
check('giorni', list, ["lunedì", "martedì", "mercoledì", "giovedì"])
check('tutti_prezzi', list, [1.50, 2.00, 1.20])
check('coppie_voti', list, [("matematica", 8), ("fisica", 7), ("informatica", 9)])
check('copia_dict', dict, {"x": 10, "y": 20, "z": 30})
check('colori_dict', dict, {"rosso": 0, "verde": 0, "blu": 0})
check('da_svuotare', dict, {})
check('insegnante_1A', str, "Prof. Rossi")
check('studenti_2B', int, 23)
check('dict_da_lista', dict, {"nome": "Luigi", "età": 25, "città": "Roma"})
check('ultimo_elemento', tuple, ("lampade", 75))

print(f"\n{GREEN}✅ Tutti i test superati.{RESET}")

# Test aggiuntivo per verificare che la copia sia indipendente
if hasattr(user, 'originale') and hasattr(user, 'copia_dict'):
    # Modifichiamo il dizionario originale per verificare l'indipendenza della copia
    user.originale["w"] = 999
    if user.copia_dict == {"x": 10, "y": 20, "z": 30}:
        print(f"{'Copia indipendente':<25} {GREEN}[OK]{RESET}")
    else:
        print(f"{'Copia indipendente':<25} {CROSS} La copia non è indipendente dall'originale")
        sys.exit(1)

# Test aggiuntivo per verificare che magazzino abbia un elemento in meno
if hasattr(user, 'magazzino'):
    magazzino = getattr(user, 'magazzino')
    if len(magazzino) == 2:
        print(f"{'magazzino dopo popitem':<25} {GREEN}[OK]{RESET}")
    else:
        print(f"{'magazzino dopo popitem':<25} {CROSS} Il magazzino dovrebbe avere 2 elementi dopo popitem()")
        sys.exit(1)
