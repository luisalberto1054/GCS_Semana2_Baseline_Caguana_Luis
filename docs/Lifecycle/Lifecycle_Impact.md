
El presente documento simula un cambio controlado dentro del ciclo de desarrollo de la **Aplicación de Turnos**, con el objetivo de evidenciar el impacto del cambio en cada fase y demostrar la importancia de la Gestión de la Configuración del Software (GCS), considerando que un cambio no controlado incrementa costos, reprocesos y riesgos.

---


**Caso 2 – Seguridad:**  
Implementación de **Autenticación de Dos Factores (2FA) para administradores**.

---



| Fase         | ¿Qué cambia?                                                                 | EC afectados                    | Riesgo si no se controla                                   | Evidencia de validación                    |
|--------------|------------------------------------------------------------------------------|---------------------------------|-------------------------------------------------------------|--------------------------------------------|
| Requisitos   | Se actualiza el requisito de seguridad para incluir 2FA y su criterio de aceptación | SRS_v1.md                       | Ambigüedad del requisito → retrabajo                        | Checklist de revisión de requisitos         |
| Diseño       | Se modifica el diseño de autenticación para incluir el segundo factor       | SDD_v1.md                       | Diseño inconsistente o incompleto                           | Revisión de diseño                          |
| Implementación | Se agrega lógica de validación del segundo factor (código backend)        | /src                            | Fallos de seguridad o errores en producción                 | Commit en repositorio                       |
| Configuración | Se añaden parámetros para el servicio de 2FA (tokens, claves, tiempo)     | /config/config.example          | Exposición de credenciales o fallas de ejecución            | Archivo de configuración validado           |
| Pruebas      | Se incorporan pruebas de autenticación con y sin 2FA                        | /tests                          | “Funciona en mi PC” / fallas no detectadas                  | Captura de ejecución de pruebas             |
| Documentación| Se actualiza la documentación técnica y de uso                              | /docs                           | Uso incorrecto del sistema                                  | Documento actualizado                       |

---



La simulación evidencia que un cambio en seguridad impacta múltiples fases del ciclo de vida del software. La ausencia de control formal sobre los elementos de configuración puede generar inconsistencias entre requisitos, diseño, código y pruebas, incrementando el riesgo operativo y los costos de corrección. La GCS permite asegurar trazabilidad, validación y control del cambio de manera integral.

---



- Tabla completa de impacto por fase  
- Commit del cambio registrado en el repositorio (posterior a la línea base)
