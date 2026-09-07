Dossier de Investigación y Especificación Técnica: Arquitectura de Escenarios de Calidad, Árboles de Utilidad y Creación de Skills SEI
EJE 1: Fundamentación Teórica del Framework de Calidad del SEI
1. Análisis Profundo de Escenarios de 6 Partes
Un escenario de atributo de calidad según el SEI (Software Engineering Institute) es una descripción breve y caracterizada de cómo responderá un sistema ante un estímulo determinado en un contexto operativo específico. Para evitar ambigüedades y vacíos de diseño, el SEI propone un marco formal compuesto estricta y exactamente por seis partes:
 * Fuente del Estímulo (Source of Stimulus): La entidad (interna o externa) que genera la condición o el evento. Puede ser un usuario humano, un componente interno, un sensor, un atacante cibernético o un sistema externo.
 * Estímulo (Stimulus): La condición o el evento de activación que arriba al sistema y requiere una respuesta. Ejemplos: una petición HTTP, un mensaje inesperado, la falla de un procesador o un intento de acceso no autorizado.
 * Artefacto (Artifact): El elemento, subsistema, interfaz o proceso específico que recibe el estímulo o que se ve directamente impactado por él.
 * Entorno (Environment): El estado operativo y las condiciones bajo las cuales ocurre el estímulo. Incluye modos como operación normal, horas pico, modo degradado, proceso de despliegue, recuperación tras falla o sobrecarga de red.
 * Respuesta (Response): La actividad o el comportamiento directo que debe llevar a cabo el artefacto o el sistema tras el impacto del estímulo. Ejemplos: conmutar a un servidor de respaldo, registrar una traza de auditoría, procesar la transacción o degradar funcionalidades no esenciales.
 * Medida de la Respuesta (Response Measure): La métrica cuantitativa, técnica, objetiva y medible con la que se determina si la respuesta del sistema satisface los requerimientos de calidad.
Taxonomía de Métricas y Estímulos Estándar
| Atributo de Calidad | Fuente típica del Estímulo | Estímulo típico | Artefactos impactados | Entornos típicos | Respuestas del Sistema | Medidas de Respuesta Estándar |
|---|---|---|---|---|---|---|
| Disponibilidad | Controlador interno, hardware, red, proceso externo | Falla de HW/SW, excepción no capturada, mensaje no anticipado | Procesos, base de datos, canales de comunicación, controladores | Operación normal, failover activo, sobrecarga de red | Aislar falla, conmutar a backup, notificar al operador, reiniciar servicio | MTBF, MTTR, RTO, RPO, tiempo de recuperación, % de uptime |
| Rendimiento | Usuarios concurrentes, temporizadores, eventos de temporizador, sistemas externos | Peticiones HTTP, llegada de mensajes de eventos, ráfagas de datos | Servicios API, colas de mensajes, motores de cálculo | Carga pico, carga nominal, procesamiento de fin de mes | Procesar peticiones, encolar eventos, escalar workers, responder resultados | Latencia promedio/percentil (p95/p99), throughput (TPS), tiempo de respuesta |
| Modificabilidad | Desarrolladores, arquitectos, cambios regulatorios, clientes | Solicitud de nueva funcionalidad, refactorización, cambio de contrato API | Módulos de código, esquemas de BD, archivos de configuración | Tiempo de desarrollo, fase de mantenimiento, integración continua | Aislar el cambio, actualizar código sin romper interfaces, compilar y desplegar | Horas/hombre dedicadas, líneas de código alteradas, cantidad de módulos afectados, costo de cambio |
| Seguridad | Atacantes no autorizados, usuarios maliciosos, procesos infectados | Inyección SQL, desbordamiento de búfer, escaneo de puertos, acceso indebido | Puertas de enlace (API Gateways), BD, componentes de autenticación | Red pública, red corporativa, canal comprometido | Autenticar, auditar eventos, bloquear IP, restaurar datos correctos | % de ataques bloqueados, tiempo de detección, tiempo de restauración de datos, latencia de auditoría |
| Escalabilidad | Nuevas líneas de negocio, incrementos masivos de usuarios o dispositivos | Aumento en volumen de datos, incremento en conexiones concurrentes | Clúster de cómputo, almacenamiento de BD, balanceadores de carga | Crecimiento proyectado del negocio, picos estacionales de tráfico | Adición horizontal de nodos de infraestructura sin alterar código | Cantidad de nodos añadidos por incremento de demanda, capacidad máxima de datos manejados, degradación de throughput |
| Testabilidad | Testers, suites de CI/CD, desarrolladores | Ejecución de pruebas unitarias/integración, inyección de fallas | Módulos de software, componentes de integración, interfaces publicas | Fase de build, despliegue en staging, pruebas de integración | Generar salidas observables, simular dependencias externas mediante stubs/mocks | Cobertura de código (%), tiempo de ejecución de suite de pruebas, capacidad de observar estados internos |
2. Metodología de Auditoría y Completitud de Escenarios
Errores y Omitidos Frecuentes
 * Ambigüedad en la Medida de la Respuesta: Uso de términos cualitativos como "el sistema debe responder rápido", "debe ser altamente seguro" o "minimizar las fallas", en lugar de métricas cuantificables.
 * Falta de Definición del Entorno: Redactar la respuesta sin especificar el estado del sistema (ejemplo: asumir que el sistema está sin carga cuando en realidad el problema ocurre en horas pico).
 * Confusión entre Estímulo y Respuesta: Mezclar el evento de entrada con la acción que toma el sistema para procesarlo.
 * Artefacto Omiso o Abstracto: Mencionar "el sistema" completo en lugar de acotar el componente o módulo afectado.
