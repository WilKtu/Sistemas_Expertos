import json

# ================================================================
# SISTEMA EXPERTO: Diagnóstico de PC
# ================================================================

# ================================================================
# BASE DE CONOCIMIENTO
# ================================================================

base_de_conocimiento = [
    {
        "id": "R01",
        "descripcion": "Fuente de poder dañada o problema de energía",
        "condiciones": ["no_enciende", "sin_luces", "sin_sonido"],
        "causas": [
            "fuente_de_poder_danada",
            "cable_desconectado",
            "bateria_defectuosa"
        ],
        "confianza": 0.92
    },
    {
        "id": "R02",
        "descripcion": "Falla de memoria RAM",
        "condiciones": [
            "enciende",
            "pitidos_arranque",
            "sin_video"
        ],
        "causas": [
            "ram_mal_instalada",
            "modulo_ram_defectuoso",
            "suciedad_contactos",
            "incompatibilidad_ram"
        ],
        "confianza": 0.88
    },
    {
        "id": "R03",
        "descripcion": "Falla de video o pantalla negra",
        "condiciones": [
            "enciende",
            "pantalla_negra",
            "sin_pitidos"
        ],
        "causas": [
            "tarjeta_video_danada",
            "monitor_defectuoso",
            "cable_video_defectuoso",
            "sistema_operativo_corrupto"
        ],
        "confianza": 0.82
    },
    {
        "id": "R04",
        "descripcion": "Problemas de almacenamiento o lentitud por disco",
        "condiciones": [
            "enciende",
            "inicia_lento",
            "disco_al_100"
        ],
        "causas": [
            "disco_duro_danado",
            "poco_espacio_disco",
            "sectores_danados"
        ],
        "confianza": 0.85
    },
    {
        "id": "R05",
        "descripcion": "Infección por malware o virus",
        "condiciones": [
            "enciende",
            "inicia_lento",
            "ventilador_siempre_activo"
        ],
        "causas": [
            "malware",
            "virus",
            "archivos_maliciosos",
            "antivirus_desactualizado"
        ],
        "confianza": 0.80
    },
    {
        "id": "R06",
        "descripcion": "Pantalla azul (BSOD)",
        "condiciones": [
            "enciende",
            "pantalla_azul_frecuente"
        ],
        "causas": [
            "drivers_defectuosos",
            "errores_hardware",
            "archivos_sistema_danados",
            "ram_defectuosa"
        ],
        "confianza": 0.87
    },
    {
        "id": "R07",
        "descripcion": "Sobrecalentamiento",
        "condiciones": [
            "enciende",
            "se_apaga_solo",
            "calor_excesivo"
        ],
        "causas": [
            "ventiladores_sucios",
            "pasta_termica_seca",
            "mala_ventilacion"
        ],
        "confianza": 0.90
    },
    {
        "id": "R08",
        "descripcion": "Reinicios inesperados",
        "condiciones": [
            "reinicios_inesperados"
        ],
        "causas": [
            "sobrecalentamiento",
            "fuente_inestable",
            "virus"
        ],
        "confianza": 0.84
    },
    {
        "id": "R09",
        "descripcion": "Disco duro no detectado",
        "condiciones": [
            "disco_no_detectado"
        ],
        "causas": [
            "conexion_suelta",
            "disco_duro_averiado"
        ],
        "confianza": 0.89
    },
    {
        "id": "R10",
        "descripcion": "Ruidos extraños en disco duro",
        "condiciones": [
            "ruidos_disco"
        ],
        "causas": [
            "desgaste_mecanico",
            "sectores_danados"
        ],
        "confianza": 0.91
    },
    {
        "id": "R11",
        "descripcion": "Teclado no responde",
        "condiciones": [
            "teclado_no_funciona"
        ],
        "causas": [
            "driver_incorrecto",
            "suciedad",
            "dano_fisico"
        ],
        "confianza": 0.83
    },
    {
        "id": "R12",
        "descripcion": "Mouse no funciona",
        "condiciones": [
            "mouse_no_funciona"
        ],
        "causas": [
            "usb_defectuoso",
            "bateria_agotada",
            "driver_danado"
        ],
        "confianza": 0.82
    },
    {
        "id": "R13",
        "descripcion": "Sin conexión a Internet",
        "condiciones": [
            "sin_internet"
        ],
        "causas": [
            "problema_red",
            "driver_red_danado",
            "configuracion_incorrecta"
        ],
        "confianza": 0.86
    },
    {
        "id": "R14",
        "descripcion": "Impresora no imprime",
        "condiciones": [
            "impresora_no_imprime"
        ],
        "causas": [
            "sin_tinta",
            "driver_incorrecto",
            "conexion_defectuosa"
        ],
        "confianza": 0.81
    },
    {
        "id": "R15",
        "descripcion": "USB no reconoce dispositivos",
        "condiciones": [
            "usb_no_reconoce"
        ],
        "causas": [
            "puerto_danado",
            "driver_ausente",
            "dispositivo_defectuoso"
        ],
        "confianza": 0.84
    },
    {
        "id": "R16",
        "descripcion": "Sistema operativo no inicia",
        "condiciones": [
            "so_no_inicia"
        ],
        "causas": [
            "archivos_arranque_danados",
            "errores_disco"
        ],
        "confianza": 0.88
    },
    {
        "id": "R17",
        "descripcion": "Aplicaciones se cierran inesperadamente",
        "condiciones": [
            "apps_se_cierran"
        ],
        "causas": [
            "falta_memoria",
            "error_programa",
            "incompatibilidad"
        ],
        "confianza": 0.79
    },
    {
        "id": "R18",
        "descripcion": "Problemas de audio",
        "condiciones": [
            "sin_sonido"
        ],
        "causas": [
            "altavoces_desconectados",
            "driver_audio_danado",
            "configuracion_incorrecta"
            ],
        "confianza": 0.85
    },
    {
        "id": "R19",
        "descripcion": "Pantalla con líneas o parpadeo",
        "condiciones": [
            "pantalla_parpadea",
            "lineas_en_pantalla"
        ],
        "causas": [
            "cable_video_defectuoso",
            "monitor_danado",
            "gpu_defectuosa"
        ],
        "confianza": 0.87
    },
    {
        "id": "R20",
        "descripcion": "Batería se descarga rápidamente",
        "condiciones": [
            "bateria_descarga_rapida"
        ],
        "causas": [
            "bateria_desgastada",
            "alto_consumo_energia"
        ],
        "confianza": 0.83
    },
    {
        "id": "R21",
        "descripcion": "Fecha y hora incorrectas",
        "condiciones": [
            "fecha_hora_incorrecta"
        ],
        "causas": [
            "bateria_cmos_agotada"
        ],
        "conclusion": "Reemplazar batería CMOS",
        "confianza": 0.95
    },
    {
        "id": "R22",
        "descripcion": "Boot Device Not Found",
        "condiciones": [
            "boot_device_not_found"
        ],
        "causas": [
            "disco_danado",
            "bios_mal_configurada"
        ],
        "confianza": 0.91
    },
    {
        "id": "R23",
        "descripcion": "Puertos USB con alimentación insuficiente",
        "condiciones": [
            "usb_sin_energia"
        ],
        "causas": [
            "placa_madre_danada",
            "sobrecarga_electrica"
        ],
        "confianza": 0.82
    },
    {
        "id": "R24",
        "descripcion": "Congelamiento frecuente del sistema",
        "condiciones": [
            "sistema_congelado"
        ],
        "causas": [
            "ram_defectuosa",
            "sobrecalentamiento",
            "errores_sistema"
        ],
        "confianza": 0.88
    },
    {
        "id": "R25",
        "descripcion": "Actualizaciones fallidas",
        "condiciones": [
            "actualizacion_fallida"
        ],
        "causas": [
            "poco_espacio_disco",
            "conexion_inestable",
            "archivos_corruptos"
        ],
        "confianza": 0.84
    }
]


