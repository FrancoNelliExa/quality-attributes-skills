---
name: sei-quality-attributes
description: >-
  Guía y procedimientos para formular escenarios de atributos de calidad según el template de 6 partes del SEI (Software Engineering Institute), auditar y completar escenarios existentes evaluando su completitud, y construir árboles de utilidad (Utility Trees) priorizados con matriz (Importancia, Riesgo) para arquitectura de software. Usar cuando el usuario pida definir o revisar requerimientos no funcionales, escenarios ATAM, o árboles de utilidad.
---

# Atributos de Calidad y Árboles de Utilidad (SEI)

Esta skill proporciona las pautas metodológicas del Software Engineering Institute (SEI) para:
1. **Generar escenarios de atributos de calidad** de 6 partes.
2. **Auditar y completar escenarios existentes**, verificando su completitud y eliminando ambigüedades.
3. **Elaborar y priorizar Árboles de Utilidad (Utility Trees)** para análisis arquitectónico (ATAM).

---

## Modos de Operación

### 1. Generación de Escenarios (Template de 6 Partes)

Cuando el usuario pida formular un escenario para un atributo de calidad (Disponibilidad, Rendimiento, Modificabilidad, Seguridad, Testabilidad, Usabilidad, etc.):

1. Consulta los detalles de cada campo en [Template SEI](./references/sei_scenario_template.md).
2. Estructura el escenario respondiendo a las seis dimensiones:
   * **Fuente del estímulo:** Quién o qué produce el estímulo.
   * **Estímulo:** El evento o condición que afecta al sistema.
   * **Artefacto:** El componente, subsistema o servicio afectado.
   * **Entorno:** El estado operativo (normal, alta concurrencia, falla de nodo, despliegue).
   * **Respuesta:** La acción observable que el sistema ejecuta ante el estímulo.
   * **Medida de respuesta:** Métrica cuantificable, no ambigua y objetivamente verificable (tiempo en ms/s, %, RTO/RPO, horas-hombre).
3. Presenta el resultado en:
   * **Tabla estructurada** de 6 filas.
   * **Formato narrativo** resumen.

---

### 2. Auditoría y Completado de Escenarios

Cuando el usuario provea un escenario y pregunte si está completo o cómo mejorarlo:

1. **Checklist de Completitud:** Evalúa rigurosamente cada una de las 6 partes según [Criterios de Auditoría](./references/sei_scenario_template.md):
   * ¿La fuente y el estímulo están claramente diferenciados?
   * ¿El artefacto está delimitado con suficiente precisión?
   * ¿El entorno describe las condiciones operativas reales?
   * ¿La medida de respuesta es numérica y verificable, o usa adjetivos ambiguos ("rápido", "robusto", "fácil")?
2. **Diagnóstico:**
   * Lista con viñetas indicando qué partes están **Completas** (✅), cuáles **Incompletas o Ambiguas** (⚠️) y cuáles **Ausentes** (❌).
   * Explica brevemente por qué las partes observadas presentan deficiencias arquitectónicas.
3. **Propuesta de Escenario Completo:**
   * Brinda una o dos opciones de escenario completado en la tabla de 6 partes con métricas realistas y precisas.
   * Consulta ejemplos en [Casos Prácticos](./examples/ejemplos_escenarios.md).

---

### 3. Elaboración de Árbol de Utilidad (Utility Tree)

Cuando el usuario solicite estructurar los atributos de calidad de un sistema o un ejercicio integrador:

1. Estructura la jerarquía en 3 niveles partiendo de la raíz **Utilidad**:
   * **Nivel 1 (Atributos de Calidad):** Rendimiento, Disponibilidad, Seguridad, etc.
   * **Nivel 2 (Sub-atributos / Refinamientos):** Latencia, Resiliencia ante fallos, Auditoría, Extensibilidad.
   * **Nivel 3 (Escenarios concretos):** Escenarios específicos identificados con un código único (ej. `ESC-01`, `ESC-02`).
2. Asigna a cada escenario la tupla de priorización bidimensional:
   $$\text{(Importancia para el Negocio o Cliente, Dificultad o Riesgo Técnico)}$$
   * Valores: **H** (High/Alto), **M** (Medium/Medio), **L** (Low/Bajo).
   * Identifica y destaca los escenarios **(H, H)** como los **drivers arquitectónicos críticos**.
3. Presenta el árbol en dos formatos complementarios:
   * **Tabla comparativa del árbol** (Atributo, Sub-atributo, ID, Escenario, Prioridad).
   * **Diagrama Mermaid** (`graph TD` o `mindmap`) para visualización conceptual.
4. Consulta las pautas de priorización en [Guía de Árbol de Utilidad](./references/utility_tree.md).

---

## Documentación de Referencia

* [Template de 6 Partes y Criterios de Completitud](./references/sei_scenario_template.md)
* [Guía y Matriz de Priorización del Árbol de Utilidad](./references/utility_tree.md)
* [Ejemplos de Escenarios y Casos de Auditoría](./examples/ejemplos_escenarios.md)