Algoritmo Sistemático de Revisión de Escenarios
INICIO Algoritmo Auditoria_Escenario(Texto_Escenario)

  1. Extraer entidades del texto mediante mapeo sintáctico-semántico:
     - Fuente = Identificar sujeto que genera el evento.
     - Estímulo = Identificar el evento o condición de entrada.
     - Artefacto = Identificar el módulo, proceso o componente impactado.
     - Entorno = Identificar el estado del sistema durante el evento.
     - Respuesta = Identificar la acción realizada por el artefacto.
     - Medida_Respuesta = Identificar el criterio o métrica de éxito.

  2. Evaluar la completitud:
     PARA CADA Componente EN [Fuente, Estímulo, Artefacto, Entorno, Respuesta, Medida_Respuesta]:
       SI Componente ESTÁ AUSENTE O ES VAGO ("rápido", "adecuado"):
         Marcar Componente como DEFICIENTE.
       FIN SI
     FIN PARA

  3. Aplicar Reglas de Inferencia Segura si hay deficiencias:
     - SI Entorno es AUSENTE: Inferir "Operación Normal" basándose en el contexto operativo típico.
     - SI Fuente es AUSENTE: Inferir la fuente estándar del Estímulo (ej. si el Estímulo es "Petición HTTP", la Fuente es "Usuario Externo").
     - SI Artefacto es VAGO ("El sistema"): Mapear al subsistema que expone la interfaz de entrada (ej. "API Gateway" o "Módulo de Autenticación").
     - SI Medida_Respuesta es VAGA o AUSENTE: Proponer métricas estándar concretas basadas en el Atributo de Calidad detectado (ej. "Latencia < 200 ms en p95" para Rendimiento).

  4. Generar Escenario Formal Auditorado de 6 Partes.

FIN Algoritmo

3. Arquitectura del Árbol de Utilidad (Utility Tree)
El Árbol de Utilidad es la herramienta del marco ATAM (Architecture Tradeoff Analysis Method) del SEI para priorizar y estructurar los requerimientos de atributos de calidad del sistema.
                                  [ UTILIDAD ]
                                       |
    +----------------------------------+----------------------------------+
    | |
[Atributo 1: Rendimiento] [Atributo 2: Disponibilidad]
    | |
    +--------------------------+ +--------------------------+
    | | | |
(Sub-atrib: Latencia) (Sub-atrib: Throughput) (Sub-atrib: Fallo HW) (Sub-atrib: Red)
    | | | |
[Escenario 1.1] [Escenario 1.2] [Escenario 2.1] [Escenario 2.2]
  (H, H) (M, H) (H, M) (L, L)

Estructura Jerárquica Exacta
 * Utilidad: Nodo raíz universal que representa el valor global o la salud operacional y técnica del sistema.
 * Atributo de Calidad: Las propiedades generales de alto nivel (Rendimiento, Disponibilidad, Seguridad, Modificabilidad, etc.).
 * Categoría / Sub-atributo: Sub-clasificación específica del atributo (ej. dentro de Rendimiento: Latencia en pico o Throughput de datos; en Disponibilidad: Fallas de Software o Fallas de Red).
 * Escenario Especificado: El escenario concreto de 6 partes enlazado a su prioridad.
