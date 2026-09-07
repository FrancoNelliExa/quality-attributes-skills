# Reglas de Auditoría y Algoritmo de Completitud de Escenarios SEI

Este documento establece la metodología formal y el algoritmo de inferencia para auditar escenarios de atributos de calidad, identificar deficiencias y transformarlos en especificaciones arquitectónicas completas de 6 partes según el Software Engineering Institute (SEI).

---

## 1. Catálogo de Errores y Omisiones Frecuentes

Durante la especificación de requerimientos de arquitectura, suelen presentarse cuatro patrones de defecto recurrentes:

### 1.1 Ambigüedad en la Medida de la Respuesta
* **Defecto:** Emplear calificativos subjetivos o vagos (*"el sistema debe ser rápido"*, *"garantizar alta disponibilidad"*, *"responder de forma segura"*, *"minimizar los errores"*).
* **Impacto Arquitectónico:** Impide verificar o falsificar el cumplimiento del requerimiento mediante pruebas de carga o benchmarks. No proporciona criterios de aceptación claros para los tradeoffs de diseño.
* **Solución:** Reemplazar por unidades físicas cuantificables y verificables: tiempo en milisegundos/segundos (especificando percentil p95 o p99), transacciones por segundo (TPS), porcentaje de uptime (ej. 99.99%), horas-hombre de modificación, o porcentaje de amenazas mitigadas.

### 1.2 Omisión o Ambigüedad del Entorno
* **Defecto:** Describir el comportamiento sin indicar el estado operativo del sistema (*"cuando un usuario se loguea..."*).
* **Impacto Arquitectónico:** Una respuesta admisible en operación nominal puede ser inaceptable durante un pico de demanda masivo (ej. CyberMonday) o durante una degradación por conmutación por error (failover).
* **Solución:** Explicitar el estado operacional: operación normal, horas pico de tráfico, modo degradado, durante despliegue con cero tiempo de inactividad (*zero-downtime deployment*), o fase de recuperación tras desastre.

### 1.3 Confusión entre Estímulo y Respuesta
* **Defecto:** Intercambiar la causa detonante con la acción que toma el sistema (ej. definir como estímulo *"el sistema conmuta al servidor secundario"* cuando en realidad ese comportamiento es la respuesta ante el estímulo *"falla del servidor primario"*).
* **Impacto Arquitectónico:** Invierte la causalidad arquitectónica y distorsiona la selección de tácticas.
* **Solución:** Separar estrictamente la condición de entrada exógena o falla (Estímulo) de la reacción observable del artefacto (Respuesta).

### 1.4 Artefacto Omiso o Hiper-Genérico
* **Defecto:** Referirse a *"el sistema"* o *"la plataforma"* sin acotar la frontera arquitectónica.
* **Impacto Arquitectónico:** Imposibilita asignar responsabilidades a un módulo, servicio o subsistema específico, diluyendo el alcance del diseño y de las pruebas.
* **Solución:** Individualizar el componente impactado: *API Gateway*, *Servicio de Pagos*, *Capa de Persistencia de Órdenes*, *Broker de Eventos*, *Módulo de Autenticación*.

---

## 2. Algoritmo Sistemático de Auditoría

Para auditar un texto provisto por el usuario, se debe aplicar secuencialmente el siguiente algoritmo:

```text
INICIO Algoritmo Auditoria_Escenario(Texto_Escenario)

  1. EXTRACCIÓN SINTÁCTICO-SEMÁNTICA:
     - Fuente           <- Identificar sujeto o entidad generadora.
     - Estímulo         <- Identificar el evento desencadenante o condición.
     - Artefacto        <- Identificar el componente, servicio o módulo receptor.
     - Entorno          <- Identificar el estado operativo del sistema.
     - Respuesta        <- Identificar la acción o táctica reactiva observable.
     - Medida_Respuesta <- Identificar la métrica objetiva de éxito.

  2. EVALUACIÓN DE COMPLETITUD Y CALIDAD:
     PARA CADA Dimensión EN [Fuente, Estímulo, Artefacto, Entorno, Respuesta, Medida_Respuesta]:
       SI Dimensión no está presente:
         Estado(Dimensión) <- ❌ AUSENTE
       SINO SI Dimensión contiene términos vagos ("rápido", "robusto", "el sistema", "seguro"):
         Estado(Dimensión) <- ⚠️ AMBIGUO / DEFICIENTE
       SINO:
         Estado(Dimensión) <- ✅ COMPLETO
       FIN SI
     FIN PARA

  3. APLICACIÓN DE REGLAS DE INFERENCIA SEGURA:
     - SI Entorno es AUSENTE o VAGO:
         Inferir "Operación Normal / Producción Estable" o el contexto inferible del estímulo.
     - SI Fuente es AUSENTE:
         Inferir el actor o componente canónico causante del estímulo según taxonomía SEI.
     - SI Artefacto es "El sistema" o AUSENTE:
         Mapear al subsistema que actúa como punto de entrada o procesador de la interacción.
     - SI Medida_Respuesta es VAGA o AUSENTE:
         Proponer métrica estándar de la industria vinculada al atributo de calidad inferido.

  4. GENERACIÓN DE ESPECIFICACIÓN FORMAL AUDITADA:
     - Emitir el informe diagnóstico (Checklist con iconos de estado).
     - Justificar técnicamente las observaciones.
     - Proporcionar la versión corregida y completada en tabla formal y narrativa.

FIN Algoritmo
```

