# Skills de Arquitectura de Software: Atributos de Calidad y Árboles de Utilidad (SEI / ATAM)

### Autores: Nicola Satragni - Franco Nelli
**Cátedra:** Ingeniería de Software 1  
**Repositorio GitHub:** [FrancoNelliExa/quality-attributes-skills](https://github.com/FrancoNelliExa/quality-attributes-skills)  
**Entrega:** Repositorio GitHub y archivo comprimido `.zip` adjunto.

---

## Resumen del Proyecto

Este proyecto implementa una suite completa de **Skills (estilo Claude / Antigravity)** especializadas en la ingeniería de requerimientos no funcionales y la evaluación de arquitecturas de software bajo los estándares rigurosos del **Software Engineering Institute (SEI)** y el método **ATAM (*Architecture Tradeoff Analysis Method*)** (*Software Architecture in Practice*, Bass, Clements & Kazman).

A partir de un informe técnico exhaustivo generado con Gemini Deep Research ([INFORME.md](./INFORME.md)), se diseñaron, implementaron y testearon las capacidades para:

1. **Generar atributos de calidad** formalizados bajo el **template canónico de 6 partes del SEI** a partir de especificaciones informales de negocio.
2. **Auditar y evaluar la completitud** de escenarios provistos por el usuario, diagnosticando ambigüedades y vacíos técnicos, y completándolos mediante **Reglas de Inferencia Segura**.
3. **Elaborar y priorizar Árboles de Utilidad (*Utility Trees*)** en 4 niveles jerárquicos con la **matriz bidimensional `(Importancia para el Negocio, Dificultad/Riesgo Técnico)`**, identificando explícitamente los *Drivers Arquitectónicos Críticos* `(H, H)`.
4. Proveer **material bibliográfico y complementario modular en `references/`** para enfocar el razonamiento del LLM sin saturar la ventana de contexto.
5. Validar exhaustivamente las habilidades mediante una **suite de pruebas automatizadas con ejemplos conocidos**.

---

## Arquitectura de las Skills y Estructura del Repositorio

Para brindar máxima flexibilidad y compatibilidad multiplataforma (Claude Code, Antigravity, Cursor, etc.), el proyecto se organiza en una **Skill Maestra unificada** (`sei-quality-attributes`) y **3 Skills modulares enfocadas** por responsabilidad:

```text
.
├── INFORME.md                           # Dossier de investigación y especificación técnica (Deep Research)
├── README.md                            # Documentación integral del proyecto y entrega
├── quality-attributes-skills.zip        # Paquete comprimido para entrega alternativa
├── tests/
│   ├── test_cases.md                    # Suite de 6 casos de prueba con trazas completas de ejecución
│   └── validate_skills.py               # Script de pruebas automatizadas y aserciones de calidad
├── .agents/skills/                      # Directorio nativo para Antigravity
│   ├── sei-quality-attributes/          # Skill Maestra Integral (Generación + Auditoría + Utility Tree)
│   │   ├── SKILL.md                     # Directiva principal con triggers, bucles de autoverificación y restricciones
│   │   ├── references/                  # Material complementario cargado bajo demanda
│   │   │   ├── sei-taxonomy.md          # Taxonomía formal de 8 atributos, tácticas y catálogo de métricas
│   │   │   ├── audit-rules.md           # Algoritmo de auditoría y reglas de inferencia segura
│   │   │   ├── utility-tree-schema.md   # Especificación jerárquica ATAM y matriz de priorización 2D
│   │   │   ├── sei_scenario_template.md # Template canónico de 6 partes y formatos de salida
│   │   │   └── utility_tree.md          # Guía rápida y ejemplos de árboles
│   │   └── examples/
│   │       └── ejemplos_escenarios.md   # Banco de ejemplos prácticos y comparativas antes/después
│   ├── sei-scenario-generator/          # Skill modular: Generador de escenarios de 6 partes
│   │   └── SKILL.md
│   ├── sei-scenario-checker/            # Skill modular: Auditor y corrector de escenarios
│   │   └── SKILL.md
│   └── sei-utility-tree-builder/        # Skill modular: Constructor de árboles de utilidad ATAM
│       └── SKILL.md
├── .claude/skills/                      # Mirror para Claude Code / proyectos Anthropic Claude
└── skills/                              # Mirror universal estandarizado para inspección directa
```

---

## Ejemplos dados a la IA:

Los requerimientos base dados a la IA para contextualizar y generar las especificaciones arquitectónicas fueron:

| Quality Attributes | Scenario | Priority |
| :---|:---| :---: |
| **Availability** | When the RFP database does not respond, Lionheart should log the fault and respond with stale data within 3 seconds. | High |
| **Availability** | A user’s searches for open RFPs and receives a list of RFPs 99% of the time on average over the course of the year. | High |
| **Scalability** | New servers can be added during a planned maintenance window (less than 7 hours). | Low |
| **Performance** | A user sees search results within 5 seconds when the system is at an average load of 2 searches per second. | High |
| **Reliability** | Updates to RFPs should be reflected in the application within 24 hours of the change. | Low |
| **Availability** | A user-initiated update (for example, starring an RFP) is reflected in the system within 5 seconds. | Low |
| **Availability** | The system can handle a peak load of 100 searches per second with no more than a 10% dip in average response times. | Low |
| **Scalability** | Data growth is expected to expand at a rate of 5% annually. The system should be able to grow to handle this with minimal effort. | Low |

### Directivas y Reglas de Diseño Metodológico Suministradas a la IA
1. **Eliminación de Ambigüedades Cualitativas:** Prohibición estricta de términos vagos como *"rápido"*, *"robusto"*, *"seguro"* o *"minimizar fallas"*. Exigencia de magnitudes verificables (latencia en percentiles p95/p99, TPS, MTBF/MTTR, RTO/RPO, horas-persona).
2. **Framework Canónico SEI de 6 Partes:** Mapeo estricto e innegociable a Fuente, Estímulo, Artefacto, Entorno, Respuesta y Medida de Respuesta.
3. **Árbol de Utilidad ATAM y Matriz Bidimensional:** Descomposición en 4 niveles (Utilidad $\rightarrow$ Atributo $\rightarrow$ Sub-atributo $\rightarrow$ Escenario) y asignación obligatoria de la tupla `(Importancia de Negocio, Dificultad o Riesgo Técnico)` con valores `(H/M/L, H/M/L)`.
4. **Patrones de Arquitectura de Skills:** Formulación de encabezados YAML con descripciones semánticamente densas para activación contextual (*skill triggering*), bucles de autoverificación previa (*self-verification loops*), restricciones negativas explícitas y una separación modular del conocimiento profundo en la carpeta `references/`.

---

## Ejemplos usados para testing:


`PERFORMANCE`

> Five hundred users initiate 2,000 requests in a 30-second interval, under normal operations. The system processes all of the requests with an average latency of two seconds.

`DEPLOYABILITY`

> A new release of an authentication/authorization service (which our product uses) is made
> available in the component marketplace and the product owner decides to
> incorporate this version into the release. The new service is tested and
> deployed to the production environment within 40 hours of elapsed time
> and no more than 120 person-hours of effort. The deployment introduces no
> defects and no SLA is violated.”

`INTEGRABILIDAD`

> A new data filtering component has become available in
> the component marketplace. The new component is integrated into the
> system and deployed in 1 month, with no more than 1 person-month of
> effort.

`SECURITY`

> A disgruntled employee at a remote location attempts to
> improperly modify the pay rate table during normal operations. The
> unauthorized access is detected, the system maintains an audit trail, and
> the correct data is restored within one day.

`TESTEABILITY`

> The developer
> completes a code unit during development and performs a test sequence
> whose results are captured and that gives 85 percent path coverage within
> 30 minutes.

`USABILIDAD`

> The user downloads a new application
> and is using it productively after 2 minutes of experimentation.

`SAFETY`
> A sensor in the patient monitoring system
> fails to report a life-critical value after 100 ms. The failure is logged, a
> warning light is illuminated on the console, and a backup (lower-fidelity)
> sensor is engaged. The system monitors the patient using the backup sensor
> after no more than 300 ms.

`MODIFICABILIDAD`

> A developer
> wishes to change the user interface. This change will be made to the code
> at design time, it will take less than three hours to make and test the
> change, and no side effects will occur.


---

La suite de pruebas fue testeada con **6 casos de prueba con ejemplos conocidos y de referencia bibliográfica**. El detalle completo de los prompts, trazas de razonamiento y salidas generadas se encuentra documentado en [tests/test_cases.md](./tests/test_cases.md):

```text
================================================================
 MATRIZ DE TESTING - EJEMPLOS CONOCIDOS
================================================================
 TC-01 | E-Commerce en Black Friday        | Rendimiento / Escalabilidad | PASS ✅
 TC-02 | Ciberataque en Core Bancario      | Seguridad / Disponibilidad  | PASS ✅
 TC-03 | Plataforma Telemedicina Crítica   | Integrador Utility Tree     | PASS ✅
 TC-04 | Radar de Control de Tráfico Aéreo | Disponibilidad Crítica      | PASS ✅
 TC-05 | Usabilidad en Punto de Venta POS  | Usabilidad / Tasa de Error  | PASS ✅
 TC-06 | Integración Pasarela en Microserv.| Modificabilidad             | PASS ✅
================================================================
```

### Síntesis de los Casos de Prueba Principales

#### 1. Test de Generación: E-Commerce bajo Black Friday (`TC-01`)
* **Entrada informal:** *"Durante el Black Friday, cuando entren miles de usuarios a comprar al mismo tiempo, el proceso de pago no se tiene que caer y debe procesar los cobros rápido."*
* **Resultado de la Skill:** Generó el escenario de 6 partes especificando:
  * *Fuente:* Compradores concurrentes autenticados.
  * *Estímulo:* 12.000 solicitudes simultáneas de pago por minuto.
  * *Artefacto:* Microservicio de Transacciones de Compra y Pasarela de Pagos.
  * *Entorno:* Evento de alta demanda comercial (Black Friday, 350% de tráfico habitual).
  * *Respuesta:* Encolamiento en broker de mensajes, autoescalado de workers y confirmación asíncrona.
  * *Medida de respuesta:* Latencia p95 $\le 1.5\text{ s}$, throughput sostenido de $5.000\text{ TPS}$, $0\%$ de órdenes perdidas y disponibilidad del $99.99\%$.

#### 2. Test de Auditoría y Corrección: Ciberataque en Core Bancario (`TC-02`)
* **Entrada deficiente:** *"Un hacker intenta hacer transacciones falsas pero el sistema bancario lo detecta y no se cae."*
* **Resultado de la Skill:**
  * **Diagnóstico:** Marcó Artefacto como ❌ Genérico ("el sistema bancario"), Entorno como ❌ Ausente, y Medida como ❌ Inaceptable ("no se cae").
  * **Inferencia y Corrección:** Reconstruyó el escenario delimitando el *API Gateway de Transacciones y Motor de Prevención de Fraude*, infirió *Operación Normal de producción*, tácticas de *bloqueo perimetral y despacho a SIEM*, con medidas de $100\%$ de intentos bloqueados, auditoría en $\le 50\text{ ms}$ y disponibilidad del $99.999\%$.

#### 3. Test de Árbol de Utilidad: Plataforma de Telemedicina Crítica (`TC-03`)
* **Resultado de la Skill:** Estructuró la jerarquía completa:
  * **Raíz:** `UTILIDAD: Plataforma de Telemedicina Crítica para Pacientes Graves`.
  * **Rendimiento $\rightarrow$ Latencia de Telemetría:** Transmisión de ECG en vivo con latencia $\le 200\text{ ms}$ $\rightarrow$ **(H, H) [DRIVER ARQUITECTÓNICO CRÍTICO]**.
  * **Seguridad $\rightarrow$ Confidencialidad:** Cifrado integral TLS 1.3 / AES-256 de Historias Clínicas con auditoría inmutable en $\le 50\text{ ms}$ $\rightarrow$ **(H, H) [DRIVER ARQUITECTÓNICO CRÍTICO]**.
  * **Disponibilidad $\rightarrow$ Resiliencia:** Reconexión de streaming de video en $\le 3\text{ s}$ ante caída de SFU $\rightarrow$ **(H, M)**.
  * **Modificabilidad $\rightarrow$ Adaptación Regulatoria:** Incorporación de nuevo estándar de hashing en $\le 40\text{ h-p}$ $\rightarrow$ **(M, L)**.
  * **Usabilidad $\rightarrow$ Alerta de Emergencia:** Disparo de ambulancia en $\le 2\text{ clics}$ y menos de $3\text{ s}$ $\rightarrow$ **(H, M)**.
  * **Visualización:** Generación automática de diagrama sintáctico Mermaid (`graph TD`).

### Validación Automatizada
El repositorio incluye un script de test en Python (`tests/validate_skills.py`) que valida automáticamente:
1. Existencia e integridad de todo el material complementario en `references/`.
2. Encabezados YAML válidos y descripciones semánticas en cada `SKILL.md`.
3. Cobertura del 100% de los casos de prueba y presencia de las 6 partes del SEI.
4. Cumplimiento de aserciones de no-ambigüedad y sintaxis de tuplas ATAM `(H/M/L, H/M/L)`.

Para ejecutar las pruebas:
```bash
python3 tests/validate_skills.py
```
*Resultado:* **4/4 suites aprobadas (100% PASS)**.

---

## Informe Resultante:

El desarrollo de estas skills se fundamenta en la investigación técnica detallada en [INFORME.md](./INFORME.md), estructurada en tres ejes cardinales:

```text
                                  [ INFORME.md ]
                                         │
     ┌───────────────────────────────────┼───────────────────────────────────┐
     ▼                                   ▼                                   ▼
[ EJE 1: Teoría SEI ]           [ EJE 2: Arquitectura Skills ]      [ EJE 3: Blueprint y Testing ]
- Template 6 Partes             - YAML Frontmatter semántico        - Blueprint 3 Skills Modulares
- Taxonomía de 8 Atributos      - Bucles de Autoverificación        - Suite de 6 Casos de Prueba
- Algoritmo de Auditoría        - Restricciones Negativas           - Matriz de Validación
- Matriz 2D ATAM (Negocio,Riesgo)- Carpeta references/ modular       - Script Automatizado Python
```

* **Eje 1 (Fundamentación Teórica del SEI):** Análisis formal de las 6 partes (Fuente, Estímulo, Artefacto, Entorno, Respuesta, Medida de Respuesta). Taxonomía de estímulos y métricas para Disponibilidad, Rendimiento, Modificabilidad, Seguridad, Escalabilidad, Testabilidad, Usabilidad e Interoperabilidad. Algoritmo sistemático de 4 pasos para auditar completitud y aplicar reglas de inferencia segura. Estructura jerárquica del Utility Tree y matriz de priorización del ATAM.
* **Eje 2 (Arquitectura de Skills estilo Claude / Antigravity):** Pautas de diseño para LLMs: activación semántica contextual mediante la clave `description`, patrones de autoverificación antes de emitir la salida, restricciones negativas estrictas y técnica de *progressive context loading* utilizando `references/` para mantener el contexto limpio de tokens redundantes.
* **Eje 3 (Blueprint de Implementación y Casos de Prueba):** Especificación de las skills especializadas, definición de la suite de pruebas sobre casos de estudio conocidos y directivas de entrega para el repositorio y empaquetado zip.

Para consultar el dossier técnico completo, revisar directamente el archivo [INFORME.md](./INFORME.md).

---

## Guía de Uso de las Skills

### ¿Cómo activar las skills?

Las skills son detectadas automáticamente por agentes compatibles (Claude Code, Antigravity) en función de las palabras clave de tu solicitud. También puedes invocarlas directamente:

#### 1. Para generar un escenario de 6 partes:
> *"Formula un escenario de atributo de calidad según el template de 6 partes del SEI para la pasarela de pagos de un e-commerce durante el Hot Sale."*

#### 2. Para auditar y corregir un escenario:
> *"Revisa este escenario: 'El sistema tiene que responder rápido las consultas de los clientes cuando hay muchos conectados'. ¿Está completo? ¿Cómo debería completarse según el SEI?"*

#### 3. Para construir un Árbol de Utilidad:
> *"Construye un Árbol de Utilidad priorizado con matriz (Importancia, Riesgo) y diagrama Mermaid para una plataforma bancaria de préstamos digitales."*

---

## Empaquetado y Entrega

El proyecto se encuentra versionado y listo para su evaluación mediante:
1. **Repositorio GitHub:** [https://github.com/FrancoNelliExa/quality-attributes-skills](https://github.com/FrancoNelliExa/quality-attributes-skills)
2. **Archivo ZIP:** `quality-attributes-skills.zip` generado en la raíz del repositorio, conteniendo todo el código, skills, referencias, tests y documentación.
