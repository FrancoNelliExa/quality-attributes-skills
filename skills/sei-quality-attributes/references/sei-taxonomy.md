# Taxonomía Formal de Atributos de Calidad (SEI)

Este documento detalla la taxonomía de atributos de calidad según el Software Engineering Institute (SEI) y el marco de Bass, Clements y Kazman (*Software Architecture in Practice*). Sirve como base de conocimiento para la formulación, inferencia y validación de escenarios de calidad de 6 partes.

---

## 1. Definición del Framework de 6 Partes

Cada escenario de atributo de calidad debe especificar estrictamente las siguientes 6 dimensiones:

| Dimensión | Nombre en Inglés | Definición Formal |
| :--- | :--- | :--- |
| **Fuente del Estímulo** | *Source of Stimulus* | La entidad (humana, de software, de hardware o externa) que genera el evento o condición de entrada. |
| **Estímulo** | *Stimulus* | La condición o evento que arriba al sistema y requiere una respuesta arquitectónica. |
| **Artefacto** | *Artifact* | El elemento, subsistema, servicio, componente o proceso específico directamente impactado por el estímulo. |
| **Entorno** | *Environment* | El estado operacional y condiciones bajo las cuales ocurre el estímulo (carga normal, horas pico, modo degradado, despliegue, recuperación). |
| **Respuesta** | *Response* | La actividad, comportamiento o táctica arquitectónica que ejecuta el artefacto o sistema tras recibir el estímulo. |
| **Medida de la Respuesta** | *Response Measure* | Métrica cuantitativa, objetiva y técnicamente verificable que determina el éxito de la respuesta (latencia, throughput, disponibilidad, tiempo de cambio, etc.). |

---

## 2. Catálogo Taxonómico por Atributo de Calidad

### 2.1 Disponibilidad (Availability)
Capacidad del sistema de permanecer operativo y accesible ante la ocurrencia de fallas o eventos imprevistos.

* **Fuentes Típicas:** Componente interno (memoria, disco, proceso), controlador de red, servidor físico/virtual, proceso externo, proveedor cloud.
* **Estímulos Típicos:** Falla de hardware (caída de nodo), caída de conexión de base de datos, excepción no capturada, timeout de servicio tercero, corrupción de datos.
* **Artefactos Impactados:** Capa de persistencia, microservicios, colas de mensajes, API Gateway, balanceadores de carga.
* **Entornos Típicos:** Operación normal, tráfico pico, proceso de conmutación (failover), modo degradado, ventana de mantenimiento.
* **Respuestas del Sistema (Tácticas):** Detectar falla (heartbeat, ping/echo), aislar componente dañado, conmutar a réplica pasiva/activa, reintentar con backoff exponencial, degradar servicio no crítico, registrar alerta de monitoreo.
* **Medidas de Respuesta Estándar:**
  * **Uptime / Porcentaje de Disponibilidad:** $\ge 99.9\%$ ("tres nueves"), $\ge 99.99\%$ ("cuatro nueves"), $\ge 99.999\%$ ("cinco nueves").
  * **MTBF (Mean Time Between Failures):** $> 720\text{ horas}$.
  * **MTTR (Mean Time To Repair) / Tiempo de Recuperación:** $\le 30\text{ segundos}$ en failover automático; $\le 15\text{ minutos}$ en intervención manual.
  * **RTO (Recovery Time Objective):** Tiempo máximo admisible de inactividad (ej. $\le 2\text{ minutos}$).
  * **RPO (Recovery Point Objective):** Pérdida admisible de datos (ej. $0\text{ segundos}$, transacciones confirmadas intactas).

---

### 2.2 Rendimiento (Performance)
Capacidad del sistema de procesar solicitudes y eventos dentro de límites temporales y de utilización de recursos determinados.

* **Fuentes Típicas:** Usuarios concurrentes, clientes móviles/web, temporizadores periódicos (cron jobs), flujos de eventos asíncronos, sensores IoT.
* **Estímulos Típicos:** Ráfagas de peticiones HTTP, lote masivo de transacciones, llegada continua de telemetría, consultas complejas a bases de datos.
* **Artefactos Impactados:** Capa de APIs, controladores, servicios de cálculo, motor de búsqueda, índices de base de datos, colas.
* **Entornos Típicos:** Operación nominal, horario comercial pico, evento extraordinario (CyberMonday, Black Friday), procesamiento de cierre mensual.
* **Respuestas del Sistema (Tácticas):** Controlar demanda de recursos (rate limiting, debouncing), optimizar algoritmos, paralelizar ejecución, cachear resultados (Redis/Memcached), encolar peticiones asíncronas, escalar workers.
* **Medidas de Respuesta Estándar:**
  * **Latencia / Tiempo de Respuesta:** Promedio $\le 150\text{ ms}$; Percentil 95 (p95) $\le 300\text{ ms}$; Percentil 99 (p99) $\le 800\text{ ms}$.
  * **Throughput / Rendimiento Transaccional:** $\ge 2.500\text{ TPS}$ (transacciones por segundo); $\ge 10.000\text{ RPM}$ (requests per minute).
  * **Jitter (varianza de retardo):** $\le 10\text{ ms}$ en transmisión de video o audio en tiempo real.
  * **Utilización de Recursos:** Uso de CPU $\le 70\%$, consumo de memoria RAM $\le 80\%$.