---

## 3. Catálogo de Reglas de Inferencia Segura

Cuando un escenario contenga partes ausentes o ambiguas, el agente aplicará las siguientes reglas predeterminadas:

| Dimensión Afectada | Estado Detectado | Regla de Inferencia Segura |
| :--- | :--- | :--- |
| **Fuente del Estímulo** | Ausente | Si el estímulo es una petición de usuario $\rightarrow$ *"Usuario final autenticado"* o *"Cliente web/móvil"*. Si es una falla de nodo $\rightarrow$ *"Infraestructura física/virtual subyacente o watchdog del cluster"*. Si es un ciberataque $\rightarrow$ *"Atacante externo no autenticado"*. |
| **Artefacto** | Vago (*"el sistema"*) | Identificar la frontera: Si es tráfico entrante $\rightarrow$ *"API Gateway y Reverse Proxy"*. Si es persistencia $\rightarrow$ *"Cluster de Base de Datos relacional/NoSQL"*. Si es procesamiento de negocio $\rightarrow$ *"Microservicio de Dominio correspondiente"*. |
| **Entorno** | Ausente | Asumir por defecto: *"Operación normal en régimen de producción nominal"*. Si el estímulo menciona *"muchos usuarios"* o *"evento especial"* $\rightarrow$ *"Pico estacional de tráfico (ej. CyberMonday) a máxima carga proyectada"*. |
| **Respuesta** | Genérica (*"funciona"*) | Traducir a táctica SEI observable: aislar componente, conmutar a respaldo (*failover*), encolar peticiones, devolver respuesta cacheada, registrar traza de auditoría. |
| **Medida de la Respuesta** | Vaga (*"rápido"*) | **Rendimiento:** Latencia $\text{p95} \le 200\text{ ms}$; Throughput $\ge 1.000\text{ TPS}$.<br>**Disponibilidad:** Uptime $\ge 99.99\%$; RTO $\le 30\text{ s}$; RPO $= 0$.<br>**Safety:** Transición a modo/sensor seguro en $\le 300\text{ ms}$; 0 lesiones, víctimas o violaciones de umbrales letales.<br>**Integrabilidad:** Integración de componente externo en $\le 1\text{ mes}$ con $\le 1\text{ persona-mes}$ de esfuerzo.<br>**Desplegabilidad:** Despliegue en $\le 40\text{ h}$ de tiempo transcurrido; esfuerzo $\le 120\text{ horas-persona}$; 0 defectos introducidos; 0 violaciones de SLA; rollback en $\le 3\text{ min}$.<br>**Seguridad:** $100\%$ de ataques mitigados; registro de auditoría en $\le 50\text{ ms}$.<br>**Modificabilidad:** Implementación y pruebas de código en $\le 16\text{ horas-persona}$ sin alterar interfaces públicas. |

---

## 4. Estructura del Informe de Auditoría

El resultado de auditar un escenario debe organizarse siempre en tres bloques:

1. **Diagnóstico de Completitud:** Checklist de 6 filas con estados:
   * ✅ **Completo:** La parte está explícita, delimitada y sin ambigüedades.
   * ⚠️ **Ambiguo / Parcial:** La parte se menciona pero carece de precisión técnica.
   * ❌ **Ausente:** La parte no fue contemplada en el texto original.
2. **Justificación Técnica:** Explicación concisa de las deficiencias y riesgos arquitectónicos identificados.
3. **Escenario Corregido y Formalizado:** Presentación del escenario completado mediante la aplicación de las reglas de inferencia segura, tanto en formato tabular como narrativo.