Matriz de Priorización del SEI
Cada escenario de hoja en el árbol recibe una tupla de ordenamiento (Importancia para el Negocio, Dificultad/Riesgo Arquitectónico) usando los valores High (H), Medium (M) y Low (L):
 * Importancia para el Negocio: Determinada por el Product Owner o los Stakeholders del negocio. Mide el impacto en el éxito comercial u operacional si el escenario no se satisface.
 * Dificultad o Riesgo Arquitectónico: Determinada por el Arquitecto de Software. Evalúa la complejidad técnica, la incertidumbre o el esfuerzo que requiere diseñar la arquitectura para satisfacer dicho escenario.
EJE 2: Arquitectura y Patrones para la Creación de Skills (Antigravity / Claude Style)
1. Principios de Diseño de Skills
Las Skills para modelos de lenguaje operan como módulos de capacidad invocables o activables semánticamente.
Encabezado YAML (SKILL.md)
El archivo principal de la skill debe configurarse mediante un bloque de encabezado YAML estructurado de la siguiente forma:
---
name: nombre-de-la-skill
description: |
  Descripción clara y semánticamente densa que explica EXACTAMENTE cuándo activar
  esta skill. Debe incluir palabras clave, disparadores explícitos y casos de uso.
---

 * Activación Semántica (Skill Triggering): La sección description es evaluada por el LLM para decidir cuándo activar la skill. Debe contener verbos de acción, contextos específicos de arquitectura de software y términos técnicos (ej. "escenarios SEI", "árbol de utilidad", "6 partes", "ATAM").
Patrones de Prompting para Agentes
 * Bucles de Autoverificación (Self-Verification): Obligar al modelo a ejecutar un paso intermedio donde verifique su propia salida contra las reglas del negocio antes de emitir la respuesta final.
 * Restricciones Negativas (Negative Constraints): Definir explícitamente lo que el agente NO debe hacer (ej. "NUNCA omitas el entorno en un escenario", "NO uses adjetivos cualitativos como 'rápido' en las medidas de respuesta").
 * Formateo Estructurado: Especificar esquemas de formato estricto (Markdown o JSON) para evitar variaciones no deseadas en las respuestas del ejecutor.
2. Estrategia de Documentos de Referencia (references/)
Para mantener el contexto principal del LLM limpio y enfocado en la ejecución inmediata del prompt, la información de soporte detallada debe organizarse modularmente dentro de una carpeta references/:
my-skill/
├── SKILL.md
└── references/
    ├── sei-taxonomy.md
    ├── audit-rules.md
    └── utility-tree-schema.md

 * Carga Bajo Demanda: La skill invocará el contenido de references/ únicamente cuando el escenario lo requiera, evitando la saturación de tokens y el fenómeno de "pérdida en el medio" (lost in the middle).
 * Aislamiento de Responsabilidades: SKILL.md contiene las instrucciones y reglas de ejecución directa del agente, mientras que references/ almacena la base de conocimiento extendida (taxonomías, esquemas y tablas formales).
EJE 3: Blueprint para la Implementación de Skills
1. Especificación de las 3 Skills
Skill 1: sei-scenario-generator
 * Propósito: Transformar requerimientos funcionales o descripciones informales del usuario en escenarios formales de atributos de calidad del SEI de 6 partes.
 * Reglas de Negocio:
   * Identificar el atributo de calidad latente en el texto informal.
   * Parsear o inferir cada una de las 6 partes: Fuente, Estímulo, Artefacto, Entorno, Respuesta y Medida de Respuesta.
   * Si la medida de respuesta es vaga, convertirla obligatoriamente a unidades técnicas cuantificables (ms, TPS, MTBF, %, Horas/Hombre).
 * Formato de Salida Obligatorio: Bloque Markdown con las 6 partes tabuladas o listadas de forma estructurada.
Skill 2: sei-scenario-checker
 * Propósito: Auditar, validar y completar escenarios de calidad provistos por el usuario.
 * Protocolo de Evaluación:
   * Analizar el escenario provisto e identificar faltantes o componentes ambiguos.
   * Generar un informe de deficiencias encontradas.
   * Invocando las Reglas de Inferencia Segura, reescribir y entregar la versión completamente corregida y enriquecida del escenario.
Skill 3: sei-utility-tree-builder
 * Propósito: Analizar un conjunto de requerimientos o escenarios del sistema y construir la estructura jerárquica del Árbol de Utilidad asignando la matriz de prioridades.
 * Algoritmo de Extracción e Integración:
   * Identificar la Utilidad Central del sistema.
   * Mapear los escenarios a los Atributos de Calidad y Sub-atributos correspondientes.
   * Evaluar la Importancia para el Negocio y el Riesgo Arquitectónico determinando tuplas (H/M/L, H/M/L) para cada escenario.
   * Rendir el árbol jerárquico final en Markdown.
