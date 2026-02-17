import time

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    inicio = time.time()
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    data = open("computer_prices_small.csv","r", encoding ="utf-8")
    titulos = data.readline()
    print (titulos)
    diccionario = {}
    line = data.readline()
    while len(line) > 0:
        datos = linea.strip().split(",") 
        diccionario_sec = {
            
        }
        linea = data.readline()
        device_type = datos[0]
        diccionario_sec["brand"] = datos[1]
        diccionario_sec["model"] = datos[2]
        diccionario_sec["release_year"] = datos[2]
        diccionario_sec["os"] = datos[4]
        diccionario_sec["form_factor"] = datos[5]
        diccionario_sec["operative_sistem"] = datos[6]
        diccionario_sec["form_factor"] = datos[7]
        diccionario_sec["cpu_brand"] = datos[8]
        diccionario_sec["cpu_model"] = datos[9]
        diccionario_sec["cpu_tier"] = datos[10]
        diccionario_sec["cpu_cores"] = datos[11]
        diccionario_sec["cpu_threads"] = datos[12]
        diccionario_sec["cpu_base_ghz"] = datos[13]
        diccionario_sec["cpu_boost_ghz"] = datos[14]
        diccionario_sec["gpu_brand"] = datos[14]
        diccionario_sec["gpu_tier"] = datos[15]
        diccionario_sec["vram_gb"] = datos[16]
        diccionario_sec["ram_gb"] = datos[17]
        diccionario_sec["storage_type"] = datos[18]
        diccionario_sec["storage_gb"] = datos[19]
        diccionario_sec["storage_drive_count"] = datos[20]
        diccionario_sec["display_type"] = datos[21]
        diccionario_sec["display_size"] = datos[22]
        diccionario_sec["resolution"] = datos[23]
        diccionario_sec["refresh_hz"] = datos[24]
        diccionario_sec["battery_wh"] = datos[25]
        diccionario_sec["charger_watts"] = datos[26]
        diccionario_sec["psu_watts"] = datos[27]
        diccionario_sec["wifi"] = datos[28]
        diccionario_sec["weight_kg"] = datos[30]
        diccionario_sec["warranty_months"] = datos[31]
        diccionario_sec["price"] = datos[32]
        if device_type not in diccionario:
            diccionario[device_type] = []
        diccionario[device_type].append(diccionario_sec)
        linea = data.readline()
    data.close()
    final = time.time()
    tiempo = final - inicio
    return diccionario, tiempo
        
# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pass

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
