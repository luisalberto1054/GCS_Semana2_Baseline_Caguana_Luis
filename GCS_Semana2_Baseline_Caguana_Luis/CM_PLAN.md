

A continuación, se detallan los Elementos de Configuración (EC) identificados para el proyecto, indicando su ubicación, la justificación de control y el rol responsable de su modificación.

| EC                          | Ubicación            | ¿Por qué es EC?                                               | Quién lo modifica |
|-----------------------------|----------------------|----------------------------------------------------------------|-------------------|
| SRS_Aplicacion_Turnos.md    | /docs/SRS/           | Define los requerimientos; cambios afectan alcance y pruebas   | Analista / PO     |
| SDD_Aplicacion_Turnos.md    | /docs/SDD/           | Describe el diseño; impacta arquitectura y desarrollo          | Arquitecto / Dev |
| Casos_Prueba_Aplicacion.md  | /docs/Pruebas/       | Define validaciones; cambios afectan la calidad del sistema    | QA / Dev          |
| Program.cs                  | /src/                | Configura el arranque de la aplicación                         | Dev               |
| TurnosControlador.cs        | /src/Controladores/  | Implementa la lógica de la API REST                             | Dev               |
| Turno.cs                    | /src/Modelos/        | Define la entidad principal del negocio                         | Dev               |
| appsettings.example.json    | /config/             | Parametriza el sistema; afecta la ejecución                    | DevOps / Dev      |
| CM_PLAN.md                  | /docs/CM/            | Define reglas de control de configuración                      | Responsable CM    |