2. Diseño de la Suite de Pruebas (Test Cases)
Caso de Prueba 1: E-Commerce bajo Eventos de Alta Concurrencia
 * Atributos Evaluados: Rendimiento / Escalabilidad.
 * Entrada Informal: "Durante el Black Friday, cuando entren miles de usuarios a comprar al mismo tiempo, el proceso de pago no se tiene que caer y debe procesar los cobros rápido."
 * Resultado Esperado (Escenario Generado de 6 Partes):
   * Fuente del Estímulo: Clientes concurrentes en plataforma.
   * Estímulo: Solicitud masiva de procesamiento de órdenes de pago durante pico de ventas.
   * Artefacto: Pasarela de Pagos y Servicio de Transacciones.
   * Entorno: Evento de Alta Concurrencia (Black Friday) / Carga Pico de Tráfico.
   * Respuesta: Procesar pagos de forma asíncrona y escalar horizontalmente las instancias de cobro.
   * Medida de la Respuesta: Latencia p95 < 1.5 segundos; throughput sostenido de 5,000 TPS; 0% de transacciones caídas o no procesadas.
Caso de Prueba 2: Escenario Incompleto en Sistema Bancario (Prueba de Auditoría)
 * Atributos Evaluados: Seguridad / Disponibilidad.
 * Entrada Deficiente: "Un hacker intenta hacer transacciones falsas pero el sistema bancario lo detecta y no se cae."
 * Deficiencias Identificadas por sei-scenario-checker:
   * Artefacto: No especificado ("el sistema bancario" es abstracto).
   * Entorno: Ausente.
   * Medida de la Respuesta: Vaga ("no se cae").
 * Resultado Correctivo Inferred:
   * Fuente del Estímulo: Atacante no autorizado externo.
   * Estímulo: Intento de inyección de transacciones no autenticadas.
   * Artefacto: Core Bancario y API Gateway de Transacciones.
   * Entorno: Operación Nominal.
   * Respuesta: Rechazar la transacción, bloquear la dirección IP del origen y generar alerta de seguridad.
   * Medida de la Respuesta: 100% de los intentos no autorizados bloqueados; registro de auditoría creado en menos de 50 ms; disponibilidad del servicio mantenida al 99.999% sin caídas.
Caso de Prueba 3: Dominio Complejo de Telemedicina (Construcción del Árbol de Utilidad)
 * Atributos Evaluados: Rendimiento, Disponibilidad, Seguridad, Modificabilidad.
 * Entrada de Dominio: Requerimientos de una plataforma de telemedicina crítica con transmisión de señales de vitales en tiempo real, integración con historia clínica y cambios de regulaciones sanitarias.
 * Resultado Esperado (Árbol de Utilidad Construido):
* UTILIDAD (Plataforma de Telemedicina Crítica)[span_79](start_span)[span_79](end_span)
  ├── Rendimiento[span_80](start_span)[span_80](end_span)
  │ └── Latencia de Transmisión en Tiempo Real[span_81](start_span)[span_81](end_span)
  │ └── Transmisión de ECG: Durante videollamada, la señal del ECG debe reflejarse en la pantalla del médico con latencia < 200 ms. (H, H)[span_82](start_span)[span_82](end_span)
  ├── Disponibilidad[span_83](start_span)[span_83](end_span)
  │ └── Resiliencia del Servicio de Consulta[span_84](start_span)[span_84](end_span)
  │ └── Falla de Servidor de Video: Durante una consulta activa, si el servidor de video falla, se reconecta en < 3 segundos. (H, M)[span_85](start_span)[span_85](end_span)
  ├── Seguridad[span_86](start_span)[span_86](end_span)
  │ └── Confidencialidad e Integridad de Datos[span_87](start_span)[span_87](end_span)
  │ └── Acceso no autorizado: Intento de extracción de Historias Clínicas interceptado y encriptado al 100%. (H, H)[span_88](start_span)[span_88](end_span)
  └── Modificabilidad[span_89](start_span)[span_89](end_span)
      └── Adaptación Regulatoria[span_90](start_span)[span_90](end_span)
          └── Cambio de Ley de Datos Sanitarios: Agregar nuevo estándar de cifrado en el módulo de almacenamiento en < 40 horas/hombre. (M, L)[span_91](start_span)[span_91](end_span)
