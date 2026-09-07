---
name: sei-quality-attributes
description: >-
  Genera escenarios de atributos de calidad de 6 partes según el Software Engineering Institute (SEI), audita y completa escenarios existentes aplicando reglas de inferencia segura, y elabora árboles de utilidad (Utility Trees) priorizados con la matriz bidimensional (Importancia de Negocio, Riesgo Técnico) de ATAM. Activar cuando el usuario solicite definir requerimientos no funcionales, redactar o evaluar escenarios de calidad (Disponibilidad, Rendimiento, Seguridad, Modificabilidad, etc.), auditar completitud de requisitos de arquitectura o construir un Utility Tree.
---

# Atributos de Calidad y Árboles de Utilidad (SEI / ATAM)

Esta skill proporciona los procedimientos rigurosos del Software Engineering Institute (SEI) y del marco *Architecture Tradeoff Analysis Method* (ATAM) para la especificación, auditoría y priorización de atributos de calidad arquitectónicos.

---

## Modos de Operación

La skill detecta automáticamente la intención del usuario y opera en uno de tres modos:

1. **Modo Generación:** Formular escenarios formales de 6 partes a partir de descripciones informales o requerimientos de negocio.
2. **Modo Auditoría y Completitud:** Analizar un escenario provisto, diagnosticar deficiencias y reescribirlo aplicando reglas de inferencia segura.
3. **Modo Árbol de Utilidad (Utility Tree):** Estructurar jerárquicamente los requerimientos del sistema y priorizarlos mediante la matriz bidimensional SEI `(Importancia, Riesgo)`.

---

## Modo 1: Generación de Escenarios (Template SEI de 6 Partes)

Cuando el usuario solicite formular o redactar un escenario para cualquier atributo de calidad (Rendimiento, Disponibilidad, Modificabilidad, Seguridad, Escalabilidad, Testabilidad, Usabilidad, Interoperabilidad):

1. **Identificación del Atributo y Tácticas:**
   * Clasifica el atributo de calidad predominante.
   * Consulta las tácticas y métricas estándar en [Taxonomía SEI](./references/sei-taxonomy.md).
2. **Construcción de las 6 Dimensiones:**
   * **Fuente del estímulo:** Especifica la entidad precisa (interna, externa, usuario, sensor, atacante).
   * **Estímulo:** Describe el evento o condición de llegada concreta.
   * **Artefacto:** Identifica el componente, microservicio, subsistema o interfaz impactada.
   * **Entorno:** Establece el estado operacional (operación normal, hora pico, modo degradado, despliegue).
   * **Respuesta:** Define la acción observable y verificable que ejecuta el sistema.
   * **Medida de respuesta:** Formula la métrica técnica, cuantitativa y no ambigua (ms con percentiles p95/p99, TPS, %, RTO/RPO, horas-hombre).
3. **Bucle de Autoverificación Previa:**
   * ¿Están presentes las 6 partes completas?
   * ¿La medida de respuesta es 100% cuantitativa y testeable?
   * ¿El artefacto delimita una frontera arquitectónica real y no solo "el sistema"?
4. **Formato de Salida Obligatorio:**
   * **Tabla estructurada de 6 filas** (según [Template SEI](./references/sei_scenario_template.md)).
   * **Formato narrativo estándar:** `"[Fuente] genera [Estímulo] sobre [Artefacto] bajo [Entorno]. El sistema [Respuesta] logrando [Medida]."`

---

## Modo 2: Auditoría y Completitud de Escenarios

Cuando el usuario provea un escenario (parcial, informal o ambiguo) y solicite revisarlo o completarlo:

1. **Extracción y Evaluación:**
   * Aplica el algoritmo de auditoría definido en [Reglas de Auditoría](./references/audit-rules.md).
   * Evalúa cada una de las 6 dimensiones asignando un estado:
     * ✅ **Completo:** Explícito y técnicamente riguroso.
     * ⚠️ **Ambiguo / Parcial:** Mencionado pero vago, cualitativo o genérico.
     * ❌ **Ausente:** Omitido en el texto original.