---

### 2.3 Modificabilidad (Modifiability)
Facilidad y costo con los que el sistema puede evolucionar ante cambios en requerimientos, tecnología o contexto regulatorio.

* **Fuentes Típicas:** Desarrolladores de software, arquitectos, analistas de negocio, reguladores normativos, clientes.
* **Estímulos Típicos:** Solicitud de nueva funcionalidad, refactorización arquitectónica, cambio de protocolo de comunicación, cambio de esquema de BD, integración de nueva pasarela de pago o API externa.
* **Artefactos Impactados:** Módulos de código fuente, interfaces de contratos (OpenAPI/gRPC), esquemas de migración de BD, configuraciones de infraestructura.
* **Entornos Típicos:** Tiempo de desarrollo, ciclo de sprints, fase de mantenimiento evolutivo, pipeline de CI/CD.
* **Respuestas del Sistema (Tácticas):** Encapsular responsabilidades (Single Responsibility), desacoplar dependencias mediante interfaces/inversión de control, usar patrones adaptadores o plugins, parametrizar por configuración.
* **Medidas de Respuesta Estándar:**
  * **Esfuerzo en Tiempo/Persona:** Cambio completado en $\le 16\text{ horas-persona}$ (o $\le 2\text{ días-hombre}$).
  * **Impacto en Módulos:** No más de $2$ clases o archivos modificados; $0$ cambios en contratos de clientes existentes.
  * **Tiempo de Build y Despliegue:** Compilación y tests automatizados en $\le 10\text{ minutos}$.
  * **Costo de Modificación:** Menor a $X$ puntos de historia o costo financiero acotado.

---

### 2.4 Seguridad (Security)
Capacidad del sistema de resistir intentos de uso no autorizado, daño malicioso y denegación de servicio, salvaguardando confidencialidad, integridad y disponibilidad.

* **Fuentes Típicas:** Atacante externo no autenticado, usuario interno malicioso, botnet distribuida, script automatizado de escaneo.
* **Estímulos Típicos:** Intento de inyección SQL, ataque de Cross-Site Scripting (XSS), saturación por Denegación de Servicio Distribuido (DDoS), intento de bypass de autenticación, suplantación de identidad (spoofing).
* **Artefactos Impactados:** API Gateway, proveedor de identidad (IdP), módulo de autenticación y autorización (OAuth2/OIDC), almacén de credenciales, base de datos de usuarios.
* **Entornos Típicos:** Red pública de internet, canal de comunicación expuesto, sistema operando bajo ataque activo.
* **Respuestas del Sistema (Tácticas):** Autenticar actores (MFA), autorizar accesos (RBAC/ABAC), cifrar datos en tránsito (TLS 1.3) y en reposo (AES-256), validar y sanitizar inputs, bloquear IPs atacantes, emitir alertas al SIEM, registrar auditoría inmutable.
* **Medidas de Respuesta Estándar:**
  * **Efectividad de Bloqueo:** $100\%$ de intentos no autorizados bloqueados antes de acceder a datos sensibles.
  * **Tiempo de Detección:** Detección de anomalía e inicio de mitigación en $\le 5\text{ segundos}$.
  * **Auditoría:** Registro de traza de auditoría inmutable generado en $\le 50\text{ ms}$.
  * **Resiliencia:** Disponibilidad del servicio mantenida al $\ge 99.95\%$ durante ataques de hasta $50\text{ Gbps}$.

---

### 2.5 Escalabilidad (Scalability)
Capacidad del sistema de manejar un incremento significativo en el volumen de trabajo (tráfico, conexiones o datos) añadiendo recursos computacionales de forma proporcional.

