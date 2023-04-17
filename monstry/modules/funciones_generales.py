import re
from datetime import datetime

def validador_variables(cb):
    def wrapper(variable):
        regexp = '(-|\.|\+54)'
        
        if type(variable) != 'str':
            try:
                variable = str(variable)
            except:
                return TypeError

        if re.search(regexp,variable):
            variable = re.sub(regexp,'',variable)
            return cb(variable)

        return cb(variable)

    return wrapper


def validador_var(variable):
    regexp = '(-|\.|\+54)'
    
    variable = str(variable)

    if re.search(regexp,variable):
        variable = re.sub(regexp,'',variable)
        return variable

    return variable


def comprobando_uuid(variable):
    """
        Valida  Unique ID
    """    
    regexp = '.{36}'

    try:
        return True if re.search(regexp, variable) else False
    except:
        return False

def comprobando_lat_long(variable):
    
    reg_exp = '^-?[0-9]\d*(\.\d+)?$'   
    try:
        if re.search(reg_exp,variable): return True
        else: return False
    except:
        return False


def comprobando_no_determinado(variable):
    reg_exp = '.+'   
    try:
        if re.search(reg_exp,variable): return True
        else: return False
    except:
        return False
    

def comprobando_alfanumerico(variable):
    variable = variable.strip()
    reg_exp = '\w*\d+'   
    try:
        if re.search(reg_exp,variable): return True
        else: return False
    except:
        return False
    

def comprobando_numeros_telefonicos(variable):
    if re.search('\.0+$',variable):
        variable = int(variable)

    reg_exp = "(^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$|\d{8,10})"
    try:
        if re.search(reg_exp,variable): return True
        else: return False
    except:
        return False


def comprobando_correo_valido(variable):
    variable = variable.strip()
    regexp = '^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$'
    try:
        return True if re.search(regexp,variable) else False
    except:
        return False

def comprobando_fecha_general(variable):
    variable = variable.strip()

    try:
        if datetime.strptime(variable, '%Y-%m-%d'):
            return True
    except:
        try:
            if datetime.strptime(variable, '%Y-%m-%d %H:%M:%S'): return True
        except:
            try:
                if datetime.strptime(variable, '%Y-%m-%d %H:%M:%S.%f'): return True
            except Exception as e:
                print(f'{e}\n{type(e)} : {type(e).__doc__}')
                return False


def comprobando_numeros(variable):
    """
    Valida numeros sin tener en cuenta la longitud de la misma
    """
    variable = variable.strip()
    reg_exp = "^[0-9]*$"
    if re.search(reg_exp, variable):
        return True
    else:
        return False



def comprobando_strings(variable):
    variable = variable.strip()
    reg_exp = "^[a-zA-ZÀ-ÿ\u00C0-\u017F]*$"

    return True if re.search(reg_exp, variable) else False


def comprobando_direcciones_completas(variable):    
    variable = variable.strip()
    reg_exp = "^[0-9a-zA-Z\u00C0-\u017F\s\.\d]*"
    return True if re.search(reg_exp, variable) else False
   

def comprobando_calles(variable):    
    variable = variable.strip()
    reg_exp = "^[a-zA-Z\u00C0-\u017F\s\.\d]*"
    
    return True if re.search(reg_exp, variable) else False


def comprobando_string_chars(variable):
    "Valida una o más palabras"
    variable = variable.strip()
    regexp = '^[a-zA-Z\u00C0-\u017F\s\/].*[a-zA-Z\u00C0-\u017F]$'
    
    return True if re.search(regexp,variable) else False

def comprobando_cp(variable):    
    variable = variable.strip()
    reg_exp = "^([a-zA-Z]{1}[0-9]{4}[a-zA-Z]{3}|[0-9]{4})$"
    
    return True if re.search(reg_exp, variable) else False

def comprobando_string_chars_especiales(variable):

    "Valida una o más palabras"
    variable = variable.strip()
    regexp = '^[0-9a-zA-Z\u00C0-\u017F\s\/\(\)].*[0-9a-zA-Z\u00C0-\u017F\(\)]$'
    
    return True if re.search(regexp,variable) else False

def comprobando_strings_numeros(variable):  
    variable = variable.strip()
    regexp = "^[0-9a-zA-Z\u00C0-\u017F\s\/].*[0-9a-zA-Z\u00C0-\u017F]$"
    return True if re.search(regexp,variable) else False


def comprobando_digitos_dni(variable):
    
    try:
        variable = int(variable.strip())
        variable = str(variable)

        reg_exp = "^[0-9]{7,8}$"
    
        return True if re.search(reg_exp, variable) else False
        
    except:
        return False


def comprobando_digitos_cuit_cuil(variable):
    try:
        variable = int(variable.strip())
        val = str(variable)
        reg_exp = "^[0-9]{2}[0-9]{8}[0-9]$"
            
        return True if re.search(reg_exp, val) else False
        
    except:
        return False
     
@validador_variables
def comprobando_telefonos(variable):
     
    try:
        variable = variable.strip()
        data = int(variable)
        data = str(data)
        reg_exp="^[0-9]{8,13}$"
        
        return True if re.search(reg_exp, data) else False
    except:
        return False


def comprobando_booleanos(variable):
    variable = variable.strip()
    if variable.isnumeric():
        variable = int(variable)
    boolean = [1,0,True,False]
    return variable in boolean 


def comprobando_genero(variable):
    variable = variable.strip()
    regexp = "(hombre|mujer|femenino|masculino|masc\.|fem\.|h|m|f)$"
    return True if re.search(regexp,variable,re.IGNORECASE) else False


def comprobando_carrera(variable):
    variable = variable.strip()
    regexp = "^[0-9a-zA-Z\u00C0-\u017F\s\/\(\)].*[0-9a-zA-Z\(\)]$"
    return True if re.search(regexp,variable,re.IGNORECASE) else False


def comprobando_nombres(variable):
    variable = variable.strip()
    regexp = '^([a-zñ\u00C0-\u017F]+ ?)*[a-zñ\u00C0-\u017F]+$'
    return True if re.search(regexp,variable,re.IGNORECASE) else False

def comprobando_letras_3_o_menos(variable):
    regexp = '^[\w]{1,3}$'
    return True if re.search(regexp,variable,re.IGNORECASE) else False

def letras_y_numeros(variable):
    regexp = '[A-Z0-9]+'
    return True if re.search(regexp,variable,re.IGNORECASE) else False

def comprobando_decimales(variable):
    try:
        float(variable)
        return True
    except:
        return False
    
