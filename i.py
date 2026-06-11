# ================================================================
# SISTEMA EXPERTO: Diagnóstico de PC
# Implementación con motor de inferencia hacia adelante
# ================================================================

# ──────────────────────────────────────────────────────────────
# COMPONENTE 1: BASE DE CONOCIMIENTO
# Aquí vive el conocimiento del experto técnico.
# Cada regla tiene: id, condiciones (lista de síntomas requeridos),
# conclusión y un factor de confianza de 0 a 1.
# ──────────────────────────────────────────────────────────────

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



# ──────────────────────────────────────────────────────────────
# COMPONENTE 2: BASE DE HECHOS (Working Memory)
# Estado actual del caso. Usamos un set de Python para
# representar los síntomas presentes (eficiente para búsqueda).
# ──────────────────────────────────────────────────────────────

base_de_hechos = set()  # vacía al inicio, se llena con los síntomas

# ──────────────────────────────────────────────────────────────
# COMPONENTE 3: MOTOR DE INFERENCIA
# Funciones de equiparación y resolución de conflictos
# ──────────────────────────────────────────────────────────────

def equiparar(base_conocimiento, hechos):
    """
    Proceso de equiparación (pattern matching).
    Retorna todas las reglas cuyas condiciones están satisfechas
    por los hechos actuales. Esto es el 'conflict set'.
    """
    conflict_set = []
    for regla in base_conocimiento:
        # Verificar si TODOS los síntomas de la regla están en los hechos
        # set.issubset() es O(len(condiciones)), más eficiente que un bucle
        if set(regla['condiciones']).issubset(hechos):
            conflict_set.append(regla)
    return conflict_set


def resolver_conflictos(conflict_set):
    """
    Estrategia de resolución de conflictos: mayor confianza.
    Si hay empate, preferir la regla con más condiciones (más específica).
    """
    if not conflict_set:
        return None
    return max(
        conflict_set,
        key=lambda r: (r['confianza'], len(r['condiciones']))
    )


def inferir(base_conocimiento, hechos):
    """
    Motor de inferencia principal.
    Ejecuta el ciclo de equiparación → resolución → ejecución.
    """
    print()
    print('━' * 55)
    print('  MOTOR DE INFERENCIA INICIADO')
    print('━' * 55)
    print(f'  Hechos ingresados: {hechos}')
    print()

    conflict_set = equiparar(base_conocimiento, hechos)

    if not conflict_set:
        print('  ⚠ No se encontraron reglas aplicables.')
        print('  Considera agregar más síntomas o revisar la base de conocimiento.')
        return

    print(f'  Reglas que aplican (conflict set): {[r["id"] for r in conflict_set]}')
    print()

    regla = resolver_conflictos(conflict_set)

    print('  DIAGNÓSTICO')
    print('  ───────────────────────────────────────────────────')
    print(f'  Regla aplicada: {regla["id"]} — {regla["descripcion"]}')
    print(f'  Recomendación:  {regla["conclusion"]}')
    print(f'  Confianza:      {regla["confianza"] * 100:.0f}%')
    print()

    # COMPONENTE 4: INTERFAZ DE EXPLICACIÓN
    print('  TRAZABILIDAD DEL RAZONAMIENTO')
    print('  ───────────────────────────────────────────────────')
    print(f'  Síntomas que activaron la regla: {regla["condiciones"]}')
    if len(conflict_set) > 1:
        descartadas = [r['id'] for r in conflict_set if r['id'] != regla['id']]
        print(f'  Reglas descartadas por menor confianza: {descartadas}')
    print('━' * 55)



# ──────────────────────────────────────────────────────────────
# COMPONENTE 5: INTERFAZ DE USUARIO
# ──────────────────────────────────────────────────────────────

PREGUNTAS = {
    "no_enciende":              "¿El equipo NO enciende (sin luces, sin sonido)?",
    "sin_luces":                "¿No hay ninguna luz LED encendida?",
    "sin_sonido":               "¿No se escucha ningún sonido al encender?",
    "enciende":                 "¿El equipo SÍ enciende (hay luces y/o sonido)?",
    "pitidos_arranque":         "¿Se escuchan pitidos (beeps) al encender?",
    "sin_video":                "¿La pantalla no muestra absolutamente nada?",
    "pantalla_negra":           "¿La pantalla queda en negro (sin pitidos)?",
    "sin_pitidos":              "¿No se escuchan pitidos?",
    "inicia_lento":             "¿El equipo tarda más de 3 minutos en iniciar?",
    "disco_al_100":             "¿El administrador de tareas muestra disco al 100%?",
    "ventilador_siempre_activo":"¿El ventilador está siempre a máxima velocidad?",
    "pantalla_azul_frecuente":  "¿Aparece pantalla azul (BSOD) con frecuencia?",
    "se_apaga_solo":            "¿El equipo se apaga solo sin advertencia?",
    "calor_excesivo":           "¿El chasis está muy caliente al tacto?"
}

def consultar():
    print()
    print('=' * 55)
    print('  SISTEMA EXPERTO: Diagnóstico de Computador')
    print('  Responde s (sí) o n (no) a cada pregunta')
    print('=' * 55)
    print()

    for sintoma, pregunta in PREGUNTAS.items():
        resp = input(f'  {pregunta} [s/n]: ').strip().lower()
        if resp == 's':
            base_de_hechos.add(sintoma)

    inferir(base_de_conocimiento, base_de_hechos)


# Ejecutar
consultar()