# ================================================================
# BASE DE HECHOS
# ================================================================

base_de_hechos = set()

# ================================================================
# MOTOR DE INFERENCIA
# ================================================================

def equiparar(base_conocimiento, hechos):

    reglas_activadas = []

    for regla in base_conocimiento:

        coincidencias = 0

        for condicion in regla["condiciones"]:
            if condicion in hechos:
                coincidencias += 1

        porcentaje = coincidencias / len(regla["condiciones"])

        if coincidencias > 0:

            confianza_final = regla["confianza"] * porcentaje

            reglas_activadas.append({
                "regla": regla,
                "coincidencias": coincidencias,
                "porcentaje": porcentaje,
                "confianza_final": confianza_final
            })

    return reglas_activadas

# ================================================================
# MÚLTIPLES DIAGNÓSTICOS
# ================================================================

def mostrar_diagnosticos(resultados):

    if not resultados:
        print("\nNo se encontraron diagnósticos.")
        return

    resultados.sort(
        key=lambda x: x["confianza_final"],
        reverse=True
    )

    print("\n" + "=" * 60)
    print("RANKING DE DIAGNÓSTICOS")
    print("=" * 60)

    for i, resultado in enumerate(resultados, start=1):

        regla = resultado["regla"]

        print(f"\n#{i}")
        print(f"Regla: {regla['id']}")
        print(f"Descripción: {regla['descripcion']}")
        print(f"Conclusión: {regla['conclusion']}")
        print(f"Confianza: {resultado['confianza_final'] * 100:.2f}%")
        print(
            f"Síntomas coincidentes: "
            f"{resultado['coincidencias']}/{len(regla['condiciones'])}"
        )
        print(f"Causas posibles: {', '.join(regla['causas'])}")

