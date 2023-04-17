import re
import numpy
from .funciones_generales import * 

regexp_list = [
{   "data" :"string",
    "dtype": "object",
    "type" : "str",
    "regexp":"^[a-zA-Z\u00C0-\u017F\s]+$",
    "default": comprobando_strings,
    
},
{
    "data" : "bool",
    "dtype": "bool",
    "type" : "bool",
    "regexp":"^(1|0|True|False)$",
    "default" : comprobando_booleanos
}
,

{   "data" : "number",
    "dtype": "int64",
    "type" : "int",
    "regexp":"^[0-9]+$",
    "default" : comprobando_numeros
},
{
    "data" : "alpha_numeric",
    "dtype": "object",
    "type" : "str",
    "regexp":"^\w+$",
    "default" : comprobando_alfanumerico
},
{
    "data" : "email",
    "dtype": "object",
    "type" : "str",
    "regexp" : "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
    "default" : comprobando_correo_valido
},
{
    "data" : "decimal",
    "dtype": "float64",
    "type" : "float",
    "regexp" : "^\d+[\.|\,]?\d*$",
    "default" : comprobando_decimales
},
{
    "data" : "uuid",
    "dtype": "object",
    "type" : "str",
    "regexp" : "^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$",
    "default" : comprobando_uuid
},
{
    "data" : "fechas",
    "dtype": "datetime64",
    "type" : "str",
    "regexp" : '^(\d){4}([-|\/|.](\d){2}){2}(|\s(\d){2}(:(\d){2}){2}|\s(\d){2}(:(\d){2}){2}(|.\d{1,5}))$',
    "default" : comprobando_fecha_general
},

{
    "data" : "alpha_numeric_text",
    "dtype": "object",
    "type" : "str",
    "regexp":"^[\w\s]+$" ,
    "default" : comprobando_alfanumerico
},
{
    "data" : "no_determinado",
    "dtype": "object",
    "type" : "str",
    "regexp":".*" ,
    "default" : comprobando_no_determinado
}
]


def matcher_regexp(regexp_list , sample, columna):
    try:
        res_data = None

        for checker in regexp_list:

            res = re.match(checker['regexp'],sample)
            if res is not None:          
                if res_data is None:
                    res_data = {**checker,**{"columna":columna,"sample":sample}}
                    break
        
        if res_data is None:
            res_data = {
                "data" : "uknown",
                "dtype": "object",
                "type" : "str",
                "regexp" :".+",
                "columna":columna,
                "sample":sample
                }
        
        del res_data['regexp']

        return res_data

    except Exception as e:
        print(e)
        return {
            "error" : e,
            "sample":sample
        }



def request_not_na_value(dataframe):
    dataframe =  dataframe.dropna(how='all',axis=0,inplace=False)

    dataframe = dataframe.astype('str')

    if len(dataframe) == 0 :
        print('El dataframe no contiene registros para analizar')
        return ''

    sample = dataframe.sample(n=1)

    [validador,*extra] = sample.isna().to_numpy()


    while validador:
        sample = dataframe.sample(n=1)

    [sample_return, *extra]  = sample.to_numpy()

    return str(sample_return)

def chequeo_valores(dataframe):

    if dataframe is None:
        print('No hay un dataframe válido')
        return

    
    columnas = dataframe.columns
    columnas_lista = []

    for index,col in enumerate(columnas):

        sample = request_not_na_value(dataframe[col])

        columnas_lista.append(matcher_regexp(regexp_list, sample, col))
    

    return columnas_lista

