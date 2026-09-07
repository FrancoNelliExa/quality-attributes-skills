# Template Canónico de Escenarios de Atributos de Calidad (SEI)

Según el Software Engineering Institute (SEI) y la metodología descrita en *Software Architecture in Practice* (Bass, Clements, Kazman), un escenario de atributo de calidad consta de seis partes fundamentales que eliminan la ambigüedad en los requerimientos arquitectónicos.

---

## Las 6 Partes del Escenario SEI

| # | Dimensión | Nombre en Inglés | Descripción Operacional | Pregunta Clave para Validar |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Fuente del estímulo** | *Source of stimulus* | La entidad o actor que origina el estímulo (humano, sistema externo, sensor, atacante, falla de hardware). | ¿Quién o qué genera el evento? |
| **2** | **Estímulo** | *Stimulus* | La condición o evento de activación que arriba al sistema y requiere una respuesta. | ¿Qué evento o condición ocurre? |
| **3** | **Artefacto** | *Artifact* | La parte delimitada del sistema que es estimulada (un microservicio, cola, base de datos, API Gateway). | ¿Qué componente específico recibe el impacto? |
| **4** | **Entorno** | *Environment* | El estado operacional bajo el cual ocurre el estímulo (operación normal, carga pico, modo degradado, despliegue). | ¿Bajo qué condiciones operativas está el sistema? |
| **5** | **Respuesta** | *Response* | El comportamiento o táctica arquitectónica observable que el sistema ejecuta ante el estímulo. | ¿Qué acciones directas realiza el sistema? |
| **6** | **Medida de respuesta** | *Response measure* | Métrica objetiva, numérica y verificable que determina si la respuesta satisface el requerimiento de calidad. | ¿Cómo se mide objetivamente el éxito de la respuesta? |

---

## Formato Estándar de Salida

Al formular o completar un escenario, se deben proporcionar siempre dos formatos complementarios:

### 1. Formato Tabular Estructurado
```markdown
| Parte | Especificación Arquitectónica |
| :--- | :--- |
| **Fuente del estímulo** | [Actor o entidad específica que origina el evento] |
| **Estímulo** | [Evento, carga o condición de entrada precisa] |
| **Artefacto** | [Componente, servicio o interfaz acotada del sistema] |
| **Entorno** | [Estado operacional y régimen de carga] |
| **Respuesta** | [Táctica o acción reactiva observable del sistema] |
| **Medida de respuesta** | [Métrica numérica cuantificable con unidades precisas (ms, TPS, %, RTO)] |
```

### 2. Formato Narrativo Estándar
> *"[Fuente] genera [Estímulo] sobre [Artefacto] bajo condiciones de [Entorno]. El sistema [Respuesta], garantizando [Medida de respuesta]."*

---

## Reglas Críticas de Redacción
* **Prohibición de adjetivos vagos:** Nunca emplear términos cualitativos como *"rápido"*, *"robusto"*, *"seguro"*, *"adecuado"* o *"eficiente"*. Toda medida debe llevar magnitudes físicas comprobables.
* **Separación causa/efecto:** La falla o solicitud es el **Estímulo**; la reacción de mitigación o procesamiento es la **Respuesta**.
* **Delimitación de frontera:** Evitar *"el sistema general"*; individualizar el componente arquitectónico receptor en el **Artefacto**.
