# Ejemplos de Escenarios SEI y Auditorías

Este archivo contiene ejemplos de referencia para la formulación de escenarios según el SEI y casos prácticos de auditoría (escenario incompleto vs. completado).

---

## 1. Ejemplos de Escenarios Completos por Atributo de Calidad

### Rendimiento (Performance)
* **Fuente:** Clientes concurrentes externos.
* **Estímulo:** Envían 5.000 solicitudes de búsqueda por segundo.
* **Artefacto:** Servicio de catálogo y búsqueda.
* **Entorno:** Operación en horario pico comercial.
* **Respuesta:** El sistema encola y procesa las consultas devolviendo los resultados paginados.
* **Medida de respuesta:** El percentil 95 (p95) de tiempo de respuesta es $\le 300\text{ ms}$, con una tasa de error inferior al $0.01\%$.

### Disponibilidad (Availability)
* **Fuente:** Servidor de base de datos primario.
* **Estímulo:** Falla de hardware no anticipada (caída total de la instancia).
* **Artefacto:** Capa de persistencia de datos.
* **Entorno:** Operación normal de producción.
* **Respuesta:** El orquestador detecta la falta de heartbeat, promueve la réplica secundaria a primaria y reconfigura los endpoints de conexión.
* **Medida de respuesta:** Tiempo de detección $\le 10\text{ segundos}$, tiempo total de indisponibilidad (RTO) $\le 30\text{ segundos}$, sin pérdida de datos confirmados ($\text{RPO} = 0$).

### Modificabilidad (Modifiability)
* **Fuente:** Desarrollador del equipo.
* **Estímulo:** Requerimiento de incorporar una nueva pasarela de pago (ej. Stripe).
* **Artefacto:** Módulo de procesamiento de pagos.
* **Entorno:** Tiempo de desarrollo / mantenimiento.
* **Respuesta:** El desarrollador implementa la interfaz adaptadora existente sin alterar el motor central de órdenes ni la lógica de facturación.
* **Medida de respuesta:** El cambio se completa y despliega a pruebas en menos de 16 horas-persona y no requiere modificar más de 3 clases existentes.

### Seguridad (Security)
* **Fuente:** Atacante externo no autenticado.
* **Estímulo:** Envío masivo de peticiones malformadas con inyecciones SQL y payloads maliciosos.
* **Artefacto:** API Gateway y servicio de autenticación.
* **Entorno:** En línea, conectado a Internet.
* **Respuesta:** El WAF y los filtros de entrada detectan el patrón malicioso, bloquean la IP origen temporalmente, rechazan la petición y registran un evento en el log de auditoría de seguridad.
* **Medida de respuesta:** El $100\%$ de los intentos son bloqueados antes de alcanzar la capa de base de datos; el registro de auditoría se almacena en menos de $500\text{ ms}$ y la IP queda vetada por 30 minutos.

---

## 2. Caso Práctico de Auditoría: Incompleto vs. Completado

### Escenario Inicial Provisto (Incompleto)
> *"El sistema debe responder rápido cuando un usuario busca un producto, incluso si hay mucha gente conectada."*

### Auditoría de Completitud
1. **Fuente:** Vago (*"un usuario"* -> ¿Cliente web, móvil, bot?).
2. **Estímulo:** Impreciso (*"busca un producto"* -> ¿Qué volumen de búsqueda? ¿Con filtros complejos?).
3. **Artefacto:** Genérico (*"El sistema"* -> ¿Qué componente específico responde?).
4. **Entorno:** Subjetivo (*"mucha gente conectada"* -> ¿Cuántos usuarios concurrentes?).
5. **Respuesta:** Parcial (*"responder"* -> ¿Qué entrega la respuesta?).
6. **Medida de respuesta:** **Ausente / Ambigua** (*"rápido"* no es una métrica medible).

### Escenario Completado (SEI 6 Partes)
| Parte | Detalle |
| :--- | :--- |
| **Fuente del estímulo** | Usuario final autenticado navegando desde la app móvil o web. |
| **Estímulo** | Ejecuta una consulta de búsqueda de productos con filtros de categoría y precio. |
| **Artefacto** | Motor de búsqueda del microservicio de catálogo. |
| **Entorno** | Pico de tráfico estacional (ej. CyberMonday) con 10.000 usuarios concurrentes y 1.500 búsquedas/segundo. |
| **Respuesta** | El sistema procesa la búsqueda, aplica los filtros, ordena los resultados y los retorna serializados en JSON. |
| **Medida de respuesta** | Latencia de respuesta $\le 400\text{ ms}$ en el percentil 95 (p95), uso de CPU del nodo $\le 75\%$, tasa de disponibilidad del servicio del $99.9\%$. |
