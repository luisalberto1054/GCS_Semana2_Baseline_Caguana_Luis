

Para la evaluación de la calidad del software se adopta el modelo **ISO/IEC 25010**, el cual permite medir la calidad del producto mediante atributos claramente definidos y métricas verificables.  
Los atributos seleccionados responden a las características críticas de la Aplicación de Turnos y pueden ser evaluados objetivamente durante el desarrollo y pruebas.

---



| Atributo           | Definición (1 línea)                                      | Métrica verificable                                                                 | EC que lo soporta          |
|--------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------|
| Funcionalidad      | Capacidad del sistema para cumplir los requisitos definidos | ≥ 95% de los casos de prueba funcionales aprobados                                    | /tests, /src               |
| Rendimiento        | Capacidad de responder en tiempos aceptables               | Tiempo de respuesta ≤ 2 segundos en el 95% de las solicitudes                         | /src                       |
| Usabilidad         | Facilidad de uso e interacción del sistema                 | ≥ 80% de tareas completadas sin errores por usuarios de prueba                        | /src, /docs                |
| Seguridad          | Protección contra accesos y usos no autorizados            | 0 contraseñas almacenadas en texto plano                                              | /config, /src              |
| Mantenibilidad     | Facilidad para modificar el sistema sin introducir fallos  | Cobertura de pruebas ≥ 60% en funciones críticas                                      | /tests, /src               |
| Confiabilidad      | Capacidad de operar sin fallos durante un periodo definido | Disponibilidad ≥ 99% durante pruebas de ejecución                                     | /src, /config              |

---



Las siguientes métricas son consideradas **críticas** para el éxito del proyecto:

1. **Rendimiento:**  
   *El sistema debe responder en ≤ 2 segundos en el 95% de las solicitudes.*

2. **Seguridad:**  
   *El sistema no debe almacenar contraseñas en texto plano.*

Estas métricas son prioritarias debido a que impactan directamente en la experiencia del usuario y en la protección de la información.

---



- Tabla completa con **6 atributos del modelo ISO/IEC 25010**
- **2 métricas estrella claramente identificadas**
- Métricas formuladas de manera **objetiva, medible y verificable**
