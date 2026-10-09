from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    if len(cadena)==5:
        for i in cadena:
            if not(i.isalpha()):
                return False
        return True
    return False

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    '''
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    '''
    return (((fin-inicio).seconds)//60,((fin-inicio).seconds)%60)

def quitar_letras(letras_restantes: str, letra: str):
    if letra in letras_restantes:
        letras_restantes=letras_restantes.replace(letra,'',1)
    return letras_restantes

def marcar_verdes(palabra_secreta: str,cadena: str,verdes='',restantes=''):
    restantes=palabra_secreta
    for i in range(0,5):
        if palabra_secreta[i]==cadena[i]:
            verdes+='V'
            restantes=restantes.replace(palabra_secreta[i],'',1)
        else: verdes+='_'
    return (verdes,restantes)

def marcar_amarillos(intento: str,verdes: str, restantes: str, colores=''):
    for i in range(0,5):
        if verdes[i]=='V':
            colores+='V'
        elif intento[i] in restantes:
            colores+='A'
            restantes=restantes.replace(intento[i],'',1)
        else:
            colores+='_'
    return colores

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    '''
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    '''
    return marcar_amarillos(intento,marcar_verdes(palabra_secreta,intento)[0],marcar_verdes(palabra_secreta,intento)[1])