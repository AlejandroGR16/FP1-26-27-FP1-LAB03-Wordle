from wordle_utils import es_palabra_valida, calcula_minutos_y_segundos, es_palabra_valida, marcar_amarillos, marcar_verdes, obtener_pistas, quitar_letras
import datetime

def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True

def test_calcula_minutos_y_segundos():
    assert calcula_minutos_y_segundos(datetime.datetime(2024, 1, 1, 23, 0, 0), datetime.datetime(2024, 1, 1, 23, 0, 30)) == (0, 30)
    assert calcula_minutos_y_segundos(datetime.datetime(2024, 1, 1, 23, 0, 0), datetime.datetime(2024, 1, 1, 23, 3, 45)) == (3, 45)
    assert calcula_minutos_y_segundos(datetime.datetime(2024, 1, 1, 23, 0, 0), datetime.datetime(2024, 1, 2, 0, 1, 15)) == (61, 15)

def test_quitar_letras():
    assert quitar_letras("casar", "a") == "csar"
    assert quitar_letras("casar", "c") == "asar"
    assert quitar_letras("casar", "r") == "casa"
    assert quitar_letras("casar", "z") == "casar"
    assert quitar_letras("aaaaa", "a") == "aaaa"

def test_marcar_verdes():
    assert marcar_verdes("casar", "polio") == ("_____", "casar")
    assert marcar_verdes("casar", "casar") == ("VVVVV", "")
    assert marcar_verdes("casar", "cazar") == ("VV_VV", "s")
    assert marcar_verdes("casar", "secta") == ("_____", "casar")
    assert marcar_verdes("casar", "sacar") == ("_V_VV", "cs")
    assert marcar_verdes("casar", "peras") == ("___V_", "csar")

def test_marcar_amarillos():
    assert marcar_amarillos("polio", "_____", "casar") == "_____"
    assert marcar_amarillos("casar", "VVVVV", "") == "VVVVV"
    assert marcar_amarillos("cazar", "VV_VV", "s") == "VV_VV"
    assert marcar_amarillos("secta", "_____", "casar") == "A_A_A"
    assert marcar_amarillos("sacar", "_V_VV", "cs") == "AVAVV"
    assert marcar_amarillos("peras", "___V_", "csar") == "__AVA"

def test_obtener_pistas():
    assert obtener_pistas("casar", "polio") == "_____"
    assert obtener_pistas("casar", "casar") == "VVVVV"
    assert obtener_pistas("casar", "cazar") == "VV_VV"
    assert obtener_pistas("casar", "secta") == "A_A_A"
    assert obtener_pistas("casar", "sacar") == "AVAVV"
    assert obtener_pistas("casar", "peras") == "__AVA"

test_es_palabra_valida()
print("✅Todas las pruebas pasaron correctamente.")