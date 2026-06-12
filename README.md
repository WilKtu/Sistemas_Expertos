# README — Sistema Experto de Diagnóstico de PC

# Descripción

Este proyecto consiste en la creación de un sistema experto en Python capaz de diagnosticar problemas técnicos en computadoras mediante reglas IF-THEN y un motor de inferencia.

El sistema fue desarrollado utilizando únicamente Python puro, sin librerías externas, aplicando estructuras como:

* listas
* diccionarios
* conjuntos
* funciones

---

# Objetivo

Simular el comportamiento básico de un sistema experto real capaz de:

* Analizar síntomas
* Inferir diagnósticos
* Mostrar múltiples resultados
* Explicar su razonamiento
* Representar una red de inferencia

---

# Componentes del Sistema Experto

## 1. Base de conocimiento

La base de conocimiento almacena todas las reglas del sistema.

Cada regla contiene:

* ID
* descripción
* condiciones
* conclusión
* causas
* confianza

Ejemplo:

```python
{
    "id": "R01",
    "condiciones": ["no_enciende", "sin_luces"],
    "conclusion": "Problema de energía"
}
```

---

## 2. Base de hechos

Es la memoria temporal del sistema.

Aquí se guardan los síntomas ingresados por el usuario.

Se implementó usando un `set()` porque permite búsquedas rápidas.

---

## 3. Motor de inferencia

Es el componente encargado de analizar los hechos y activar reglas compatibles.

Funciones principales:

* equiparar()
* mostrar_diagnosticos()
* backward_chain()
* exportar_red()

---

## 4. Interfaz de explicación

El sistema muestra:

* reglas activadas
* nivel de confianza
* síntomas encontrados
* síntomas faltantes

Esto permite entender cómo llegó al diagnóstico.

---

# Ajustes realizados

## Implementación de múltiples diagnósticos

Originalmente el sistema solo devolvía un resultado.

Se modificó para:

* devolver TODOS los diagnósticos posibles
* ordenarlos por confianza
* mostrar ranking completo

Ventaja:
Permite tomar mejores decisiones y comparar posibilidades.

---

## Implementación de backward chaining

Se agregó una función recursiva llamada:

```python
backward_chain()
```

Esta función trabaja desde la conclusión hacia los síntomas necesarios.

Ventaja:
Permite saber qué información falta para confirmar un diagnóstico.

---

## Exportación de red de inferencia

Se implementó:

```python
exportar_red()
```

La función genera:

* nodos
* aristas
* reglas conectadas

y luego lo imprime como JSON.

Ventaja:
Permite visualizar la estructura lógica del sistema experto.

---

# Desafíos implementados

## Nivel 2 — Múltiples diagnósticos

Se agregó cálculo de porcentaje de coincidencia para mostrar diagnósticos parciales.

---

## Nivel 3 — Encadenamiento hacia atrás

Se implementó una búsqueda recursiva simple para identificar síntomas faltantes.

---

## Nivel 4 — Red de inferencia

Se construyó un grafo lógico usando diccionarios y listas.

---

# Reflexión

## ¿Cuál es la diferencia principal entre un sistema experto y un programa tradicional?

Un programa tradicional sigue instrucciones fijas.

Un sistema experto utiliza conocimiento y reglas para tomar decisiones similares a un experto humano.

---

## ¿Por qué se dice que el conocimiento está separado del motor de razonamiento?

Porque las reglas se almacenan aparte del código que toma decisiones.

Ventaja:
Se pueden agregar nuevas reglas sin modificar el motor principal.

---

## ¿Qué es la base de hechos?

Es la información actual del problema.

La base de conocimiento contiene reglas generales.
La base de hechos contiene datos específicos del caso actual.

---

## ¿Qué significa explicar el razonamiento?

Significa mostrar cómo el sistema llegó a una conclusión.

Esto es importante porque:

* aumenta confianza
* permite auditoría
* ayuda a validar decisiones

Especialmente importante en medicina y derecho.

---

## ¿Por qué fracasaron los sistemas expertos en los años 90?

1. Alto costo de mantenimiento
2. Difícil actualización del conocimiento
3. Limitaciones computacionales
4. Rigidez de reglas
5. Aparición del machine learning

---

## Regla lógica COVID

Regla:

```text
SI (fiebre AND tos) OR perdida_olfato
ENTONCES sospecha_covid
```

Hechos:

```python
{
    fiebre=True,
    tos=False,
    perdida_olfato=True
}
```

Sí se activa.

Porque:

```text
(False) OR (True)
```

Resultado:

```text
True
```

---

## Tabla de verdad

Expresión:

```text
(A AND NOT B) OR (NOT A AND B)
```

| A | B | Resultado |
| - | - | --------- |
| F | F | F         |
| F | V | V         |
| V | F | V         |
| V | V | F         |

---

## Diferencia entre forward y backward chaining

### Encadenamiento hacia adelante

Parte desde los hechos hacia conclusiones.

Ejemplo:
Diagnóstico médico.

---

### Encadenamiento hacia atrás

Parte desde una meta y busca síntomas necesarios.

Ejemplo:
Sistema que verifica si un estudiante puede graduarse.

---

# Reglas IF-THEN para recomendar lenguajes

## Regla 1

IF objetivo = desarrollo_web
THEN aprender JavaScript

---

## Regla 2

IF objetivo = analisis_datos
THEN aprender Python

---

## Regla 3

IF objetivo = videojuegos
THEN aprender C#

---

# Red de inferencia

```text
desarrollo_web  ─────► JavaScript
analisis_datos  ─────► Python
videojuegos     ─────► C#
```

---

# Problema de reglas duplicadas

Si dos reglas tienen las mismas condiciones pero conclusiones distintas:

* puede existir conflicto
* resultados ambiguos

Solución:

* usar prioridades
* usar factores de confianza
* pedir más información al usuario

---

# Conclusión

El proyecto permitió comprender cómo funcionan internamente los sistemas expertos:

* reglas
* inferencia
* razonamiento
* explicación
* representación del conocimiento

Además permitió aplicar lógica computacional y estructuras de datos en Python.
