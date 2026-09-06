# Template de Escenarios de Atributos de Calidad (SEI)

Según el Software Engineering Institute (SEI) y la metodología descrita en *Software Architecture in Practice* (Bass, Clements, Kazman), un escenario de atributo de calidad consta de seis partes fundamentales:

---

## Las 6 Partes del Escenario SEI

| Parte | Nombre en Español | Nombre en Inglés | Descripción | Pregunta Clave para Validar |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Fuente del estímulo** | *Source of stimulus* | La entidad o actor que genera el estímulo (humano, sistema externo, falla de hardware, atacante, etc.). | ¿Quién o qué origina el evento? |
| 2 | **Estímulo** | *Stimulus* | La condición o evento que afecta al sistema y requiere una respuesta (solicitud de usuario, caída de red, intento de intrusión, etc.). | ¿Qué evento o condición ocurre? |
| 3 | **Artefacto** | *Artifact* | La parte del sistema o el sistema completo que es estimulado (un servicio, una base de datos, la interfaz web, el sistema entero). | ¿Qué componente o subsistema recibe el estímulo? |
| 4 | **Entorno / Ambiente** | *Environment* | Las condiciones operacionales bajo las cuales ocurre el estímulo (operación normal, alta carga, modo degradado, durante despliegue, recuperación de desastre). | ¿En qué estado u condiciones operativas se encuentra el sistema? |
| 5 | **Respuesta** | *Response* | La actividad o comportamiento que el sistema ejecuta como consecuencia del estímulo (procesar la solicitud, registrar auditoría, aislar falla, cambiar a réplica). | ¿Qué acciones realiza el sistema ante el estímulo? |
| 6 | **Medida de respuesta** | *Response measure* | Métrica cuantificable y verificable de la respuesta (latencia en ms, porcentaje de disponibilidad, tiempo de recuperación RTO, tasa de error). | ¿Cómo se mide objetivamente si la respuesta fue exitosa? |

---

## Criterios de Completitud y Auditoría

Al analizar un escenario provisto por el usuario, verificar exhaustivamente cada una de las 6 partes:

1. **¿Están presentes las 6 partes explícitamente?**
   - Si falta alguna, señalar claramente cuál es (ej. *"Falta la Medida de Respuesta"* o *"El Entorno no está definido"*).
2. **¿Es la medida de respuesta medible y no ambigua?**
   - Evitar términos vagos como *"rápidamente"*, *"fácilmente"*, *"de forma segura"*, *"sin problemas"*.
   - Exigir unidades: segundos/milisegundos, porcentaje de uptime (ej. 99.9%), cantidad de personas-hora requeridas, transacciones por segundo (TPS).
3. **¿El artefacto está delimitado adecuadamente?**
   - Diferenciar entre el sistema completo y un módulo específico si la respuesta corresponde a una parte arquitectónica particular.
4. **¿La fuente y el estímulo están diferenciados?**
   - Errores comunes confunden la fuente (ej. "usuario autenticado") con el estímulo (ej. "solicita reporte mensual").

---

## Formato de Presentación Estándar

Al generar o completar un escenario, presentar dos formatos:

### 1. Formato Tabular (Estructurado)
```markdown
| Parte | Detalle del Escenario |
| :--- | :--- |
| **Fuente del estímulo** | ... |
| **Estímulo** | ... |
| **Artefacto** | ... |
| **Entorno** | ... |
| **Respuesta** | ... |
| **Medida de respuesta** | ... |
```

### 2. Formato Narrativo Conciso
> *"[Fuente] genera [Estímulo] en [Artefacto] bajo [Entorno]. El sistema [Respuesta] logrando [Medida de respuesta]."*
