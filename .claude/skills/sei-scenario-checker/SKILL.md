---
name: sei-scenario-checker
description: >-
  Audita, valida y completa escenarios de atributos de calidad según el estándar de 6 partes del SEI. Diagnostica ambigüedades, evalúa la presencia de cada componente y aplica reglas de inferencia segura para reescribir y corregir escenarios deficientes. Activar cuando el usuario pida revisar, verificar, auditar o completar un escenario de arquitectura.
---

# Auditor y Corrector de Escenarios SEI (Checker)

Esta skill está especializada en **auditar la completitud metodológica de escenarios de calidad**, identificar errores y ambigüedades frecuentes, y reescribir escenarios incompletos aplicando **Reglas de Inferencia Segura**.

---

## Flujo de Trabajo de Auditoría

Al recibir un escenario propuesto por el usuario:

1. **Extracción y Evaluación de las 6 Partes:**
   * Consulta las heurísticas en [Reglas de Auditoría](../sei-quality-attributes/references/audit-rules.md).
   * Evalúa cada componente:
     * **Fuente:** ¿Está identificado el sujeto o actor específico?
     * **Estímulo:** ¿Es un evento concreto o está mezclado con la respuesta?
     * **Artefacto:** ¿Se delimita un componente/servicio o dice vagamente "el sistema"?
     * **Entorno:** ¿Se explicita el estado operativo y régimen de carga?
     * **Respuesta:** ¿Es una acción observable del sistema o solo un deseo abstracto?
     * **Medida de Respuesta:** ¿Es una métrica numérica objetiva o usa calificativos subjetivos (*"rápido"*, *"robusto"*, *"seguro"*)?

2. **Informe Diagnóstico:**
   * Presenta un checklist con estados claros:
     * ✅ **Completo:** La dimensión está explícita y precisa.
     * ⚠️ **Ambiguo / Parcial:** Presente pero vago o genérico.
     * ❌ **Ausente:** La dimensión no figura en el texto original.
   * Explica los riesgos arquitectónicos de las deficiencias detectadas.

3. **Inferencia y Reparación:**
   * Aplica las Reglas de Inferencia Segura:
     * Infiere el estado operativo canónico para el entorno si falta (*"Operación normal"* o *"Pico de carga"*).
     * Mapea *"el sistema"* al componente de frontera o subsistema de procesamiento adecuado.
     * Reemplaza medidas vagas por métricas estándar (latencia en percentiles, TPS, %, RTO/RPO, horas-hombre).

4. **Entrega de la Versión Corregida:**
   * Provee la versión formal reparada en tabla de 6 filas y formato narrativo.

---

## Restricciones Negativas
* NUNCA apruebes como "completo" un escenario que carezca de medida numérica verificable.
* NUNCA omitas el estado operativo del entorno.
* NUNCA aceptes "el sistema" como artefacto sin delimitar la frontera del componente.

---

## Documentación de Referencia
* [Reglas de Auditoría y Algoritmo de Inferencia](../sei-quality-attributes/references/audit-rules.md)
* [Taxonomía y Métricas Estándar SEI](../sei-quality-attributes/references/sei-taxonomy.md)
* [Casos Prácticos de Auditoría](../sei-quality-attributes/examples/ejemplos_escenarios.md)
