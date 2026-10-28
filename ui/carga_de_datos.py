import json

def cargar_json(ruta_archivo):
    """ Carga y retorna los datos json de la ruta especificada """
    with open(ruta_archivo) as f:
        datos = json.load(f)
    return datos






