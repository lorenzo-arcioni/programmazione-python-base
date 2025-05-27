import sys
import io
import contextlib
import importlib
import math

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

def check(name, expected_type, expected_value=Ellipsis, tolerance=1e-9):
    try:
        assert hasattr(user, name), f"❌ La variabile '{name}' non è definita"
        val = getattr(user, name)
        assert isinstance(val, expected_type), f"❌ '{name}' dovrebbe essere di tipo {expected_type.__name__}, ma è {type(val).__name__}"
        if expected_value is not Ellipsis:
            if isinstance(expected_value, float):
                assert abs(val - expected_value) < tolerance, f"❌ '{name}' dovrebbe avere valore {expected_value}, ma ha {val}"
            else:
                assert val == expected_value, f"❌ '{name}' dovrebbe avere valore {expected_value}, ma ha {val}"
        print(f"{name:<30} {GREEN}[OK]{RESET}")
    except AssertionError as e:
        print(f"{name:<30} {CROSS} {e}")
        sys.exit(1)

# Test esercizi 1–10
check('media_geometrica', float, 5.656854249492381)
check('palindromo', bool, True)
check('ipotenusa', float, 25.0)
check('prima_cifra', int, 6)
check('seconda_cifra', int, 7)
check('terza_cifra', int, 4)
check('quarta_cifra', int, 8)
check('quinta_cifra', int, 9)
check('secondi_totali', int, 192645)
check('confronto', bool, False)
check('area_trapezio', float, 50.0)
check('risultato_espressione', float, 4.4)
check('resto_potenza', int, 2)
check('ore_intere', int, 5)
check('minuti_da_decimali', int, 45)
check('secondi_da_decimali', int, 0)

# Test esercizi 11–20
check('capitale_11', int, 2500)
check('tasso_11', float, 4.5)
check('tempo_11', float, 2.5)
check('interesse_11', float, 281.25)
check('montante_11', float, 2781.25)

check('diametro_12', int, 32)
check('lato_quadratino_12', int, 4)
check('area_pizza_12', float, 804.24704, 1e-4)
check('area_quadratino_12', int, 16)
check('quadratini_12', int, 50)

check('g_13', float, 9.81)
check('altezza_13', int, 45)
check('velocita_finale_13', float, 29.71363323459452, 1e-5)

check('fahrenheit_14', int, 86)
check('celsius_14', float, 30.0)
check('kelvin_14', float, 303.15)

check('numero_15', int, 6274)
check('numero_invertito_15', int, 4726)

check('prezzo_originale_16', int, 180)
check('prezzo_scontato_16', int, 135)
check('percentuale_sconto_16', float, 25.0)

check('raggio_17', int, 6)
check('pi_17', float, 3.14159)
check('volume_sfera_17', float, 904.7779199999999, 1e-5)

check('numero_18', int, 144)
check('divisibile_6_e_8', bool, True)

check('lunghezza_19', int, 12)
check('larghezza_19', int, 9)
check('diagonale_19', float, 15.0)

check('distanza_sole_20', int, 150000000)
check('giorni_anno_20', float, 365.25)
check('circonferenza_orbita_20', float, 942477000.0, 1e-3)
check('km_al_giorno_20', float, 2580361.3963039014, 1e-2)

print(f"\n{GREEN}✅ Tutti i test superati. Ottimo lavoro con le operazioni matematiche avanzate!{RESET}")