# ================================================================
# ENCADENAMIENTO HACIA ATRÁS
# ================================================================

def backward_chain(meta, base_conocimiento, hechos, visitados=None):

    if visitados is None:
        visitados = set()

    if meta in visitados:
        return []

    visitados.add(meta)

    preguntas = []

    for regla in base_conocimiento:

        if regla["conclusion"] == meta:

            for condicion in regla["condiciones"]:

                if condicion not in hechos:
                    preguntas.append(condicion)

    return preguntas

# ================================================================
# EXPORTAR RED DE INFERENCIA
# ================================================================

def exportar_red(base_conocimiento):

    red = {
        "nodos": [],
        "aristas": []
    }

    nodos = set()

    for regla in base_conocimiento:

        conclusion = regla["conclusion"]

        nodos.add(conclusion)

        for condicion in regla["condiciones"]:

            nodos.add(condicion)

            red["aristas"].append({
                "desde": condicion,
                "hacia": conclusion,
                "regla": regla["id"]
            })

    red["nodos"] = list(nodos)

    print("\n" + "=" * 60)
    print("RED DE INFERENCIA")
    print("=" * 60)

    print(json.dumps(red, indent=4, ensure_ascii=False))

# ================================================================
# PREGUNTAS
# ================================================================

PREGUNTAS = {

    "no_enciende": "¿La PC no enciende?",
    "sin_luces": "¿No hay luces encendidas?",
    "sin_sonido": "¿No hay sonidos?",
    "enciende": "¿La PC enciende?",
    "pitidos_arranque": "¿Hay pitidos al arrancar?",
    "sin_video": "¿No hay imagen?",
    "pantalla_negra": "¿La pantalla está negra?",
    "sin_pitidos": "¿No hay pitidos?",
    "inicia_lento": "¿La PC inicia lenta?",
    "disco_al_100": "¿El disco está al 100%?",
    "se_apaga_solo": "¿La PC se apaga sola?",
    "calor_excesivo": "¿La PC tiene mucho calor?"

}

# ================================================================
# INTERFAZ
# ================================================================

def consultar():

    print("=" * 60)
    print("SISTEMA EXPERTO - DIAGNÓSTICO DE PC")
    print("=" * 60)

    for sintoma, pregunta in PREGUNTAS.items():

        respuesta = input(f"{pregunta} [s/n]: ").lower()

        if respuesta == "s":
            base_de_hechos.add(sintoma)

    resultados = equiparar(
        base_de_conocimiento,
        base_de_hechos
    )

    mostrar_diagnosticos(resultados)

    print("\n" + "=" * 60)
    print("ENCADENAMIENTO HACIA ATRÁS")
    print("=" * 60)

    meta = input(
        "\nEscribe un diagnóstico para analizar: "
    )

    faltantes = backward_chain(
        meta,
        base_de_conocimiento,
        base_de_hechos
    )

    if faltantes:

        print(
            "\nSíntomas faltantes para confirmar el diagnóstico:"
        )

        for f in faltantes:
            print("-", f)

    else:
        print(
            "\nEl diagnóstico ya tiene suficientes síntomas."
        )

    exportar_red(base_de_conocimiento)

# ================================================================
# EJECUCIÓN
# ================================================================

consultar()