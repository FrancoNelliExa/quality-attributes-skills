---
name: sei-scenario-generator
description: >-
  Genera escenarios formales de atributos de calidad según el template de 6 partes del SEI (Software Engineering Institute) a partir de requerimientos funcionales o informales. Activar cuando el usuario pida redactar, formular o transformar requerimientos en escenarios de rendimiento, disponibilidad, desplegabilidad, seguridad, modificabilidad, safety / inocuidad, integrabilidad, escalabilidad o testabilidad.
---

# Generador de Escenarios de Calidad SEI (6 Partes)

Esta skill está especializada en transformar requerimientos informales, historias de usuario o descripciones generales de negocio en **escenarios formales de atributos de calidad de 6 partes** bajo el estándar del Software Engineering Institute (SEI).

---

## Procedimiento de Generación

Al recibir una necesidad o requerimiento no funcional:

1. **Identificación y Clasificación:**
   * Detecta el atributo de calidad predominante (Disponibilidad, Rendimiento, Desplegabilidad, Seguridad, Modificabilidad, Safety / Inocuidad, Integrabilidad, Escalabilidad, Testabilidad, Usabilidad o Interoperabilidad).
   * **Criterio de Desambiguación Safety vs. Disponibilidad:** Si el requerimiento involucra la preservación de la vida humana, valores críticos para la vida (*life-critical values*), estados seguros (*fail-safe*) o conmutación a sensores/modos de respaldo ante peligros (*hazards*) en sistemas médicos o de misión crítica, clasifícalo estrictamente como **Safety (Seguridad Funcional / Inocuidad)**.
   * **Criterio de Desambiguación Integrabilidad vs. Modificabilidad:** Si el requerimiento se centra en ensamblar, adaptar o incorporar componentes externos, provistos por terceros o desde un *marketplace de componentes* (COTS, librerías externas), evaluando el esfuerzo y tiempo de integración (personas-mes, meses de calendario), clasifícalo como **Integrabilidad (Integrability)**.
   * **Criterio de Desambiguación Desplegabilidad vs. Modificabilidad:** Si el requerimiento se centra en el empaquetado, incorporación de versiones/releases (propias o de terceros), pipelines CI/CD, despliegue a producción o staging, tiempo transcurrido de despliegue (*elapsed time*), horas-persona de despliegue, rollback o cumplimiento de SLA sin defectos durante la liberación, clasifícalo como **Desplegabilidad (Deployability)**.
   * Consulta el catálogo de métricas y tácticas en [Taxonomía SEI](../sei-quality-attributes/references/sei-taxonomy.md).

2. **Formulación Rigurosa de las 6 Partes:**
   * **1. Fuente del estímulo (*Source*):** Quién o qué origina el evento (actor humano específico, nodo, red, atacante externo, etc.).
   * **2. Estímulo (*Stimulus*):** Condición de entrada o evento medible que arriba al sistema (solicitud masiva, caída de proceso, intento de intrusión).
   * **3. Artefacto (*Artifact*):** El subsistema, servicio, base de datos o módulo delimitado que recibe el impacto directo.
   * **4. Entorno (*Environment*):** El régimen operativo en el que ocurre el estímulo (operación normal, hora pico, modo degradado, durante despliegue).
   * **5. Respuesta (*Response*):** La táctica arquitectónica y acción observable que ejecuta el artefacto ante el estímulo.
   * **6. Medida de respuesta (*Response Measure*):** Métrica cuantitativa, objetiva y verificable (latencia p95/p99 en ms, TPS, uptime %, MTTR/RTO, horas-persona).

3. **Bucle de Autoverificación Previa:**
   * ¿Están presentes las 6 dimensiones sin excepción?
   * ¿Se eliminaron adjetivos vagos como "rápido", "robusto", "adecuado"?
   * ¿El artefacto delimita un componente concreto y no la totalidad del sistema?

---

## Formato de Salida

Presenta el escenario en dos formatos obligatorios:

### 1. Formato Tabular Estructurado
```markdown
| Dimensión SEI | Especificación Arquitectónica |
| :--- | :--- |
| **Fuente del estímulo** | [Entidad precisa] |
| **Estímulo** | [Evento o condición cuantitativa] |
| **Artefacto** | [Componente o subsistema delimitado] |
| **Entorno** | [Estado operativo del sistema] |
| **Respuesta** | [Táctica y comportamiento observable] |
| **Medida de respuesta** | [Métrica numérica verificable con unidades] |
```

### 2. Formato Narrativo Canónico
> *"[Fuente] genera [Estímulo] sobre [Artefacto] bajo condiciones de [Entorno]. El sistema [Respuesta], garantizando [Medida de respuesta]."*

---

## Documentación de Referencia
* [Taxonomía de Atributos SEI](../sei-quality-attributes/references/sei-taxonomy.md)
* [Template Canónico SEI](../sei-quality-attributes/references/sei_scenario_template.md)
* [Banco de Ejemplos de Escenarios](../sei-quality-attributes/examples/ejemplos_escenarios.md)