* **Fuentes Típicas:** Crecimiento masivo de usuarios, expansión a nuevos mercados, campañas de marketing viral, incremento de sensores conectados.
* **Estímulos Típicos:** Aumento sostenido del $300\%$ en solicitudes simultáneas, incremento en volumen de base de datos de $1\text{ TB}$ a $50\text{ TB}$.
* **Artefactos Impactados:** Clúster de Kubernetes, auto-escaladores horizontales (HPA), sharding de bases de datos, brokers de mensajería (Kafka).
* **Entornos Típicos:** Crecimiento proyectado, temporadas altas, expansión geográfica.
* **Respuestas del Sistema (Tácticas):** Autoescalado horizontal de pods/contenedores sin reinicio del cluster, particionamiento de bases de datos (sharding), distribución de lecturas mediante réplicas de lectura.
* **Medidas de Respuesta Estándar:**
  * **Tiempo de Escalado:** Provisión de nuevas instancias operativas en $\le 60\text{ segundos}$ tras cruzar umbral de $75\%$ de CPU.
  * **Linealidad de Rendimiento:** La latencia p95 no se degrada en más de un $10\%$ al cuadruplicar la carga concurrente.
  * **Capacidad Máxima Soportada:** Hasta $100.000$ usuarios simultáneos sin degradación del servicio.

---

### 2.6 Testabilidad (Testability)
Facilidad con la que el software permite descubrir y aislar defectos mediante la ejecución de pruebas automatizadas y la observabilidad de sus estados internos.

* **Fuentes Típicas:** Ingenieros de pruebas (QA), desarrolladores, agentes de integración continua (CI/CD).
* **Estímulos Típicos:** Ejecución de suite de pruebas unitarias/integración, inyección de fallas en pruebas de caos (*chaos engineering*), verificación de cobertura.
* **Artefactos Impactados:** Módulos de código, endpoints de diagnóstico (`/health`, `/metrics`), capas de inyección de dependencias.
* **Entornos Típicos:** Pipeline de CI/CD, entorno de Staging o pruebas de laboratorio.
* **Respuestas del Sistema (Tácticas):** Proveer interfaces observables, desacoplar dependencias para habilitar stubs/mocks, exponer métricas de telemetría (OpenTelemetry), permitir sembrado determinista de estados.
* **Medidas de Respuesta Estándar:**
  * **Cobertura de Código:** Cobertura de ramas y líneas $\ge 85\%$ en módulos de lógica de negocio.
  * **Tiempo de Ejecución de Pruebas:** Suite de pruebas de integración completa ejecutada en $\le 5\text{ minutos}$.
  * **Aislamiento de Defectos:** El $95\%$ de las fallas reproducidas en menos de $30\text{ minutos}$ gracias a trazas distribuidas.

---

### 2.7 Usabilidad (Usability)
Grado en el que el sistema permite a los usuarios alcanzar objetivos específicos con eficacia, eficiencia y satisfacción.

* **Fuentes Típicas:** Usuarios finales novatos, usuarios expertos, usuarios con capacidades especiales.
* **Estímulos Típicos:** Ejecución de un flujo de compra, configuración de perfil, recuperación de contraseña, error involuntario de entrada de datos.
* **Artefactos Impactados:** Interfaz de usuario (UI), flujo de experiencia (UX), validaciones de cliente.
* **Entornos Típicos:** Uso habitual en dispositivos móviles o web, situaciones de estrés o prisa del usuario.
* **Respuestas del Sistema (Tácticas):** Proveer feedback inmediato, prevención y recuperación de errores (mensajes claros, deshacer acción), diseño consistente y accesible (WCAG 2.1 AA).
* **Medidas de Respuesta Estándar:**
  * **Tiempo de Finalización de Tarea:** Completar checkout en $\le 90\text{ segundos}$.
  * **Tasa de Error del Usuario:** Menos del $3\%$ de errores de entrada en formularios críticos.
  * **Tiempo de Aprendizaje:** Usuarios nuevos completan su primera orden sin ayuda en $\le 5\text{ minutos}$.

---

### 2.8 Interoperabilidad (Interoperability)
Capacidad de intercambiar información útil y ejecutar servicios cooperativos de manera transparente con sistemas externos heterogéneos.

* **Fuentes Típicas:** Sistemas externos de terceros, servicios gubernamentales, socios comerciales, pasarelas de pago.
* **Estímulos Típicos:** Envío o recepción de mensajes en formatos estándar (JSON, XML, FHIR, ISO 8583), cambio de versión de API de socio.
* **Artefactos Impactados:** Adaptadores de integración, servicios de transformación de esquemas, bus de integración.
* **Entornos Típicos:** Redes corporativas seguras, internet pública, entornos multi-proveedor.
* **Respuestas del Sistema (Tácticas):** Mapear contratos de datos, gestionar compatibilidad retroactiva, manejar fallas transitorias de socios externos con *Circuit Breaker*.
* **Medidas de Respuesta Estándar:**
  * **Tasa de Éxito de Conversión:** $100\%$ de mensajes válidos parseados sin truncamiento.
  * **Compatibilidad de Versiones:** Soportar versión $N$ y $N-1$ de la API simultáneamente durante un período de gracia de 6 meses.
