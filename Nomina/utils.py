
from datetime import date

def PeriodoCarga():
    # período ventana de carga del 1 al 10 de cada mes
    p = True
    if date.today().day > 10:
        p = False     
    p = True
    return p

def IdEmpresaActiva():
    id_empresa = 1 # ver cómo levantar el id de la empresa a la cual pertenece el usuario logueado
    return id_empresa