2. **Generación del Diagnóstico:**
   * Presenta un checklist con viñetas y el estado de cada componente.
   * Explica brevemente la deficiencia arquitectónica y el riesgo de dejarla sin resolver.
3. **Aplicación de Reglas de Inferencia Segura:**
   * *Si el Entorno está ausente:* Asume "Operación normal de producción" o el estado inferido por el estímulo.
   * *Si la Fuente está ausente:* Infiere el actor típico según el estímulo (ver [Taxonomía](./references/sei-taxonomy.md)).
   * *Si el Artefacto es genérico ("el sistema"):* Mapea al componente responsable (API Gateway, Core, BD, etc.).
   * *Si la Medida es vaga ("rápido", "seguro"):* Reemplaza por la métrica cuantitativa estándar de la industria.
4. **Entrega de la Versión Corregida:**
   * Presenta el escenario completo y reparado en tabla formal de 6 partes y formato narrativo.

---

## Modo 3: Construcción de Árboles de Utilidad (Utility Tree)

Cuando el usuario provea requerimientos globales de un sistema o solicite elaborar un Utility Tree:

1. **Estructuración Jerárquica de 4 Niveles:**
   * Consulta las especificaciones de diseño en [Esquema del Árbol de Utilidad](./references/utility-tree-schema.md).
   * **Nivel 0 (Raíz):** Utilidad Global del Sistema (propósito central de negocio).
   * **Nivel 1 (Atributos):** Rendimiento, Disponibilidad, Seguridad, Modificabilidad, etc.
   * **Nivel 2 (Sub-atributos / Categorías):** Latencia en pico, Resiliencia ante fallas, Extensibilidad, etc.
   * **Nivel 3 (Escenarios Hojas):** Escenarios concretos codificados con ID único (ej. `ESC-01`, `ESC-02`).
2. **Calificación Bidimensional del SEI:**
   * Asigna a cada escenario la tupla formal:
     $$\mathbf{(Importancia\ de\ Negocio,\ Dificultad\ o\ Riesgo\ T\acute{e}cnico)}$$
   * Valores válidos: **H** (High / Alto), **M** (Medium / Medio), **L** (Low / Bajo).
   * **Identifica y resalta los escenarios `(H, H)` como Drivers Arquitectónicos Críticos.**
3. **Formatos de Salida Obligatorios:**
   * **Tabla Jerárquica Markdown:** Columnas (Atributo, Sub-atributo, ID, Escenario Resumido, Prioridad).
   * **Diagrama Mermaid (`graph TD`):** Para visualización clara de la jerarquía completa.

---

## Restricciones Negativas Estrictas

* **NUNCA** emplees adjetivos cualitativos ni medidas relativas (*"rápido"*, *"robusto"*, *"seguro"*, *"fácil"*, *"eficiente"*). Siempre expresa cantidades con unidades medibles.
* **NUNCA** omitas el *Entorno*: un requerimiento sin entorno carece de validez arquitectónica.
* **NUNCA** utilices *"El sistema"* como artefacto sin especificar el módulo, servicio o capa tecnológica impactada.
* **NUNCA** confundas el *Estímulo* (la causa externa/evento de activación) con la *Respuesta* (el comportamiento reactivo del sistema).
* **NUNCA** asignes una prioridad unidimensional en el árbol de utilidad; la notación del SEI exige siempre la tupla bidimensional `(H|M|L, H|M|L)`.

---

## Material de Referencia y Documentación Complementaria

* [Taxonomía Formal de Atributos de Calidad SEI](./references/sei-taxonomy.md)
* [Reglas de Auditoría y Algoritmo de Inferencia](./references/audit-rules.md)
* [Especificación y Esquema del Árbol de Utilidad](./references/utility-tree-schema.md)
* [Template Canónico de Escenarios](./references/sei_scenario_template.md)
* [Banco de Ejemplos de Escenarios, Auditorías y Árboles](./examples/ejemplos_escenarios.md)
