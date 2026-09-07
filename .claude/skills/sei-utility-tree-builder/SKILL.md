---
name: sei-utility-tree-builder
description: >-
  Construye, jerarquiza y prioriza Árboles de Utilidad (Utility Trees) para análisis arquitectónico según la metodología ATAM del Software Engineering Institute (SEI). Asigna la matriz bidimensional de priorización (Importancia de Negocio, Riesgo Técnico) con valores (H/M/L, H/M/L) e identifica drivers arquitectónicos críticos. Activar cuando el usuario pida elaborar un árbol de utilidad, priorizar requerimientos no funcionales o analizar tradeoffs ATAM.
---

# Constructor de Árboles de Utilidad SEI (Utility Tree Builder)

Esta skill está especializada en estructurar y priorizar requerimientos de calidad arquitectónicos mediante la herramienta formal **Utility Tree** del método ATAM (*Architecture Tradeoff Analysis Method*) del SEI.

---

## Metodología de Construcción

Al recibir una lista de requerimientos no funcionales o la descripción global de un sistema:

1. **Estructuración Jerárquica en 4 Niveles:**
   * Consulta las especificaciones en [Esquema del Árbol de Utilidad](../sei-quality-attributes/references/utility-tree-schema.md).
   * **Nivel 0 (Raíz):** Define el nodo de *Utilidad General* del sistema (propósito central y salud del negocio).
   * **Nivel 1 (Atributos de Calidad):** Agrupa en categorías de alto nivel (Rendimiento, Disponibilidad, Seguridad, Modificabilidad, etc.).
   * **Nivel 2 (Sub-atributos / Refinamientos):** Subdivide cada atributo en aspectos técnicos concretos (Latencia, Throughput, Tolerancia a fallos, Cifrado, Extensibilidad).
   * **Nivel 3 (Escenarios Hojas):** Formula escenarios específicos con código identificador (`ESC-01`, `ESC-02`, etc.).

2. **Priorización Bidimensional del SEI:**
   * Califica cada escenario hoja con la tupla bidimensional:
     $$\mathbf{(Importancia\ para\ el\ Negocio,\ Dificultad\ o\ Riesgo\ T\acute{e}cnico)}$$
   * Valores válidos: **H** (High / Alto), **M** (Medium / Medio), **L** (Low / Bajo).
   * **Regla de Drivers:** Destaca explícitamente los escenarios clasificados como **(H, H)** como los *Drivers Arquitectónicos Críticos* que deben guiar las decisiones centrales de arquitectura.

3. **Formatos de Salida Obligatorios:**
   * **Tabla Comparativa Markdown:** Con columnas `Atributo`, `Sub-atributo`, `ID`, `Escenario Resumido` y `Prioridad (Negocio, Riesgo)`.
   * **Diagrama Mermaid (`graph TD`):** Para visualización estructural clara de la jerarquía completa.

---

## Restricciones Negativas
* NUNCA califiques escenarios con una sola letra (ej. "Alta" o "H"). La metodología ATAM exige estrictamente la tupla bidimensional `(Importancia, Riesgo)`.
* NUNCA dejes escenarios sin identificar los drivers críticos `(H, H)`.
* NUNCA omitas el sub-atributo intermedio entre el atributo de calidad y el escenario concreto.

---

## Documentación de Referencia
* [Especificación y Esquema del Árbol de Utilidad](../sei-quality-attributes/references/utility-tree-schema.md)
* [Guía de Priorización ATAM](../sei-quality-attributes/references/utility_tree.md)
* [Ejemplos de Árboles de Utilidad](../sei-quality-attributes/examples/ejemplos_escenarios.md)
